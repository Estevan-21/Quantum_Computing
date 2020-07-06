from ObservablesYMedidas import ObservablesYMedidas as o
from Library import Library as l
from DinamycAndProbabilisticSystems import DinamycAndProbabilisticSystems as d

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

# Excercise 4.3.2
def test_transicion_probability():
    v1 = [[1, 0], [0, 0]]
    v2 = [[0, 0], [1, 0]]
    sx = [[0, 1], [1, 0]]
    sy = [[0, -1j], [1j, 0]]
    sz = [[1, 0], [0, -1]]
    print("\n-----4.3.2-----------")
    print("Probabilidad de [1, 0], [0, 0] pasar a [0, 1], [1, 0]", o.probability(v1, v2, sx, 1))
    print("Probabilidad de [1, 0], [0, 0] pasar a [0, -1], [1, 0]", o.probability(v1, v2, sx, 2))
    print("Probabilidad de [0, 0], [1, 0] pasar a [0, 1], [1, 0]",o.probability(v1, v2, sx, 3))
    print("Probabilidad de [0, 0], [1, 0] pasar a [0, -1], [1, 0]",o.probability(v1, v2, sx, 4))

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