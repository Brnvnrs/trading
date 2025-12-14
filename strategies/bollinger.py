from Purchase import Purchase
from Sell import Sell
import numpy as np
class Bollinger:
    '''la idea de las bandas de bollinger es que nos diga la volatilidad del mercado'''
    topBand: np.ndarray[np.float32]
    middleBand: np.ndarray[np.float32]
    lowerBand:np.ndarray[np.float32]
    data: list
    def __init__(self,data:list):
        super().__init__()
        '''la iidea es recibir un set de datos(90 dias) y calcular las bandas'''
        self.__data = data
        self.__topBand =np.array(self.__data).mean()+2*np.array(self.__data).std()
        self.__middleBand =np.array(self.__data).mean()
        self.__lowerBand = np.array(self.__data).mean()-2*np.array(self.__data).std()

    def toString(self):
        return self.__topBand,self.__middleBand,self.__lowerBand
    
    def updateAtributes(self,valor:float)->None:
        '''la idea es recibir un valor y actualizar los valores de las bandas'''
        del self.__data[0]
        self.__data.append(valor)
        self.__topBand =np.array(self.__data).mean()+np.array(self.__data).std()
        self.__middleBand =np.array(self.__data).mean()
        self.__lowerBand = np.array(self.__data).mean()-np.array(self.__data).std()
    
    def overbought(self,valor:float)->bool:
        '''si el precio es mayor a la banda superior'''
        self.updateAtributes(valor)
        return valor > self.topBand

    def oversold(self,valor:float)->bool:
        '''si el precio es menor a la banda inferior'''
        self.updateAtributes(valor)
        return valor < self.lowerBand

    # la idea seria comprar cuando haya sobreventa y vender cuando haay sobrecompra 
    def ejecucionDeEstrategia(self,valor:float,cantidadAComprarOVender:float)->None:
        self.updateAtributes(valor)
        if(self.overbought):
            #compro
            Purchase.ejecutarCompra(cantidadAComprarOVender)
        elif(self.oversold):
            #vendo
            Sell.ejecutarVenta(cantidadAComprarOVender)
        
    def simulation(self,valor:float)->None:
        
        print(f"mis atributos antes de actualizar son \n {self.toString()} \n")
        self.updateAtributes(valor)
        print(f"actualizando los atributos me quedo con \n {self.toString()}\n")
        if(self.overbought):
            #compro
            print(f"ccomo hay sobrecompra vendemos \n")

        elif(self.oversold):
            #vendo
            print(f"como hay sobrevenra vendemos\n")
        else:
            print(f"como no hay niguna de las dos, no compro ni vendo\n")


