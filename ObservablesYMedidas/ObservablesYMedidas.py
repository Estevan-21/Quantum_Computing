import numpy as np
from Library import Library as l

def transition_amplitude(v1,v2):
    v1,v2 = v2,v1
    v11 = list(v1)
    v1 = l.matrix_conjugate(v1,2)
    norma = l.internal_product(v1,v11)
    norma = (norma[0]+norma[1]) ** (1/2)
    v22 = list(v2)
    x = len(v22)
    v2 = l.matrix_conjugate(v2,2)
    norma2 = l.internal_product(v2,v22)
    norma2 = (norma2[0]+norma2[1]) ** (1/2)
    v2 = l.makevect(v2,x)
    v2 = l.conjugate_matrix(v2,2)
    v1 = l.matriz_Transpuesta(v1)
    producto = l.matriz_Producto(v1,v2)
    noma_Total = norma * norma2
    for i in range(len(producto[0][0])):
        for j in range(1):
            producto[0][0][i] = round(producto[0][0][i] / noma_Total,2)
    return producto


def expected_values(matrix, param):
    value = []
    values, vectors = np.linalg.eig(matrix)
    vector = [[] for i in range(len(vectors))]
    for i in range(len(values)):
        value.append(round(values[i], 1))
    for i in range(len(vectors)):
        for j in range(len(vectors)):
            vector[i].append(vectors[i][j])
    if param == 1:
        return value
    else:
        return vector


def probability(state1_vector, state2_vector, matrix, value):
    if matrix == [[0, -1j], [1j, 0]]:
        vector1 = [[0, 1], [1, 0]]
        vector2 = [[0, -1], [1, 0]]
    else:
        vectores_propios = expected_values(matrix, 2)
        vector1 = [[0, 0] for i in range(len(vectores_propios[0]))]
        vector2 = [[0, 0] for i in range(len(vectores_propios[0]))]
        if vectores_propios[0][0] != complex:
            vector1[0][0] = vectores_propios[0][0]
        else:
            vector1[0][1] = vectores_propios[0][0]
        if vectores_propios[0][1] != complex:
            vector1[1][0] = vectores_propios[0][1]
        else:
            vector1[1][1] = vectores_propios[0][1]
        # 2
        if vectores_propios[1][0] != complex:
            vector2[0][0] = vectores_propios[1][0]
        else:
            vector2[0][1] = vectores_propios[1][0]
        if vectores_propios[1][1] != complex:
            vector2[1][0] = vectores_propios[1][1]
        else:
            vector2[1][1] = vectores_propios[1][1]
    if value == 1:
        amplitud1 = transition_amplitude(state1_vector, vector1)
        return amplitud1
    elif value == 2:
        amplitud2 = transition_amplitude(state1_vector, vector2)
        return amplitud2
    elif value == 3:
        amplitud3 = transition_amplitude(state2_vector, vector1)
        return amplitud3
    elif value == 4:
        amplitud4 = transition_amplitude(state2_vector, vector2)
        return amplitud4



def unitary_matrix(matrix1,matrix2):
    if (l.isUnitary(matrix1) and l.isUnitary(matrix2)):
        if (l.isUnitary(l.productMatrix(matrix1, matrix2))):
            return True
    return False

