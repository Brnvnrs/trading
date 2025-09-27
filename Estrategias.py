#esta clase debe decidir si se debe o no comprar o vender
import pandas as pd
from CompraVenta import 
class Estrategia(CompraVenta):
    list listaDePrecios
    float alpha = 0.05
    def __init__(self,listaDePrecios,tipoDeMoneda):
        self.listaDePrecios = listaDePrecios
        self.tipoDeMoneda = tipoDeMoneda
    def ultimoValor(precioMoneda:float):
        logPrecios = np.log(self.listaDePrecios)
        shape, loc, scale = lognorm.fit(log_precios, floc=0)
        
        prob = lognorm.cdf(precio_actual, shape, loc, scale)
        if(prob < alpha):
            #comprar
        else if(prob > 1-alpha):
            #vender
            
        