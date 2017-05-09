'''
def fact(n):
	if n == 1:
		return 1
	return n*fact(n-1)

print(fact(5))

print(fact(15))


def fact(n):
	return fact_iter(n,1)

def fact_iter(num,product):
	if num==1:
		return product
	return fact_iter(num-1,num*product)

print(fact(100))

'''

'''
#---after school practice
i = 0
def move(n,a,b,c):
	global i
	if n==1:
		print(a, '---->',c)
		i = i + 1
		return
	else:
		i=i+1
		move(n-1,a,c,b)     #首先把钱n-1从a移动到b
		print(a,'---->',c)  #把n从a移动到c
		move(n-1,b,a,c)     #再把n-1从b移动到c
n = int(input("Pls Input The Levels of Hanoi Tower:"))
print(move(n,'A','B','C'))
print('Total moved %d' % i)
'''
'''
L =[]
n = 1
while n<=99:
	L.append(n)
	n=n+2
print(L)
'''

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[-1])
print(L[-2:])
print(L[-2:-1])

S= list(range(100))
print(S[:10])
print(S[-10:])
print(S[0:10:2])
print(S[10:90:5])
s = 'ABCDEFGHIJKLMN'
print(s[:3])
print(s[::2])