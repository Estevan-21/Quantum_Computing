import numpy as np
from Library import Library as l
from TeoriaCuanticaBasica import TeoriaCuanticaBasica as T

def transition_amplitude(v1,v2):
    return l.internalProduct(v1,v2)


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


def probability(state_vector1, state_vector2, observable, position):
    v1 = observable[position]
    normalized_observable = T.normalizarVector(v1)
    #e1
    normalized_state1 = T.normalizarVector(state_vector1)
    ampl1 = transition_amplitude(normalized_state1, normalized_observable)
    # e2
    normalized_state2 = T.normalizarVector(state_vector2)
    ampl2 = transition_amplitude(normalized_state2, normalized_observable)
    return l.sum(ampl1,ampl2)




def unitary_matrix(matrix1,matrix2):
    if (l.isUnitary(matrix1) and l.isUnitary(matrix2)):
        if (l.isUnitary(l.productMatrix(matrix1, matrix2))):
            return True
    return False

