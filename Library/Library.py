import numpy as np
import math

""" ---------------------------- LAB 01 --------------------------------"""
def sum(a,b):
    return a+b

def rest(a,b):
    return a-b


def product(a,b):
    return a*b

def division(a,b):
    return a/b

def module(a):
    return abs(a)

def conjugate(a):
    return a.conjugate()

def norm(a):
    return (a.real**2 + a.imag**2)

def phase(a):
    rad = math.atan(a.imag/a.real)
    return round(math.degrees(rad),2)

def cartesianToPolar(a):
    mod = module(a)
    ph = phase(a)
    r = [round(mod, 2), round(ph, 2)]
    return r

def polarToCartesian(a):
    x = (a[0] * math.cos(math.radians(a[1])) * 1000) / (1000)
    ang = ((1000 * a[0] * math.sin(math.radians(a[1]))) / 1000)
    r = [round(x, 2), round(ang, 2)]
    return r;
    
""" ---------------------------- LAB 02 --------------------------------"""

def sumVector(a,b):    
    r=[];
    for i in range(len(a)):
        r.append(sum(a[i],b[i]))
    return r;

def inverse(a):
    r=complex(a.real*-1, a.imag*-1);
    return r;

def inverseVector(a):
    r=[];
    for i in range(len(a)):
        r.append(inverse(a[i]));
    return r;

def scalarMultVector(vec,num):
    r=[];
    for i in range(len(vec)):
        r.append(product(vec[i],num))
    return r

def sumMatrix(a,b):
    r=[];
    for i in range(len(a)):
        r2=[];
        for j in range(len(a)):
            r2.append(sum(a[i][j],b[i][j]));
        r.append(r2);
    return r;

def inverseMatrix(a):
    r=[]
    for i in range(len(a)):
        r.append(inverseVector(a[i]))
    return r

def scalarToMatrix(num,matrix):
    r=[]
    for col in range(0,len(matrix)):
        v=[]
        for row in range(0,len(matrix[0])):
            v.append(product(matrix[col][row],num))
        r.append(v)
    return r

def transposedMatrix(a):
    r=[];
    for i in range(len(a[0])):
        col = [T[i] for T in a]
        r.append(col)
    return r;

def conjugateMatrix(a):
    r=[];
    for i in range(len(a)):
        r2=[];
        for j in range(len(a[0])):
            r2.append(conjugate(a[i][j]));
        r.append(r2);
    return r;

def adjoinMatrix(a):
    r=transposedMatrix(a)
    r=conjugateMatrix(r)
    return r;

