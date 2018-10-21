i =raw_input().split()
n = int(i[0])
m = float(i[1])
if n>m:
	print ("%.2f"%m)
elif n<m and n%5==0:
	print ("%.2f"%(m-n-0.5))
else:
	print ("%.2f"%m)