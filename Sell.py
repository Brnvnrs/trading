from binance_connection import ConexionABinance

class Sell:
    moneda:str
    
    def __init__(self,moneda:str):
        super().__init__
        self.moneda = moneda
    
    def ejecutarVenta(self,cantidadAVender: float)->None:
        self.cliente().order_market_sell(symbol=self.moneda,quantity=cantidadAVender)
