from numpy import linalg as LA
from Library import Library as l
import numpy as np
import math

def normaVector(v1):
    suma=0
    for i in range(len(v1)):
        suma+=(v1[i].real**2)+(v1[i].imag**2)
    norma=math.sqrt(suma)
    return (norma)

def normalizarVector(vk):
    vkNormalizado = []
    norma = normaVector(vk)
    for i in range(len(vk)):
        vkNormalizado.append([])
        vkNormalizado[i] = vk[i]/norma
    return vkNormalizado

def matrizIdentidad(fil,col):
    m=[]
    for i in range(fil):
        lis=[]
        m.append(lis)
        for j in range(col):
            lis.append([])
    for i in range(fil):
        for j in range(col):
            if i==j:
                m[i][j]=complex(1,0)
            else:
                m[i][j]=complex(0,0)
    return m

def valorEsperado(m1,vk):
    vNor = normalizarVector(vk)
    accion = l.matrixOnVec(m1,vNor)
    return (l.internalProduct(accion,vNor))

def varianza(m1,vk):
    valor = valorEsperado(m1,vk)
    vNor = normalizarVector(vk)
    resultado = l.scalarToMatrix(valor, matrizIdentidad(len(m1),len(m1[0])))
    resta = l.restMatrix(m1,resultado)
    restaCuadrada= l.productMatrix(resta,resta)
    return(valorEsperado(restaCuadrada,vNor))


def varianza_valor(m1, V):
    if l.isHermitian(m1):
        return[valorEsperado(m1,V), varianza(m1,V)]
    else:
        print('El observable no es una matriz hermitiana')


def position_transition(V, p, V2):
    raiz = 0
    for i in V:
        raiz += (i.real ** 2) + (i.imag ** 2)
    prob = ((V[p].real ** 2) + (V[p].imag ** 2)) / raiz
    total = complex (0, 0)
    norm1 = 0
    norm2 = 0
    V1 = V
    for z, y in zip(V1, V2):
        total = l.sum(total, l.product(z, y))
        norm1 += (z.real ** 2) + (z.imag ** 2)
        norm2 += (y.real ** 2) + (y.imag ** 2)
    norm1f = norm1 ** (1 / 2)
    norm2f = norm2 ** (1 / 2)
    deno = norm1f * norm2f
    return [prob, complex((total.real / deno), (total.imag / deno))]

def propios(X, V):
    a = [X,V]
    w, v = LA.eigh(a)
    prop = v[0]
    total = (0, 0)
    norm1 = 0
    norm2 = 0
    V1 = V
    for z, y in zip(V1, prop):
        total = l.sum(total, l.product(z, y))
        norm1 += (z.real ** 2) + (z.imag ** 2)
        norm2 += (y.real ** 2) + (y.imag ** 2)

    norm1f = norm1 ** (1 / 2)
    norm2f = norm2 ** (1 / 2)
    deno = norm1f * norm2f
    return("Valores propios",w,"Vectores propios",v,"Probabilidad de transicion",complex(total[0]/deno, total[1]/deno))


def dynamic(X, V, n):
    Y = X
    result = [[0 for j in range(len(X))] for i in range(len(Y[0]))]
    ssum = complex(0, 0)
    for t in range(n):
        for i in range(len(X)):
            for j in range(len(Y[0])):
                for k in range(len(Y)):
                    result[i][j] = l.sum(ssum, l.product(X[i][k], Y[k][j]))
                    ssum = result[i][j]
                ssum = complex (0, 0)
        Y = result

    result2 = [[0 for j in range(len(X))] for i in range(len(Y[0]))]
    ssum2 = complex(0, 0)
    X = result
    Y = V
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] = l.sum(ssum2, l.product(X[i][k], Y[k][j]))
                ssum2 = result[i][j]
            ssum2 = complex(0, 0)
    return result2












def varianza_Valor(m1,v1):
    return [2.5,0.25]