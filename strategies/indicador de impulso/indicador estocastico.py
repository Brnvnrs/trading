class stocastic:
    pricesList:list[float]
    k:float
    d:float
    def __init__(self,pricesList:list[float]):
        self.pricesList= pricesList
        self.k = 0.0
        self.d = 0.0
        self.k_vals: list[float] = []

    def calculate_K(self,periodo:int)->None:

        self.k = 100*(self.pricesList[-1] - min(self.pricesList))/(max(self.pricesList) - min(self.pricesList))
        if(len(self.k_vals)>3):
            self.k_vals.pop(0)
            self.k_vals.append(self.k)
        else:
            self.k_vals.append(self.k)


    def calculate_D(self)->None:
        if(len(self.pricesList) <3):
            raise ValueError("la lista no es mayor/igual a 3")
        self.d = sum(self.k_vals)/3
        return self.d