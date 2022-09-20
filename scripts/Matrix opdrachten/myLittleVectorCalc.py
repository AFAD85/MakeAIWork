#!/usr/bin/env python
# Dit programma rekent de som uit van twee vectoren (a en b) en slaat deze op in lijst (c)
# de vectoren zijn lijsten
# het programma neemt dus de corresponderende onderdelen van de lijsten (bv:1,1 en 2,1) 
# en telt deze bij elkaar op en maakt hiervan de corresponderende cel in de nieuwe lijst (3,1)

a = [0,3,1]
b = [1,4,7]
def sumVector (a,b):
    if len(a)==len(b):
        c = [a[0]+b[0],a[1]+b[1],a[2]+b[2]]
        return c
    else:
        print("Rustaaaagh")



print (sumVector(a,b))

print (a)
print (a,b)

print (bin(231))
