class Purchase:
    #atributos principales
    moneda: str
    cantidadAComprar: float
    #importamos el modulo de 
    def __init__(self,moneda,cantidadAComprar):
        self.moneda = moneda
        self.cantidadAComprar = cantidadAComprar
        #tenemos que importar el objeto de Conexion a Binance
    
    def ejecutarCompra(self,moneda,cantidad):
        ##aca falta configurar que el monto a comprar tiene que ser multiplo de 0.00001000 y sea mayor al minimo de compra que es 0.00001
        client.order_market_sell(symbol=self.moneda,quantity=self.cantidadAComprar)
        
