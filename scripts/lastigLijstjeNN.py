import math as m




trainingSet = (
	((
			(1,1,1),
			(1,0,1),
			(1,1,1)
	), 'O'),
	((
			(0,1,0),
			(1,0,1),
			(0,1,0)
	), 'O'),
	((
			(0,1,0),
			(1,1,1),
			(0,1,0)
	), 'X'),
	((
			(1,0,1),
			(0,1,0),
			(1,0,1)
	), 'X')
)
input = []
set1 = trainingSet[0][0]

weightX = [1,1,5,1,1,1,1,1,1]
weightO = [1, 0.1, 0.1, 0.1, 0.1, 1,1,1,1,1]

for ts in set1:
    for mainlist in ts:
            input.append(mainlist)

print(input)

label = trainingSet[0][1]
for ts_label in label:
    for mainlist_ in ts_label:
                print ("Label ", mainlist_)
            
            
output = []            
# for x in input:
#     for y_x in weightX:
#         print(y_x[0])
                

# for mainlist in trainingSet:
#     for sublist in mainlist[1]:
#         for row in sublist:
#             print (row)

k = [a * b for a,b in zip(input, weightX)]
l = [a * b for a,b in zip(input, weightO)]
print("O ",l, ' ', "X ",k)

blah = m.exp(12)/m.exp(12)+m.exp(5.3)
print(blah)