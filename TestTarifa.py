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
    
    
if __name__ == '__main__':
    unittest.main()