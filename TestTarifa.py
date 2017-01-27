'''
Created on 25 ene. 2017

@author: genekufatty
'''

import unittest

from tarifa import tarifa,calcularPrecio
from datetime import datetime

class Test(unittest.TestCase):
    
    def testtarifa(self):
        tarifa(2,3)
        
    def testtarifaFin(self):
        self.assertEqual(tarifa(1,3).getTarifaFin(),1)
    
    def testtarifaSem(self):
        self.assertEqual(tarifa(1,3).getTarifaSem(),3)    
    
    
if __name__ == '__main__':
    unittest.main()