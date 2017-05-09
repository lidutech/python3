def normalize(name):
	return name.capitalize()

L1 = ['Lise','Jim','Mickey']
L2 = list(map(normalize,L1))
print (L2)
