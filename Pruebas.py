'PRUEBAS DE UNIDAD'
'''El primer y segundo parentesis son los números a operar y el tercero es el
resultado correspondiente a cada operación'''
#Los números complejos se representa de la forma a+bi=c o en este caso (a,b)

import unittest
import Complejos
import math

class unit_complejos(unittest.TestCase):
    #Pruebas para la suma.
    def test_sumar(self):
        self.assertEqual(Complejos.sumar((4,5),(5,2)),(9,7))
        self.assertEqual(Complejos.sumar((1,5),(0,2)),(1,7))

    #Pruebas para la resta.
    def test_restar(self):
        self.assertEqual(Complejos.restar((1,5),(0,2)),(1,3))
        self.assertEqual(Complejos.restar((3,1),(4,1)),(-1,0))

    #Pruebas para la multiplicación.
    def test_producto(self):
        self.assertEqual(Complejos.producto((-2,-1),(-1,-2)),(0,5))
        self.assertEqual(Complejos.producto((-2,-1),(1,-3)),(-5,5))

    #Pruebas para el conjugado.
    def test_conjugado(self):
        self.assertEqual(Complejos.conjugado((-2,-1)),(-2,1))
        self.assertEqual(Complejos.conjugado((-2,1)),(-2,-1))

    #Pruebas pra el módulo.
    def test_modulo(self):
        self.assertEqual(Complejos.modulo((4,-3)),(5))
        self.assertEqual(Complejos.modulo((6,-3)),(6.71))

    #Pruebas para la división.
    def test_division(self):
        self.assertEqual(Complejos.division((4,12),(6,2)),(1.2,1.6))
        self.assertEqual(Complejos.division((0,3),(-1,-1)),(-1.5,-1.5))

    #Pruebas para la conversión de representación polar a cartesiana.
    def test_pol_a_car(self):
        self.assertEqual(Complejos.pol_a_car((3,math.pi/3)),(1.5,2.6))
        self.assertEqual(Complejos.pol_a_car((4,math.pi/6)),(3.46,2))

    #Pruebas para la conversión de representación cartesiana a polar.
    def test_car_a_pol(self):
        self.assertEqual(Complejos.car_a_pol((-2,-1)),(2.24,26.57))
        self.assertEqual(Complejos.car_a_pol((1,2)),(2.24,63.43))

    #Pruebas para la fase.
    def test_fase(self):
        self.assertEqual(Complejos.fase((3,2)),(34))
        self.assertEqual(Complejos.fase((-3,2)),(146))
        self.assertEqual(Complejos.fase((-3,-2)),(214))
        self.assertEqual(Complejos.fase((3,-2)),(326))

unittest.main()