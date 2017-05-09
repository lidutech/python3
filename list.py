classmates = ['Alpha', 'Beta','Cathie']
length = len(classmates)
print(length)
print (classmates[0])
print (classmates[1])
print (classmates[2])
print (classmates[-1])
#print (classmates[3])
print ('\n......Appending Doctor...... ')
classmates.append('Doctor')
print(classmates)

print('\n......Inserting Coon to Index 2.......')
classmates.insert(2,'Coon')
print (classmates)

print('\n......Poping out the last one.......')
classmates.pop()
print (classmates)

print('\n......Delete Index 2......')
classmates.pop(2)
print(classmates)

print('\n......Replace Index 0 to Alice....')
classmates[0] = 'Alice'
print(classmates)

L = ['Apple', 123, True]
print(len(L))

s= ['AAA','BBB','CCC','DDD']
q= ['TTT','XXX',s, 'ZZZ']
print (s)
print (q)
print (q[2])
print (q[2][2])

print ('======TUPLE PRACTICE======')
t = (1,2,3)
print(t)
print (t[-1])

print ('======After School Test======')
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print (L[0][0])
print (L[1][1])
print (L[2][2])