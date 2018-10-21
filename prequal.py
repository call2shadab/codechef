for t in range(input()):
	n, k = map(int,raw_input().split())
	s = map(int,raw_input().split())
	s.sort()
	s.reverse()
	temp = k-1
	f = k
	i = 1

	if s[temp+1]!=s[temp]:
		print k
	else:
		while s[k+i-1]==s[k-1]:
			i+=1
			f+=1
		print f