def productMatrix(a,b):
    if len(a) != len(b[0]):
        print ("LAS MATRICES NO SON COMPLATIBLES PARA MULTIPLICAR")
        return -1
    else:
        result = [[None] * len(b[0]) for i in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                col = [row[j] for row in b]
                result[i][j] = productVector(a[i],col)
        return result

def matriz_Transpuesta(matriz1):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    matrizTranspuesta = [[[0,0] for j in range(filas)]for i in range(columnas)]
    for i in range(columnas):
        for j in range(filas):
            matrizTranspuesta[i][j] = matriz1[j][i]
    return matrizTranspuesta

def productRealMatrix(a,b):
    if len(a) != len(b[0]):
        print ("LAS MATRICES NO SON COMPLATIBLES PARA MULTIPLICAR")
        return -1
    else:
        result = [[None] * len(b[0]) for i in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                col = [row[j] for row in b]
                result[i][j] = productVectorReal(a[i],col)
        return result

def matrixOnVector(matrix,vector):
    result = []
    for i in range(len(matrix)):    
        result.append(productVector(vector,matrix[i]))
    return result

def matrixOnVectorReal(matrix,vector):
    result = []
    for i in range(len(matrix)):
        result.append(productVectorReal(vector,matrix[i]))
    return result

def productVector(vec1,vec2):
    res = (0+0j)
    for i in range(len(vec1)):
        temp = product(vec1[i],vec2[i])
        res = sum(res,temp)
    return res

def productVectorReal(vec1,vec2):
    res = 0
    for i in range(len(vec1)):
        temp = vec1[i]*vec2[i]
        res += temp
    return res

def internalProduct(vec1,vec2):
    r = [0,0]
    for i in range(len(vec1)):
        c = conjugate(vec1[0]);
        s = product(c,vec2[i]);
        r = sum(r,s)
    return r;

def normVector(a):
    result = 0;
    for i in range(len(a)):
        result += a[i].real **2
        result += a[i].imag **2
    result = result**0.5
    return round(result,2)

def distanceVector(vec1,vec2):
    result = 0
    for i in range(len(vec1)):
            temp = vec2[i].real-vec1[i].real
            temp2 = vec2[i].imag-vec1[i].imag
            result += temp**2
            result += temp2**2
    result = result**0.5
    return result

def isUnitary(matrix):
    if len(matrix) != len(matrix[0]):
        print("Matriz no cuadrada")
        return -1
    else:
        mult = productMatrix(matrix, adjoinMatrix(matrix))
        return matrix == productMatrix(matrix, mult)

def isHermitian(matrix):
    h = adjoinMatrix(matrix);
    if h == matrix:
        return True;
    return False;

def tensorProduct(matrix1,matrix2):
    matrix = []
    for i in range(len(matrix1)):
        temp = [[]] *len(matrix2)
        for j in range(len(matrix1[i])):
            matrix3 = scalarToMatrix(matrix1[i][j],matrix2)
            for k in range(len(matrix2)):                
                temp[k] = temp[k] + matrix3[k]
        for k in range(len(matrix2)):
            matrix.append(temp[k])
    return matrix


def matrixOnVec(matrix1,vector1):
    cont = 1
    matrix = [[[0,0] for j in range(1)] for i in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(vector1[0])):
            for k in range(len(matrix1[0])):
                matrix[i][j][0] = matrix[i][j][0] + (matrix1[i][k][0] * vector1[k][j] - matrix1[i][k][1]*vector1[k][j+cont])
                matrix[i][j][1] = matrix[i][j][1] + (matrix1[i][k][1] * vector1[k][j] + matrix1[i][k][0]*vector1[k][j+cont])
            break
    return(matrix)

def Multicomplejos(a,b):
    return((a[0]*b[0] - a[1]*b[1]) , (a[1]*b[0] + a[0]*b[1]))

def sumComplejos(a,b):
    return (a[0]+b[0], a[1]+b[1])

def matrix_conjugate(matrix,value):
    if value == 1:
        matriz_Conjugada = [[[0,0] for j in range(len(matrix))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                    matriz_Conjugada[i][j][0] = matrix[i][j][0]
                    matriz_Conjugada[i][j][1] = matrix[i][j][1] * -1
        return matriz_Conjugada
    else:
        vectorEsca = [[[0,0] for j in range(1)] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(1):
                vectorEsca[i][j][0] = matrix[i][0]
                vectorEsca[i][j][1] = matrix[i][1] * -1
        return vectorEsca
    
def internal_product(v1,v2):
    cont = [0,0]
    lista = []
    v22 = [[(v2[j][0],v2[j][1]) for j in range(len(v2))] for i in range(1)]
    for i in range(len(v1)):
        for j in range(len(v1)):
            primera = Multicomplejos(v1[j][i],v2[j])
            lista.append(primera)
        break
    for i in range(len(lista)):
        cont = sumComplejos(cont,lista[i])
    return cont

def makevect(v1,x):
    cont = 0
    vector = [[0,0] for i in range(x)]
    for i in range(len(vector)):
        if cont <= 2:
            cont += 1
            for j in range(len(vector)):
                if cont <= 2:
                    vector[j][i] = v1[j][0][i]
    return vector

def conjugate_matrix(matriz1,valor):
    if valor == 1:
        matriz_Conjugada = [[[0,0] for j in range(len(matriz1))] for i in range(len(matriz1))]
        for i in range(len(matriz1)):
            for j in range(len(matriz1)):
                    matriz_Conjugada[i][j][0] = matriz1[i][j][0]
                    matriz_Conjugada[i][j][1] = matriz1[i][j][1] * -1
        return matriz_Conjugada
    else:
        vectorEsca = [[[0,0] for j in range(1)] for i in range(len(matriz1))]
        for i in range(len(matriz1)):
            for j in range(1):
                vectorEsca[i][j][0] = matriz1[i][0]
                vectorEsca[i][j][1] = matriz1[i][1] * -1
        return vectorEsca

def matriz_Producto(m1,m2):
    matrizProducto = [[[0,0] for j in range(len(m1))] for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            for k in range(len(m1[0])):
                matrizProducto[i][j][0] = matrizProducto[i][j][0] + (m1[i][k][0] * m2[k][j][0] - m1[i][k][1]*m2[k][j][1])
                matrizProducto[i][j][1] = matrizProducto[i][j][1] + (m1[i][k][1] * m2[k][j][0] + m1[i][k][0]*m2[k][j][1])
    return matrizProducto