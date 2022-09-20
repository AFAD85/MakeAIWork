import math as m
import numpy as n



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
input1 = trainingSet[0][0]
print ("input set 1",input1)
input2 = trainingSet[1][0]
print ("input set 2",input2)

# input = []
# set1 = trainingSet[0][0]

weightsX = [1,1,1,1,1,1,1,1,1,1]
weightsO = [1,1,1,1,1,1,1,1,1,1]

# for ts in set1:
#     for mainlist in ts:
#             input.append(mainlist)

# print(input)

# label = trainingSet[0][1]
# for ts_label in label:
#     for mainlist_ in ts_label:
#                 print ("Label ", mainlist_)
            
            
# output = []            
# for x in input:
#     for y_x in weightX:
#         print(y_x[0])
                

# for mainlist in trainingSet:
#     for sublist in mainlist[1]:
#         for row in sublist:
#             print (row)

# k = [a * b for a,b in zip(input, weightX)]
# l = [a * b for a,b in zip(input, weightO)]
# print("O ",l, ' ', "X ",k)

# blah = m.exp(somX)/(m.exp(somX)+m.exp(somO))
# print(blah)

"""

Weights maken met 9x1 matrix(tuple) vec:
def initWeights(vec):
    n = len(vec)
    weights = []
    for i in range(0,n):
        weights.append(1.0)
    return weights
"""


def sumX(weightsX,input):
	outputX = []
	n.multiply(weightsX,input1)
	print(outputX)


print ("hieroX",sumX(weightsX,input1))


def sumO(weightsO,input):



print("hiero O",sumO(weightsO,input1))



def softmax(outputs):
	expOutputs=[]
	for items in outputs:
		expOutputs.append(m.exp(items))
	sum_expOutputs = sum(expOutputs)
	softmax=[]
	for itemsexp in expOutputs:
		softmax.append(itemsexp/(sum_expOutputs))
	return(softmax)

print(softmax(sumX,sumO)) #7 is de som van X en 9 de som van O

labelX=[1,0]
labelO=[0,1]
"""
def loss_function (probs,labels):
	if len(probs)!=len(labels):
		print("NEE JOH WAT HEB JE GEDAAN??? probs en labels zijn niet even lang... man man man...")
	loss=0
	for i in range (len(probs)):
		error = (labels[i]-probs[i])
		squaredError = error**2
		loss += squaredError
	return loss

print(loss_function(softmax([9,7]),labelX))
"""

def lossFunction(probs, label):
	# if len(probs)!=len(labels):
	# print("NEE JOH WAT HEB JE GEDAAN??? probs (uitkomst softmax) en labels (bekende waarden kans x en o) zijn niet even lang... man man man...")
	loss = sum(n.subtract(probs,label)**2)
	return loss

print(lossFunction(softmax(sumX,sumO),labelX))










