# Dit programma maakt een willekeurige matrix van formaat x (matrixRows) bij y (matrixCollums)
# Met x = 1,2,3 of 4 en y = 1,2,3 of 4
# De waardes in de elementen worden maximaal 9 en minimaal -9
# En de waardes zijn gehele getallen (int)
# Uiteindelijk krijgen we 1 lijst met daarin x maal y elementen verdeeld over x lijsten

# Tussentijdse notitie: er wordt nu een lijst gemaakt van willekeurige lengte met willekeurige elementen, 
# nu dus nog opdelen in lijstjes met de lengte van het aantal kolommen


import random as randrange
import random as ra
import random


matrixRows = ra.randint(1,4)
matrixCollums = ra.randint(1,4)
matrixRandomElements = ra.randint(-9,9)



randomMatrix = []


def createTheRandomMatrix (matrixRows,matrixCollums):
    for rows in range(matrixRows):
        for collums in range(matrixCollums):
            randomMatrix.append(ra.randint(-9,9))
    return randomMatrix

print(createTheRandomMatrix (matrixRows,matrixCollums))




# low = -9
# high = 9
# in_r = random.randint(-9,9)
# col1 = random.randint(1,4)
# kol1 = random.randint(1,4)



# Rij1 = [random.choices(range(low,high), k=col1) for _ in range(kol1)]
# print(Rij1)
