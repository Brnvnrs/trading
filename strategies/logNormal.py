import time
import numpy as np
from scipy.stats import lognorm

class LogNorm:
    def __init__(self, lista_precios_inicial: list[float], umbral: float = 0.15,
                 capital_inicial_usdt: float = 10.0, comision: float = 0.001,
                 stop_loss_pct: float = 0.15):
        self.__lista_precios = np.array(lista_precios_inicial, dtype=float)
        self.__umbral = umbral
        self.comision = comision                    # 0.001 = 0.1%
        self.stop_loss_pct = stop_loss_pct          # 15% de pérdida máxima
        
        # === GESTIÓN DE CAPITAL Y POSICIÓN ===
        self.capital_usdt = capital_inicial_usdt
        self.cantidad_crypto = 0.0
        self.en_posicion = False
        self.precio_entrada = 0.0
        self.ganancia_total_acumulada = 0.0
        self.capital_peak = capital_inicial_usdt

        # Ajuste inicial
        self.shape, self.loc, self.scale = lognorm.fit(self.__lista_precios, floc=0)

    def priceUpdate(self, newPrice: float) -> None:
        self.__lista_precios = np.append(self.__lista_precios[1:], newPrice)
        self.shape, self.loc, self.scale = lognorm.fit(self.__lista_precios, floc=0)

    def priceSignal(self, newPrice: float, moneda: str) -> None:
        prob = lognorm.cdf(newPrice, self.shape, self.loc, self.scale)
        
        # si la prob < umbral o prob > 1-umbral hay sobre compra o sobreventa 
        if prob < self.__umbral and not self.en_posicion:
            self.en_posicion = True
            # 1 BTC ________ newprice USD
            # X BTC ________ 10 USD aca X es nuestra incognita 
            self.precio_entrada = newPrice
            self.cantidad_crypto = self.capital_usdt/newPrice
            print(f"compro 10 USD al precio de: 1 BTC _____ {newPrice} USD")
        elif self.en_posicion: 
            ''' aca es medio delicado porque no necesariamente tenemos que vender cuando la cripto esta sobrecomprada si el valor de la misma esta en el promedio yo la venderia
            Por el momento vamos a vender si el precio es mayor al proemdio'''
            if prob >0.5:
                ''' aca es lo mismo que antes pero al reves, tenemos la X pero ya no vamos a tener 10 USD, esperemos que mas :D '''
                self.capital_peak = self.cantidad_crypto*newPrice 
                self.ganancia_total_acumulada = self.capital_peak-self.capital_usdt
                self.capital_usdt = self.capital_peak
                self.cantidad_crypto = 0
                print(f"vendo toda la cripto que tenga")
