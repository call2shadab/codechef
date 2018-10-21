from random import randint
s = [randint(1,100) for i in range(100000000)]
res = []
temp = []
for i in range(len(s)):
	for j in range(i+1,len(s)):
		temp.append(s[i])
		temp.append(s[j])
		res.append(temp)
		temp = []


print res