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
        cliente =Client(self.apiKey,self.apiSecret)


