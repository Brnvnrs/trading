import numpy as np
class Bollinger:
    topBand: np.ndarray[np.float32]
    middleBand: np.ndarray[np.float32]
    lowerBand:np.ndarray[np.float32]
    data: list
    def __init__(self,data:list):
        self.data = data
        self.topBand =np.array(data).mean()+2*data.std()
        self.middleBand =np.array(data).mean()
        self.lowerBand = np.array(data).mean()-2*data.std()


    def updateAtributes(self,valor:float):
        self.data