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


weightsX = np.ones(9)
weightsO = [1,1,1,1,1,1,1,1,1,1]


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


def lossFunction(probs, label):
	# if len(probs)!=len(labels):
	# print("NEE JOH WAT HEB JE GEDAAN??? probs (uitkomst softmax) en labels (bekende waarden kans x en o) zijn niet even lang... man man man...")
	loss = sum(n.subtract(probs,label)**2)
	return loss

print(lossFunction(softmax(sumX,sumO),labelX))
