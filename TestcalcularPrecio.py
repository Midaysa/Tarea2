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
    
    def testTarifaMinSem(self):
        time = [datetime(2017,1,25,1,0,0),datetime(2017,1,25,1,16,0)]
        self.assertEquals(calcularPrecio(self.prueba,time),1*self.prueba.getTarifaSem())
        
    def testTarifaMaximaFinCom(self):
        time = [datetime(2017,1,28,0,0,0),datetime(2017,1,30,0,0,0)]
        self.assertEquals(calcularPrecio(self.prueba,time),24*2*self.prueba.getTarifaFin())
        
    def testTarifaMaximaSemCom(self):
        time = [datetime(2017,1,30,0,0,0),datetime(2017,2,4,0,0,0)]
        self.assertEquals(calcularPrecio(self.prueba,time),24*5*self.prueba.getTarifaSem())
        
    def testTarifaMaxima(self):
        time = [datetime(2017,1,8,0,0,0),datetime(2017,1,15,0,0,0)]
        self.assertEquals(calcularPrecio(self.prueba,time),24*5*self.prueba.getTarifaSem()+24*2*self.prueba.getTarifaFin())
        
    def testfechamayor(self):
        with self.assertRaises(Exception) as context:
            time = [datetime(2016, 12,13,0,0,0), datetime(1996, 2,7,0,0,0)]
            calcularPrecio(tarifa(2,6),time)
        self.assertTrue('La hora de salida tiene que ser mayor' in str(context.exception))
    
    
if __name__ == '__main__':
    unittest.main()