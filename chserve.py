t = int(input())
while t:
	p1, p2, k = map(int,input().split())
	s = p1+p2
	temp = s%(2*k)
	if temp<k:
		print ("CHEF")
	else:
		print ("COOK")

	t-=1