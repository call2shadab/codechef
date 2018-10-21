from time import clock
from random import randint
s = clock()
t = int(input())
while s<1 and t:
	n = randint(0,1600)
	print ("N: ",n)
	temp = n % 26
	temp2 = int(n/26)
	if temp == 0 and n == 0:
		res = 1
		print (int(res),0,0)
	elif temp == 0 and n!=0:
		res = 2**(temp2-1)
		print (0,0,int(res))
	elif temp>0 and temp<=2:
		res = 2**temp2
		print (int(res),0,0)
	elif temp>2 and temp<=10:
		res = 2**temp2
		print (0,int(res),0)
	elif temp>10:
		res = 2**temp2
		print (0,0,int(res))
	s = clock()
	print ("Time: ",s)
	t-=1

if s>1:
	print ("Alas! Time Exceed")
elif not t:
	print ("Hurray! Success")

