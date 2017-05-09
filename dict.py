d = {'Alice':95,'Beta':88,'Candy':59}
print(d['Alice'])

d['Alice'] = 77
print(d['Alice'])
print('Jack' in d)

print(d.get('Jack', 'NOTIN'))
d.pop('Alice')
print(d)

#set practice
s =set([1,2,3,4])
print (s)
s.add(5)
print(s)

s.remove(3)
print(s)

s1= set([1,2,3,4])
s2= set([2,3,4,5])
print(s1&s2)
print(s1|s2)

l = ['c','b','a']
print(l.sort())

a = 'abc'
b = a.replace('a','A')
print (a)
print (b)