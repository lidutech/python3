import math
def move(x,y,step, angle=0):
	nx = x + step* math.cos(angle)
	ny = y - step* math.sin(angle)
	return nx,ny

x,y = move(100,100,60,math.pi/6)
print(x,y)

r = move(100,100,60,math.pi/6)
print(r)

#---After school practice

def quadratic(a,b,c):
	x1 = ((-b)+math.sqrt(b*b-4*a*c))/(2*a)
	x2 = ((-b)-math.sqrt(b*b-4*a*c))/(2*a)
	return x1,x2
print(quadratic(2,3,1))
print(quadratic(1,3,-4))

def power(x,n):
	s = 1
	while n>0:
		n = n -1
		s = s*x
	return s

print(power(5,2))
print(power(5,-1))

def enroll(name,gender,age =6, city = 'Zhongshan'):
	print('name:',name)
	print('gender:',gender)
	print('age',age)
	print('city',city)
enroll('Sarah','F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')
'''
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum

nums = [1,2,3]
print(calc((1,2,3))
#print(calc((2,3,4,5,6)))
print(calc(*nums))
'''

def person(name,age,**kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name:',name, 'age:',age,'other:',kw)

person('Jack',24,city='Beijing',addr='Chaoyang',zipcode=123456)