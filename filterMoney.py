from binance_connection import ConexionABinance
'''
LiquidityFilter
---------------
Clase que hereda de ConexionABinance y se encarga de filtrar monedas
por liquidez antes de operar con ellas.

Al instanciarse, obtiene automáticamente todos los pares USDT
disponibles en Binance. Al llamar al método filtrar(), analiza cada
par según tres criterios: volumen de las últimas 24hs, spread entre
el precio de compra y venta, y profundidad del libro de órdenes.
Las monedas que pasan el filtro quedan guardadas en self.listDeMonedas.

El objetivo es evitar entrar en monedas poco líquidas donde después
no se pueda salir por falta de compradores/vendedores.

'''
 
class LiquidityFilter(ConexionABinance):
    min_volumen: float
    max_spread: float
    min_profundidad: float
    listDeMonedas: list[str]
    symbols: list[str]
 
    def __init__(
        self,
        min_volumen: float = 500_000,
        max_spread: float = 0.1,
        min_profundidad: float = 10_000,
    ):
        super().__init__()
        self.min_volumen = min_volumen
        self.max_spread = max_spread
        self.min_profundidad = min_profundidad
        self.listDeMonedas = []
 
        client = self.cliente()
        exchangeInfo = client.get_exchange_info()
        self.symbols = [
            s["symbol"]
            for s in exchangeInfo["symbols"]
            if s["symbol"].endswith("USDT") and s["status"] == "TRADING"
        ]
 
    def _analizar(self, symbol: str) -> dict:
        client = self.cliente()
        ticker = client.get_ticker(symbol=symbol)
        volumen_24h = float(ticker["quoteVolume"])
 
        order_book = client.get_order_book(symbol=symbol, limit=5)
        mejor_ask = float(order_book["asks"][0][0])
        mejor_bid = float(order_book["bids"][0][0])
        spread_pct = ((mejor_ask - mejor_bid) / mejor_bid) * 100
 
        profundidad_bids = sum(float(b[0]) * float(b[1]) for b in order_book["bids"])
        profundidad_asks = sum(float(a[0]) * float(a[1]) for a in order_book["asks"])
 
        return {
            "symbol": symbol,
            "volumen_24h_usdt": volumen_24h,
            "spread_pct": spread_pct,
            "profundidad_bids": profundidad_bids,
            "profundidad_asks": profundidad_asks,
        }
 
    def _es_liquida(self, metricas: dict) -> bool:
        return (
            metricas["volumen_24h_usdt"] >= self.min_volumen
            and metricas["spread_pct"] <= self.max_spread
            and metricas["profundidad_bids"] >= self.min_profundidad
            and metricas["profundidad_asks"] >= self.min_profundidad
        )
 
    def filtrar(self, verbose: bool = True) -> None:
        self.listDeMonedas = []  # resetea por si se llama más de una vez
 
        for symbol in self.symbols:
            try:
                metricas = self._analizar(symbol)
                pasa = self._es_liquida(metricas)
 
                if verbose:
                    icono = "✅" if pasa else "❌"
                    print(
                        f"{icono} {symbol:<12} | "
                        f"Vol 24h: {metricas['volumen_24h_usdt']:>15,.0f} USDT | "
                        f"Spread: {metricas['spread_pct']:.3f}% | "
                        f"Prof.Bid: {metricas['profundidad_bids']:>10,.0f} USDT"
                    )
 
                if pasa:
                    self.listDeMonedas.append(symbol)
 
            except Exception as e:
                if verbose:
                    print(f"⚠️  {symbol:<12} | Error: {e}")
 
        if verbose:
            print(f"\n📊 {len(self.listDeMonedas)}/{len(self.symbols)} monedas pasaron el filtro.")
