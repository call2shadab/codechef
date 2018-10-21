for i in xrange(input()):
	nin = input()
	arr = map(int,raw_input().split())
	d = 1
	k = 1+arr[0]
	pktt = 1
	v = arr[0]
	while k<nin:
		tempoor = v + sum(arr[pktt:k])
		pktt = k
		v = tempoor
		if k+tempoor>=nin:
			d+=1
			break
		else:
			k=k+tempoor
		d+=1

	print (d)