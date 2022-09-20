



vector1 = [6,5,4]

vector2 = [1,2,3]

# matrix optellen, hoe zat dat ookalweer?
# matrixen moeten even groot zijn
# eenheden van corresponderende plekken worden bij elkaar opgetelt

#vectoren optellen:
vector3 = [vector1[_] + vector2[_] for _ in range(len(vector1))]
print(vector3)


matrix1 = [[6,5,4],[3,2,1]]

matrix2 = [[1,2,3],[4,5,6]]

matrix3 = [[matrix1[R][C] + matrix2[R][C] for C in range(len(matrix1[0]))]for R in range(len(matrix1))]
print(matrix3)