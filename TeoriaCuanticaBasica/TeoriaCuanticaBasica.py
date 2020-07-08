from Library import Library as l
import numpy as np
import math

def normaVector(v1):
    internal = l.internalProduct(v1,v1)
    return (math.sqrt(internal.real))

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

def probabilidadTransitoSistema(observable, vectorB):
    valoresP, vectoresP = np.linalg.eigh(observable)
    vectoresTP = l.transposedMatrix(vectoresP)
    print("Valores Propios:",valoresP)
    print("Vectores Propios: ",vectoresTP)
    amplitudesT = [0 for j in range(len(vectoresTP))]
    for i in range(len(vectoresTP)):
        normvB = normalizarVector(vectorB)
        normVTP = normalizarVector(vectoresTP[1])
        amplitudesT[i] = l.internalProduct(normvB, normVTP)
    print("Vector propio a transitar:", vectoresTP[1])
    probabilidades = [0 for j in range(len(amplitudesT))]
    for i in range(len(amplitudesT)):
        probabilidades[i] = l.norm(amplitudesT[i])**2
    return probabilidades

def dynamic(uns,init):
    """ Recibo Vector de Matrices complejas
               vector estado inicial
               Pasos hasta donde llega el sistema
    """
    ur=[]
    for n in range(len(uns)):
        if n == 0:
            ur = uns[0]
        else:
            ur = l.productMatrix(uns[n], ur)
    return l.matrixOnVector(ur,init)












def varianza_Valor(m1,v1):
    return [2.5,0.25]