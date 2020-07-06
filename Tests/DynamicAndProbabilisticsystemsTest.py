from DinamycAndProbabilisticSystems import DinamycAndProbabilisticSystems as d
import math

""" Realiza la simulación del estado final de un sistema probabilístico después de t clicks. """
matriz1 = [ [0,0,0,0,0,0,0,0,0,0,0,0,1],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,0],
            [0,0,1,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,1,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,0,0,0,0,0],
            [0,0,0,0,0,1,0,0,0,1,0,0,0],
            [0,0,0,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0]
          ]
vector1 = [10,4,1,7,2,2,11,0,3,1,0,5,2]
res = d.systemAndDinamycsReal(matriz1, vector1,25)

""" Realiza la simulación de un ensamblaje de sistemas"""
matrizA = [[0,1/6,5/6],
           [1/3,1/2,1/6],
           [2/3,1/3,0]]
matrixB = [[1/3,2/3],
           [2/3,1/3]]
vectorA = [[1,0,0]]
vectorB = [[0.8,0.1]]

matrizC, vectorC = d.systemsAssembly(matrizA,matrixB,vectorA,vectorB)
res0 = d.classicMultipleSlits(matrizC,vectorC,5)
print("Vector Result Assembled System: ", res0)
d.Graphs(res0, "Assembled System")



""" MULTIPLES RENDIJAS CLASICO"""
Matrix1 = [[0,0,0,0,0,0,0,0]
            ,[1/2,0,0,0,0,0,0,0]
            ,[1/2,0,0,0,0,0,0,0]
            ,[0,1/3,0,1,0,0,0,0]
            ,[0,1/3,0,0,1,0,0,0]
            ,[0,1/3,1/3,0,0,1,0,0]
            ,[0,0,1/3,0,0,0,1,0]
            ,[0,0,1/3,0,0,0,0,1]]
Vector1 = [1,0,0,0,0,0,0,0]
res1 = d.classicMultipleSlits(Matrix1,Vector1,2)
print("Vector Result Classic System: ", res1)
d.Graphs(res1, "Classic")

""" MULTIPLES RENDIJAS CUANTICO"""
Matrix2 = [[0, 0, 0, 0, 0, 0, 0, 0]
        , [1/math.sqrt(2), 0, 0, 0, 0, 0, 0, 0]
        , [1/math.sqrt(2), 0, 0, 0, 0, 0, 0, 0]
        , [0, (-1+1j)/math.sqrt(6), 0, 1, 0, 0, 0, 0]
        , [0, (-1-1j)/math.sqrt(6), 0, 0, 1, 0, 0, 0]
        , [0, (1-1j)/math.sqrt(6), (-1+1j)/math.sqrt(6), 0, 0,1, 0, 0]
        , [0, 0, (-1-1j)/math.sqrt(6), 0, 0, 0, 1, 0]
        , [0, 0, (1-1j)/math.sqrt(6), 0, 0, 0, 0, 1]]
Vector2 = [1, 0, 0, 0, 0, 0, 0, 0]
res2 = d.quantumMultipleSlits(Matrix2, Vector2, 2)
print("Vector Result Quantum System: ", res2)
d.Graphs(res2, "Quantum")


