from binance_connection import ConexionABinance
class Purchase():
    #atributos principales
    moneda: str
    #importamos el modulo de 
    def __init__(self,moneda:str):
        super().__init__()
        self.moneda = moneda
        #tenemos que importar el objeto de Conexion a Binance
    
    def ejecutarCompra(self,cantidadAComprar: float)->None:
        ##aca falta configurar que el monto a comprar tiene que ser multiplo de 0.00001000 y sea mayor al minimo de compra que es 0.00001
        self.cliente().order_market_buy(symbol=self.moneda,quantity=cantidadAComprar)
        
