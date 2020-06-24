from Library import Library as l
import matplotlib.pyplot as plot
import numpy as np

"""Realiza la simulación del estado final de un sistema probabilístico después de t clicks.
    @param matrix matriz que posee el sistema
    @param vector vector de estado inicial del sistema
    @param clicks número de clicks de tiempo en los que se evaluará el sistema
    @return vector de estado final del sistema después de t clicks de tiempo
    """
def systemAndDinamycsReal(matrix, vector, clicks):
    raisedMatrix = matrix
    for i in range(clicks-1):
        raisedMatrix = l.productRealMatrix(raisedMatrix, matrix)
    result = l.matrixOnVectorReal(raisedMatrix, vector)
    return result

""" Realiza la simulación del estado final de un sistema cuántico después de t clicks.
     @param matrix matriz que posee el sistema
     @param vector vector de estado inicial del sistema
     @param clicks número de clicks de tiempo en los que se evaluará el sistema
     @return vector de estado final del sistema después de t click de tiempo
    """
def systemAndDinamycsQuantum(matrix, vector, clicks):
    raisedMatrix = matrix;
    for i in range(clicks-1):
        raisedMatrix = l.productMatrix(raisedMatrix, matrix);
    result = l.matrixOnVector(raisedMatrix, vector);
    return result

""" Realiza la simulación del experimento de las múltiples rendijas clásico probabilístico, con más de dos rendijas.
     @param matrix matriz que posee el sistema
     @param vector vector de estado inicial del sistema
     @param clicks número de clicks de tiempo en los que se evaluará el sistema
     @return vector de estado final del sistema después de t click de tiempo
    """
def classicMultipleSlits(matrix,vector,clicks):
    if len(matrix) == 0 or len(vector) == 0:
        print("The operation cannot be performed.")
    elif len(matrix[0]) != len(vector):
        print("The operation cannot be performed.")
    else:
        cont = 1
        res=vector
        while cont <= clicks:
            res = l.matrixOnVectorReal(matrix,res)
            cont += 1
    return(res)



""" Realiza el ensamblaje de dos sistemas clásicos
     @param matrix1 matriz que posee el primer sistema
     @param matrix2 matriz que posee el segundo sistema
     @param vector1 vector que posee el primer sistema
     @param vector2 vector que posee el segundo sistema
     @return matrixResult, vectorResult matrix y vector resultantes del ensamblaje de los dos sistemas
    """
def systemsAssembly(matrix1,matrix2,vector1,vector2):
    matrixResult = l.tensorProduct(matrix1,matrix2)
    vectorResult = l.tensorProduct(vector1,vector2)[0]
    return matrixResult,vectorResult



""" Realiza la simulación del experimento de las múltiples rendijas cuántico
     @param matrix matriz que posee el sistema
     @param vector vector de estado inicial del sistema
     @param clicks número de clicks de tiempo en los que se evaluará el sistema
     @return vector de estado final del sistema después de t click de tiempo
    """
def quantumMultipleSlits(matrix,vector,clicks):
    if len(matrix) == 0 or len(vector) == 0:
        print("The operation cannot be performed.")
    elif len(matrix[0]) != len(vector):
        print("The operation cannot be performed.")
    else:
        cont = 1
        res=vector
        while cont <= clicks:
            res = l.matrixOnVector(matrix,res)
            cont += 1
        for i in range(len(res)):
            res[i] = abs(res[i].real)
    return(res)


""" Realiza el gráfico de probabilidades de estados de un vector dado
    @param vector Vector resultado que se desea graficar
    """
def Graphs(vector, title):
    x = np.array([ x for x in range(len(vector))])
    y = np.array([round(vector[x]*100,2) for x in range(len(vector))])
    plot.bar( x,y , color ='b', align='center')
    plot.title('Probability of states ' + title)
    plot.show()

def Graphs2(vector):
    x = np.array([ x for x in range(len(vector))])
    y = np.array([round(vector[x][0]*100,2) for x in range(len(vector))])
    plot.bar( x,y , color ='b', align='center')
    plot.title('Probability of states')
    plot.show()

