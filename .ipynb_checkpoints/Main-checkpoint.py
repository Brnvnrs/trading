class Compra:
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
        
class Venta:
from dotenv import load_dotenv
from binance.client import Client
import os

class ConexionABinance:
    apiKey:str
    apiSecret:str
    def __init__(self,apiKey,apiSec):
        load_dotenv(override=True)
        self.apiKey = os.getenv('BINANCE_API_KEY')
        self.apiSecret = os.getenv('BINANCE_API_SECRET')
    def cliente(self):
        cliente =Client(self.apiKey,slef.apiSecret)
class Estrategia:
    conjuntoDeDatos: 
    