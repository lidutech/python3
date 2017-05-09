print ("Hello world")

print ('the tom','is a little','busy')


number = 1024*768
print ('1024*768=',number)

print ('I\'m \"OK\"')

print ('\\\t\\')
print (r'\\\t\\')
print ('\n')

print('''line1
...line2
...line3''')

print (10/3)
print (10//3)
print (9/3)
print (10%3)
n=123
f=456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Jim\''
s3 = r'Hello, "Bart" ' 
s4 = r'''Hello,
Lisa!'''

print (n)
print (f)
print (s1)
print (s2)
print (s3)
print (s4)

print ('包含中文的str')
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print( '\u4e2d\u6587')

print('Hello,%s' % 'world')

print ('Hi, %s, you have $%d' %('Jim', 100000000))
print ('%.4f' % 3.1415926)
print ('%.2f' % 3.1415926)
print ('Age: %s, Salary:%s, you are top 1 %%' %(25,800000))

s1 = 72
s2 = 85

r  = (s2 - s1)/s1*100
print ('Xiaoming\'GPA up %.1f %%' % r)