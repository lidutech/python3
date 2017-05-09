names = ['Apple', 'Google', 'Microsoft']
for name in names:
	print (name)

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum = sum + x
print (sum)

#list(range(5))
#计算1+2+3...+100
sum = 0 
for x in range(101):
	sum = sum + x

print (sum)
#计算100以内的奇数之和
sum = 0 
n = 99
while n>0:
	sum =sum +n
	n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
	print('Hello, %s' % name)


n = 0
while n<= 100:
	n = n +1
	if n % 2 == 0:
		continue
	print(n)
	

print('END')