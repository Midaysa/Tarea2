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
    