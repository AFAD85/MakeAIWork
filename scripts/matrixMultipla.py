# # BEHORENDE BIJ LES VAN 5 SEPTEMBER
# # dit programma vermenigvuldigt twee gegeven matrixen van bepaalde lengte en slaat deze op als matrix3

matrix1 = [[6,5,4],[3,2,1]]

matrix2 = [[1,2],[3,4],[5,6]]

matrix3 = [[0,0],[0,0]] # append proberen te benutten om de lijst aan te vullen


if len(matrix1[0]) == len (matrix2):
    for rowIndex in range(len(matrix1)):
        for collumIndex in range(len(matrix2[0])):
            for itteraties in range(len(matrix1[0])):
                matrix3[rowIndex][collumIndex] += matrix1[rowIndex][itteraties] * matrix2[itteraties][collumIndex]
else:  
    print ("NEE JOH, dat kan helemaal niet, het aantal kolommen van de eerste matrix moet gelijk zijn aan het aantal rijen van de tweede")


print (matrix3)

