from binance_connection import ConexionABinance

class CandleList():
    # candleList:list[]
    # symbol:str
    # period:str
    # lenght:int
    pricesList:list[list]
    def __init__(self,symbol:str,period:str,length:int):
        # self.candleList=CandleList.Candle 
        super().__init__()
        self.pricesList= self.cliente().get_klines(symbol,period,length)

    """ 
    now my pricesList is a list of candle where every candle look like this
    [
        [
            1499040000000,      # 0 open_time (timestamp)
            "0.01634790",       # 1 open
            "0.80000000",       # 2 high
            "0.01575800",       # 3 low
            "0.01577100",       # 4 close
            "2235.19400",       # 5 volume
            1499644799999,      # 6 close_time
            "17.00000000",      # 7 quote_asset_volume
            123,                # 8 number_of_trades
            "1000.00000000",    # 9 taker_buy_base_asset_volume
            "8.00000000",       # 10 taker_buy_quote_asset_volume
            "0"                 # 11 ignore
        ],
        # ... más velas
    ]
    """
    def closePrices(self)->
        auxList = []
        for 
