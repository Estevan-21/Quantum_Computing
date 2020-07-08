from TeoriaCuanticaBasica import TeoriaCuanticaBasica as T
import unittest
import math



# Posicion y transicion
def test1():
    assert [0.05263157894736842, 0.36842105263157887+0.31578947368421045j] == T.position_transition([-3-1j, -2j, 1j, 2], 2, [-3-1j, -2j, 1j, 2])

test1()

# Media y Varianza
def test2():
    assert [2.5, 0.25] == T.varianza_Valor([[1, -1j], [1j, 2]], [(2**(1 / 2))/ 2, (2j ** (1 / 2)) / 2])
test2()


# Valores propios,vetores propios,Transicion
def test3():
    print("Probabilidades de transitar al vector propio:", T.probabilidadTransitoSistema([[-1, -1j], [1j,1]], [1/2+0j,1/2+0j]))
test3()

# Sistema dinamico
def test3():
    matrix1 = [[0,1/math.sqrt(2),1/math.sqrt(2),0], [1j/math.sqrt(2), 0, 0, 1/math.sqrt(2)], [1/math.sqrt(2), 0 , 0, 1j/math.sqrt(2)], [0,1/math.sqrt(2),-1/math.sqrt(2),0]]
    uns = [matrix1, matrix1, matrix1]
    vect = [1, 0, 0, 0]
    print("Dinamica",T.dynamic(uns,vect))
test3()