from binance_connection import ConexionABinance
from binance.client import Client
from filterMoney import LiquidityFilter
from CandleList import CandleList
from strategy import Estrategia


monedasFiltradas = LiquidityFilter()

monedasFiltradas.filtrar()
print(monedasFiltradas.listDeMonedas)


for monedas in monedasFiltradas.listDeMonedas:
    # por cada moneda tendriamos que traer al menos sus ultimos 14 valores al cierre
    # y luego aplicar una estrategia para cada moneda y despues ir actualizando el valor de esa moneda y nuevamente aplicar la esdtrategia
    intervalos = {
        "1": Client.KLINE_INTERVAL_1MINUTE,
        "5": Client.KLINE_INTERVAL_5MINUTE,
        "15": Client.KLINE_INTERVAL_15MINUTE,
        "30": Client.KLINE_INTERVAL_30MINUTE,
        "1h": Client.KLINE_INTERVAL_1HOUR,
        "4h": Client.KLINE_INTERVAL_4HOUR,
        "1d": Client.KLINE_INTERVAL_1DAY,
    }
    lista = CandleList(monedas, intervalos{1} ,14)    
    #aca se aplicaria una o varias estrategias por cada moneda 

# the main idea
# get prices => update state => execute strategy => get prices ...

#we need to know if the conditions are well 
#if the conection to internet is good or we can't conect to the data base and more 
# WE NEED TO KNOW THAT
flags = ConditionsToExecuteTheProgram()



listOfPrices = LiquidityFilter() # we have all the values like(BTC,ETH...) 
listOfPrices.filtrar() # we gonna filter the values(there is an explain in the module)
btc=listOfPrices.value("btc") # this method doesn't exist now, but it represent a value  


#we gonna take one value (BTC)

stgy = Estrategia(btc)

while(True):
    if(flags.mains()):#it must looking for errors in the conection to internet and report
        if(stgy.conditionsToPurchaseOrSell()):# it tell us if there are a posiblie to sell or purchase but no wich one 
            # i'm thinking that it won't save complexity in our program becouse the 80% or 90% from the work was done 

