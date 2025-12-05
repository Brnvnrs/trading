from dotenv import load_dotenv
from binance.client import Client
import os
from pathlib import Path



class ConexionABinance:
    apiKey:str
    apiSecret:str
    def __init__(self):
        env_path = Path("/home/brian/Documentos/.env")
        load_dotenv(dotenv_path=env_path, override=True)
        self.apiKey = os.getenv('BINANCE_API_KEY')
        self.apiSecret = os.getenv('BINANCE_API_SECRET')
    def cliente(self):
        return Client(self.apiKey,self.apiSecret)

