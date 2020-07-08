from TeoriaCuanticaBasica import TeoriaCuanticaBasica as T
import unittest



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
    assert([0,0,0,0.16666666666666666,0.16666666666666666,0.3333333333333333,0.16666666666666666,0.16666666666666666] ==
                T.dynamic([   [0, 0, 0, 0, 0, 0, 0, 0],
                              [0.5, 0, 0, 0, 0, 0, 0, 0],
                              [0.5, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0.3333333333333333, 0, 1, 0, 0, 0, 0],
                              [0, 0.3333333333333333, 0, 0, 1, 0, 0, 0],
                              [0, 0.3333333333333333, 0.3333333333333333, 0, 0, 1, 0, 0],
                              [0, 0, 0.3333333333333333, 0, 0, 0, 1, 0],
                              [0, 0, 0.3333333333333333, 0, 0, 0, 0, 1]],
                              [ 1, 0, 0, 0, 0, 0, 0, 0], 2))
test3()