'''
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
'''

#height = 1.75
#weight = 80.5
h1 = input ("请输入你的身高，单位(m):")
w1 = input ("请输入你的体重，单位(kg):")
h2 = float(h1)
w2 = float(w1)
bmi = w2/(h2*h2)
print ('您的身高是', h2, '米')
print ('您的体重是', w2, '公斤')
print ('您的BMI指数是 %.2f' % bmi)
if bmi < 18.5:
	print("--->过轻")
elif bmi >=18.5 and bmi <25:
	print ("--->正常")
elif bmi >=25 and bmi <28:
	print("--->过重")
elif bmi>=28 and bmi <32:
	print ("--->肥胖")
elif bmi>=32:
	print ("TOOOO Fat!")
