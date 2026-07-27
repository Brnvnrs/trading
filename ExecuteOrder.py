from binance_connection import ConexionABinance
from dataBase import DataBase
class ExecuteOrder():
    #atributos principales
    symbol: str
    db:DataBase
    #importamos el modulo de 
    def __init__(self,symbol:str):
        super().__init__()
        self.symbol = symbol
        self.db = DataBase()
    
    def executePurchase(self,amountToPurchase: float,currentPrice:float)->None:
        ##aca falta configurar que el monto a comprar tiene que ser multiplo de 0.00001000 y sea mayor al minimo de compra que es 0.00001
        self.cliente().order_market_buy(symbol=self.symbol,quantity=amountToPurchase)
        self.db.insertData(self.symbol,amountToPurchase,currentPrice,"Purchase")
        
    def executeSell(self,amountToSell: float,currentPrice:float)->None:
        self.cliente().order_market_sell(symbol=self.symbol,quantity=amountToSell)
        self.db.insertData(self.symbol,amountToSell,currentPrice,"Sell")
