'PRUEBAS DE UNIDAD'
'''El primer y segundo paréntesis son los números a operar y el tercero es el
resultado correspondiente a cada operación'''

#Los números complejos se representa de la forma a+bi=c o en este caso (a,b)

'''Nota:Los casos de prueba se realizaron sin ningún tipo de redondeo para no descartar ninguna cifra decimal'''


import unittest
import Complejos
import math

class unit_complejos(unittest.TestCase):
    '-----------------------------------Operaciones básicas-----------------------------------'
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

    #Pruebas para el módulo.
    def test_modulo(self):
        self.assertEqual(Complejos.modulo((4,-3)),(5))
        self.assertEqual(Complejos.modulo((6,-3)),(6.708203932499369))

    #Pruebas para la división.
    def test_division(self):
        self.assertEqual(Complejos.division((4,12),(6,2)),(1.2,1.6))
        self.assertEqual(Complejos.division((0,3),(-1,-1)),(-1.5,-1.5))

    #Pruebas para la conversión de representación polar a cartesiana.
    def test_pol_a_car(self):
        self.assertEqual(Complejos.pol_a_car((3,math.pi/3)),(1.5000000000000004,2.598076211353316))
        self.assertEqual(Complejos.pol_a_car((4,math.pi/6)),(3.464101615137755,1.9999999999999998))

    #Pruebas para la conversión de representación cartesiana a polar.
    def test_car_a_pol(self):
        self.assertEqual(Complejos.car_a_pol((-3,-1)),(3.1622776601683795,198.43494882292202))
        self.assertEqual(Complejos.car_a_pol((1,1)),(1.4142135623730951,45))

    #Pruebas para la fase.
    def test_fase(self):
        self.assertEqual(Complejos.fase((3,2)),(33.690067525979785))
        self.assertEqual(Complejos.fase((-3,2)),(146.30993247402023))
        self.assertEqual(Complejos.fase((-3,-2)),(213.69006752597977))
        self.assertEqual(Complejos.fase((3,-2)),(326.30993247402023))

    '-----------------------------------Vectores-----------------------------------'
    #Pruebas para la suma de vectores.
    def test_sumaVector(self):
        self.assertEqual(Complejos.sumaVector([(8,3),(-1,-4),(0,-9)],[(8,-3),(2,5),(3,0)]),[(16,0),(1,1),(3,-9)])
        self.assertEqual(Complejos.sumaVector([(3, 2),(3, 4),(5, 6)],[(2, 1),(5, 4),(6,3)]),[(5,3),(8,8),(11,9)])

    #Pruebas para el inverso aditivo de un vector.
    def test_inversaVector(self):
        self.assertEqual(Complejos.inversaVector([(9,3),(-1,-5),(6,-4)]),[(-9,-3),(1,5),(-6,4)])
        self.assertEqual(Complejos.inversaVector([(-5,2),(3,0),(0,-1)]),[(5,-2),(-3,0),(0,1)])

    #Pruebas para la multiplicación escalar de un vector.
    def test_escalarVector(self):
        self.assertEqual(Complejos.escalarVector((3,2),[(6,3),(0,0),(5,1),(4,0)]),[(12,21),(0,0),(13,13),(12,8)])
        self.assertEqual(Complejos.escalarVector((-1,1),[(-2,5),(-1,-1),(2,-9)]),[(-3,-7),(2,0),(7,11)])

    #Pruebas para la distancia entre vectores.
    def test_distanciaVector(self):
         self.assertEqual(Complejos.distanciaVector([(2,7),(4,-1),(2,-4)],[(7,8),(2,-8),(1,4)]),12)
         self.assertEqual(Complejos.distanciaVector([(9,-7),(-1,-6)],[(7,-8),(5,-9)]),7.0710678118654755)

    #Pruebas para el producto interno de vectores.
    def test_productoInterno(self):
        self.assertEqual(Complejos.productoInterno([(1,1),(3,0)],[(1,1),(0,1)]),(2,3))
        self.assertEqual(Complejos.productoInterno([(2,-1),(-8,-5),(-2,-6)],[(6,-3),(5,-1),(-6,-2)]),(4,1))

    #Pruebas para la norma de vectores.
    def test_normaVector(self):
        self.assertEqual(Complejos.normaVector([(4,3),(6,-4),(12,-7),(0,13)]),20.952326839756964)
        self.assertEqual(Complejos.normaVector([(4,5),(3,1),(0,-7)]),10)

    '----------------------------------Matrices---------------------------------'
    #Pruebas para la suma de matrices.
    def test_sumaMatriz(self):
        self.assertEqual(Complejos.sumaMatriz([[(-8,-3),(-6,-4),(0,-4)],[(-1,8),(6,-10),(8,-5)],[(4,0),(8,5),(-7,-9)]],[[(-7,-2),(-4,-2),(7,7)],[(5,9),(0,3),(6,-5)],[(1,5),(-6,-6),(5,8)]]),[[(-15,-5),(-10,-6),(7,3)],[(4,17),(6,-7),(14,-10)],[(5,5),(2,-1),(-2,-1)]])
        self.assertEqual(Complejos.sumaMatriz([[(2,3),(1,1)],[(4,5),(2,1)]],[[(4,5),(1,1)],[(2,1),(1,1)]]),[[(6,8),(2,2)],[(6,6),(3,2)]])

    #Pruebas para el inverso aditivo de una matriz.
    def test_inversaMatriz(self):
        self.assertEqual(Complejos.inversaMatriz([[(3,4),(6,1)],[(-2,8),(7,-6)],[(0,-1),(5,-4)]]),[[(-3,-4),(-6,-1)],[(2,-8),(-7,6)],[(0,1),(-5,4)]])
        self.assertEqual(Complejos.inversaMatriz([[(7,3),(-1,7)],[(-9,-4),(-7,-9)]]),[[(-7,-3),(1,-7)],[(9,4),(7,9)]])

    #Pruebas para la multiplicación escalar de una matriz.
    def test_escalarMatriz(self):
        self.assertEqual(Complejos.escalarMatriz((3,2),[[(4,5),(1,1)],[(2,1),(1,1)]]),[[(2,23),(1,5)],[(4,7),(1,5)]])
        self.assertEqual(Complejos.escalarMatriz((-2,3),[[(3,-2),(8,-4)],[(4,-10),(-2,-8)]]),[[(0,13),(-4,32)],[(22,32),(28,10)]])

    #Pruebas para la transpuesta de una matriz.
    def test_matrizTranspuesta(self):
        self.assertEqual(Complejos.matrizTranspuesta([[(4,9),(1,-3)],[(5,1),(6,8)]]),[[(4,9),(5,1)],[(1,-3),(6,8)]])
        self.assertEqual(Complejos.matrizTranspuesta([[(5,9),(-7,-5),(-1,-4)],[(8,2),(-3,-7),(7,-8)]]),[[(5,9),(8,2)],[(-7,-5),(-3,-7)],[(-1,-4),(7,-8)]])

    #Pruebas para la matriz conjugada.
    def test_matrizConjugada(self):
        self.assertEqual(Complejos.matrizConjugada([[(-6,1),(3,8)],[(2,-6),(3,0)]]),[[(-6,-1),(3,-8)],[(2,6),(3,0)]])
        self.assertEqual(Complejos.matrizConjugada([[(5,4),(3,2),(5,0)],[(1,1),(6,3),(8,9)]]),[[(5,-4),(3,-2),(5,0)],[(1,-1),(6,-3),(8,-9)]])

    #Pruebas para la adjunta o daga de una matriz.
    def test_matrizAdjunta(self):
        self.assertEqual(Complejos.matrizAdjunta([[(7,7),(3,8),(8,4)],[(5,0),(8,-6),(-10,-1)]]),[[(7,-7),(5,0)],[(3,-8),(8,6)],[(8,-4),(-10,1)]])
        self.assertEqual(Complejos.matrizAdjunta([[(5,4),(6,5)],[(8,7),(6,6)]]),[[(5,-4),(8,-7)],[(6,-5),(6,-6)]])

    #Pruebas para el producto de matrices.
    def test_productoMatriz(self):
        self.assertEqual(Complejos.productoMatriz([[(-6,2),(0,6),(7,2)],[(6,9),(7,7),(-6,-6)],[(5,8),(-6,8),(6,9)]],[[(9,-6),(-3,-4),(5,-2)],[(3,6),(-1,-5),(0,-5)],[(9,9),(8,-4),(-8,-4)]]),
                         [[(-33,153),(120,0),(-44,-22)],[(87,0),(-26,-117),(107,70)],[(0,165),(147,26),(69,-36)]])
        with self.assertRaises(ValueError):
            (Complejos.productoMatriz([[(2,1),(3,0),(1,-1)],[(0,0),(0,-2),(7,-3)],[(3,0),(0,0),(1,-2)]],[[(0,-1),(1,0)],[(0,0),(0,1)]]))

    #Pruebas para la acción de matriz sobre vector.
    def test_accionMatriz(self):
        self.assertEqual(Complejos.accionMatriz([[(-1,5),(1,-7),(-6,3)],[(-3,-9),(2,-5),(1,-10)],[(-6,5),(6,-5),(3,-2)]],[(1,-3),(4,3),(-3,1)]),[(54,-32),(0,17),(41,30)])
        with self.assertRaises(ValueError):
            (Complejos.accionMatriz([[(2,1),(3,0),(1,-1)],[(0,0),(0,-2),(7,-3)]],[(1,4),(6,-3)]))

    #Pruebas para la matriz unitaria.
    def test_matrizUnitaria(self):
        self.assertEqual(Complejos.matrizUnitaria([[(0,1),(1,0),(0,0)],[(0,0),(0,1),(1,0)],[(1,0),(0,0),(0,1)]]),False)
        self.assertEqual(Complejos.matrizUnitaria([[(1,0),(-1,1)],[(1,1),(1,0)]]),True)

    #Prueba para la matriz hermitiana.
    def test_matrizHermitiana(self):
        self.assertEqual(Complejos.matrizHermitiana([[(3,0),(2,-1),(0,-3)],[(2,1),(0,0),(1,-1)],[(0,3),(1,1),(0,0)]]),True)
        self.assertEqual(Complejos.matrizHermitiana([[(1,0),(3,-1)],[(3,1),(0,1)]]),False)

    #Prueba para el producto tensorial.
    def test_productoTensor(self):
        self.assertEqual(Complejos.productoTensor([[(1,1),(0,0)],[(1,0),(0,1)]],[[(-1,2),(-2,-2),(0,2)],[(2,3),(3,1),(2,2)],[(-2,1),(1,-1),(2,1)]]),
                         [[(-3,1),(0,-4),(-2,2),(0,0),(0,0),(0,0)],[(-1,5),(2,4),(0,4),(0,0),(0,0),(0,0)],[(-3,-1),(2,0),(1,3),(0,0),(0,0),(0,0)],[(-1,2),(-2,-2),(0,2),(-2,-1),(2,-2),(-2,0)],
                          [(2,3),(3,1),(2,2),(-3,2),(-1,3),(-2, 2)],[(-2,1),(1,-1),(2,1),(-1,-2),(1,1),(-1,2)]])

unittest.main()
