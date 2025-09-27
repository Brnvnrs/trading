from dotenv import load_dotenv
import os
from binance.client import Client

class ConexionBinance:
    
    #la idea seria que cargando el metodo principal ya pueda tener acceso a binance
    def __init__(self,api_key,api_secret):
        