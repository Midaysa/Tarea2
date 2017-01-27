'''
Created on 25 ene. 2017

@author: Midaysa
'''

import unittest

from tarifa import tarifa,calcularPrecio
from datetime import datetime

class Test(unittest.TestCase):
    
    def setUp(self):
        self.prueba = tarifa(2,14)
        
    def testTarifaMinFin(self):
        time = [datetime(2017,1,28,1,0,0),datetime(2017,1,28,1,16,0)]
        self.assertEquals(calcularPrecio(self.prueba,time),1*self.prueba.getTarifaFin())
    
    
if __name__ == '__main__':
    unittest.main()