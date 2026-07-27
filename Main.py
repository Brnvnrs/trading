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

# get prices => update state => execute strategy => get prices ...
flags = ConditionsToExecuteThisProgram()

listOfPrices = LiquidityFilter()
listOfPrices.filtrar() # his atribute get a list[str] with the name of every crypto to use in strategy

strategyRightNow = Estrategia(listOfPrices.dictMoney)

strategyRightNow.update(listOfPrices.update())
while(True):
    if(flags.status()):#for example if the conection to internet doesn't work,the binanceAPI doesn't work,etc so we can't continue
        if(strategyRightNow.currentState()):#if every flag are 
            strategyRightNow.executeOrder()












# def obtener_cierres(symbol: str, intervalo: str, cantidad: int = 14) -> list[float]:
#     client = ConexionABinance().cliente()
#     klines = client.get_historical_klines(symbol, intervalo, limit=cantidad)
#     return [float(k[4]) for k in klines]  # índice 4 = precio de cierre

# def main():
#     symbol = input("Ingresá el símbolo (ej: BTCUSDT): ").upper()

#     print("\nIntervalos disponibles:")
#     for key in INTERVALOS:
#         print(f"  {key}")

#     eleccion = input("\nElegí el intervalo: ").strip()

#     if eleccion not in INTERVALOS:
#         print("Intervalo no válido.")
#         return

#     cierres = obtener_cierres(symbol, INTERVALOS[eleccion])

#     print(f"\nÚltimos 14 cierres de {symbol} en intervalo {eleccion}:")
#     for i, precio in enumerate(cierres, 1):
#         print(f"  {i:>2}. {precio:.4f} USDT")

# if __name__ == "__main__":
#     main()