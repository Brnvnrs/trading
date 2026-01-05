# strategies/bollinger.py

import numpy as np
import time

class Bollinger:
    """
    Bandas de Bollinger con ventana móvil
    - Compra cuando precio < lower band (oversold)
    - Vende cuando precio > upper band (overbought)
    - Gestión de posición, comisiones y capital compuesto
    - SIN prints para evitar saturación en backtest/live
    """
    def __init__(self, data_inicial: list[float], periodo: int = 20, desvios: float = 2.0,
                 capital_inicial_usdt: float = 10.0, comision: float = 0.001):
        self.periodo = periodo
        self.desvios = desvios
        self.comision = comision
        
        # Ventana móvil de precios
        self.data = list(data_inicial[-periodo:])  # últimos 'periodo' precios
        
        # Gestión de capital y posición
        self.capital_usdt = capital_inicial_usdt
        self.cantidad_crypto = 0.0
        self.en_posicion = False
        self.precio_entrada = 0.0
        self.ganancia_acumulada = 0.0
        
        # Calculamos bandas iniciales
        self._calcular_bandas()

    def _calcular_bandas(self):
        """Actualiza las bandas con los datos actuales"""
        if len(self.data) < self.periodo:
            return
        precios = np.array(self.data)
        self.middle = precios.mean()
        self.std = precios.std()
        self.upper = self.middle + self.desvios * self.std
        self.lower = self.middle - self.desvios * self.std

    def update(self, precio_nuevo: float):
        """Actualiza la ventana móvil y recalcula bandas"""
        if len(self.data) >= self.periodo:
            self.data.pop(0)
        self.data.append(precio_nuevo)
        self._calcular_bandas()

    def es_overbought(self, precio: float) -> bool:
        return precio > self.upper

    def es_oversold(self, precio: float) -> bool:
        return precio < self.lower

    def signal(self, precio: float, simbolo: str):
        """Evalúa señal y ejecuta compra/venta de forma silenciosa"""
        self.update(precio)

        if self.es_oversold(precio) and not self.en_posicion:
            # === COMPRA (oversold) ===
            cantidad = (self.capital_usdt * (1 - self.comision)) / precio
            self.en_posicion = True
            self.cantidad_crypto = cantidad
            self.precio_entrada = precio

        elif self.es_overbought(precio) and self.en_posicion:
            # === VENTA (overbought) ===
            usdt_recibidos = self.cantidad_crypto * precio * (1 - self.comision)
            ganancia = usdt_recibidos - (self.cantidad_crypto * self.precio_entrada * (1 + self.comision))
            self.ganancia_acumulada += ganancia
            
            self.capital_usdt = usdt_recibidos
            self.en_posicion = False
            self.cantidad_crypto = 0.0
            self.precio_entrada = 0.0

        # No hay else con print → completamente silencioso

    def get_capital_actual(self, precio_actual: float) -> float:
        """Devuelve el valor actual de la cartera para backtest/resumen"""
        return self.cantidad_crypto * precio_actual if self.en_posicion else self.capital_usdt