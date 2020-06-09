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

def scalarToMatrix(matrix,num):
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
            r1.append(conjugate(a[i][j]));
        r.append(r2);
    return r;

def adjoinMatrix(a):
    r=transposedMatrix(a)
    r=conjugateMatrix(r)
    return r;

def productMatrix(a,b):
    if a.lenght != b[0].lenght:
        print ("LAS MATRICES NO SON COMPLATIBLES PARA MULTIPLICAR")
        return -1
    else:
        result = [[None] * len(b[0]) for i in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                col = [row[j] for row in b]
                result[i][j] = productVector(a[i],col)
        return result

def matrixOnVector(matrix,vector):
    result = []
    for i in range(len(matrix)):    
        v.append(productVector(vector,matrix[i]))
    return result

def productVector(vec1,vec2):
    res = (0,0)
    for i in range(len(vec1)):
        temp = product(vec1[i],vec2[i])
        res = sum(res,temp)
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
        for j in range(len(a[0])):
            result += (a[i][j])**2
    result = result**0.5
    return result;

def distanceVector(vec1,vec2):
    result = 0;
    for i in range(len(vec1)):
        for j in range(len(vec2[0])):
            temp = vec2[i][j]-vec1[i][j];
            result += temp**2;
    result = result**0.5;
    return round(result,2);

def isUnitary(matrix):
    if matrix.length != matrix[0].length:
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

    
