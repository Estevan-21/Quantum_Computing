from ObservablesYMedidas import ObservablesYMedidas as o
from Library import Library as l
from DinamycAndProbabilisticSystems import DinamycAndProbabilisticSystems as d
import math

# Excercise 4.3.1
def test_possible_states():
    sx = [[0, 1], [1, 0]]
    sy = [[0, -1j], [1j, 0]]
    sz = [[1, 0], [0, -1]]
    print("-----4.3.1-----------")
    print('Vectores propios de Sx =', o.expected_values(sx, 2))
    print('Vectores propios de Sy =', o.expected_values(sy, 2))
    print('Vectores propios de Sz =',  o.expected_values(sz,2))

test_possible_states()
#
# Excercise 4.3.2
def test_transicion_probability():
    v1, v2 = [-0.923j, -0.382], [-0.382j, 0.923]
    vSx = [[-1, 1], [1, 1]]
    vSy = [[-1j, 1], [1j, 1]]
    vSz = [[0, 1], [1, 0]]
    print("\n-----4.3.2-----------")
    print("Probabilidad de transitar a [-1, 1], observable Sx", o.probability(v1, v2, vSx,0))
    print("Probabilidad de transitar a [1, 1], observable Sx", o.probability(v1, v2, vSx,1))
    print("Probabilidad de transitar a [-1i, 1], observable Sy",o.probability(v1, v2, vSy,0))
    print("Probabilidad de transitar a [1i, 1], observable Sy",o.probability(v1, v2, vSy,1))

test_transicion_probability()

# Excercise 4.3.2
def test_Unitarias():
    m1 = [[0, 1], [1, 0]]
    m2 = [[0.7, 0.7], [0.7, -0.7]]
    print("\n-----4.4.1-----------")
    print("Matriz 1 Unitaria: ", l.isUnitary(m1))
    print("Matriz 2 Unitaria: ", l.isUnitary(m2))
    print("Producto de Matrices Unitario: ", o.unitary_matrix(m1,m2))

test_Unitarias()

def test_probabilidad():
    m1 = [[0, 1 / (2 ** (1 / 2)), 1 / (2 ** (1 / 2)), 0],
          [1j / (2 ** (1 / 2)), 0, 0, 1j / (2 ** (1 / 2))],
          [1 / (2 ** (1 / 2)), 0, 0, 1j / (2 ** (1 / 2))],
          [0, 1 / (2 ** (1 / 2)),  -1 / (2 ** (1 / 2)), 0]]
    v = [1,0,0,0]
    print("\n-----4.4.2-----------")
    print("Vector de probabilidades resultado: ", d.systemAndDinamycsQuantum(m1,v,3))

test_probabilidad()
