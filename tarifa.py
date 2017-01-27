'''
Created on 25 ene. 2017

@author: genekufatty
'''

from datetime import *

class tarifa():

    def __init__(self,tarifaFin,tarifaSem):
        self.tarifaFin = tarifaFin
        self.tarifaSem = tarifaSem

    def getTarifaSem(self):
        return self.tarifaSem
    
    def getTarifaFin(self):
        return self.tarifaFin
    
    
def calcularPrecio(tarifa,tiempoDeServicio):
    total = 0
    start_date =tiempoDeServicio[0]
    end_date = tiempoDeServicio[1]
    
    if (tiempoDeServicio[0] > tiempoDeServicio[1]):
        raise Exception('La hora de salida tiene que ser mayor')
     
    d = start_date
    delta = timedelta(seconds=3600)
    while d < end_date:
        if (d.weekday() == 6 or d.weekday() == 5) : 
            total += tarifa.getTarifaFin()
        else : 
            total += tarifa.getTarifaSem()
        d += delta
        
    return total