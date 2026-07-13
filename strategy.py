#esta clase debe decidir si se debe o no comprar o vender
from binance_connection import ConexionABinance
import numpy as np
from CandleList import CandleList
class PrecioActual(ConexionABinance):
    
    #la idea es que se ingrese el tipo de moneda ya sea BTCUSDT o el quue sea y el metodo precio me devuelva el precio actual de esa moneda
    cliente:ConexionABinance
    symbol:str
    def __init__(self, symbol: str):
        super().__init__()                    # Esto crea self.client correctamente
        self.symbol = symbol.upper()
    def precio(self)->float:
        return float(self.cliente().get_symbol_ticker(symbol=self.symbol)["price"])


class Estrategia():

    #atributos 
    dictMoney:dict[str,CandleList]

    #constructor
    def __init__(self,dictMoney:dict[str,CandleList]):
        self.dictMoney = dictMoney
    def update():
        pass 
