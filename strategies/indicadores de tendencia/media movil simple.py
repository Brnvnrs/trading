class mms:
    priceList:list[float]
    def __init__(self,pricesList:list[float]):
        self.pricesList = pricesList

    def length(self)->int:
        return self.pricesList.length()

    def update(self,value:float)->None:
        self.pricesList.pop(0)
        self.pricesList.append(value)
    def mean(self)->float:
        return sum(self.pricesList)/ len(self.pricesList)

