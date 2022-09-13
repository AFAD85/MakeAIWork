Opdracht bij les 12 september Neural networks - 

Import math is toegestaan (numpy niet)


NN maken om kruisjes en rondjes te herkennen uit een 3x3 plaatje (zwart wit) die wordt dus in een 3,3 matrix gezet.

De uitkomst wordt uitgedrukt in X of O (binair dus)

We gebruiken Softmax (dus waarschijnlijkheid dat het om een X of O gaat) als activatie functie
De waarde die uit de softmax functie komt interpreteren we als de kans dat de output bij de X of O hoort

Back propagation zonder gradient descent toepassen

3? klassen namelijk Node, Link, X? en O?
of klasse node met x of o


Node : 9 nodes die elk een punt van het plaatje weergeven 
1,2,3
4,5,6
7,8,9
	heeft een waarde 1 of 0
	heeft een gewicht (softmax probability)
	
per node dus een Softmax oftewel een waarschijnlijkheid dat het zijn van een 0 of 1 bijdraagt aan kruisje of rondjes

9 links van elke node naar de output dat geeft dus een (1,9) x (9,1) = (1,1) en die (1,1) geeft dus een getal waarschijnlijk tussen de 0 en 1 en die zetten we om naar X of O

Meansquared error gebruiken om te kijken hoe goed t werkt


symbolVecs = {'O': (1,0), 'X': (0,1)}
symbolChars = dict ((value, key) for key, value in symbolVecs.items ())

# Define datasets (training set should normally be much larger than test set for best results)

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






class Node ():
	def __init__(self)
		self.value = None
		self.inputlinks = []
	

class Link ()
	def __init__(self, inputNode, outputNode)
		self.weight= 
		?self.inputNode=
		?self.outputNode=
		
		
self.weight instellen op 1 (want zegt Frank)


z = x of o


Algemene functies:
def softmax
# zet output om in probabilities
# voor natuurlijke exponent gebruiken we de math library math.exp(hiero de output waarde voor het goede plekje in de functie)

	softmax = math.exp(waarde van de X of O node(degene waarop je de kans berekent))/math.exp(waarde van de X of O node) + math.exp(waarde van de X of O node)
	

def loss
# functie voor de meansquared error loss voor een bepaalde set gewichten om te vergelijken met andere instellingen van de gewichten
# verschil met output van NN tegenover de juiste output



