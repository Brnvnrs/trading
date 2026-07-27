from CandleList import CandleList
from spicy.stats import lognorm
from Sell import Sell

class LogNormal:
    #atributos 
    prices:CandleList
    thresold:float
    #constructor
    def __init__(self,symbol:str,thresold:float=0.15):
        self.symbol = symbol
        self.prices = CandleList(self.symbol)
        self.thresold = thresold

    #methods
    def parameters(self):
        shape, loc, scale = lognorm.fit(self.prices, floc=0)

    def purchaseOrBuy(self,newPrice:float):
        shape, loc, scale = lognorm.fit(self.prices, floc=0)
        prob = lognorm.cdf(newPrice,shape,loc,scale)
        if(prob>1-self.thresold):
            Sell.ejecutarVenta(self.symbol)
