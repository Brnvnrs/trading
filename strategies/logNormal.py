import numpy as np
from scipy.stats import lognorm
from Sell import Sell
from Purchase import Purchase

class LogNorm:
    listaPrecios:np.ndarray[np.float32]
    umbral:np.float32
    shape:np.float32
    loc:np.float32
    scale:np.float32
    def __init__(self,listaPrecios:list,umbral:np.float32):
        self.__listaPrecios = np.array(listaPrecios)
        self.__umbral = umbral
        #shape seria el std, scale la mediana pero es igual a e^(media) y loc es simplemente un desplazamiento pero como aqui los valores del precio siempre son positivos no es necesario desplazar nada por lo tanto es igual a cero
        self.shape, self.loc, self.scale = lognorm.fit(self.__listaPrecios, floc=0)

    
    def priceUpdate(self,newPrice:np.float32)->None:
        self.__listaPrecios = self.__listaPrecios[1:]
        self.__listaPrecios = np.append(self.__listaPrecios,newPrice)
        self.shape, self.loc, self.scale = lognorm.fit(self.__listaPrecios, floc=0)
    
    def priceSignal(self,newPrice:np.float32,quantity:np.float32,moneda:str)->None:
        ''' si el nuevo precio esta por debajo del unbra o es superior a 1-umbral es porque hau una señal de compra y venta respectivamente '''
        prob = lognorm.cdf(newPrice,self.shape,self.loc,self.scale)
        if prob < self.__umbral:
            print(f"se ejecutará una orden de compra de la moneda: {moneda} por el monto de : {quantity} \n")
            compra = Purchase(moneda)
            compra.ejecutarCompra(quantity)
        elif prob > 1-self.__umbral:
            print(f"se ejecutará una orden de venta de la moneda: {moneda} por el monto de : {quantity} \n")
            venta = Sell(moneda)
            venta.ejecutarVenta(quantity)
        else:
            print(f"actualizacion de datos \n como el precio no esta fuera del rango de los umbrales no se hace nada \n los datos actuales son: Precio actual : {newPrice} \n Probabilidad acumulada: {prob} \n La mediana es: {self.scale} y la desviacion Standar es: {self.shape}")
