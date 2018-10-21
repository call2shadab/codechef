t = int(input())
while t:
    a, b, c = map(int, input().split())
    l = bin(a)[2:].count('1')
    r = bin(b)[2:].count('1')
    cnt = 0
    for i in range(0,int(c/2)+1):
        print ("I and C-I: ",i,c-i)
        if bin(i)[2:].count('1') == l and bin(c-i)[2:].count('1') == r:
            cnt+=1
        print ("C-I and I: ",c-i,i)
        if bin(c-i)[2:].count('1') == l and bin(i)[2:].count('1') == r:
            cnt+=1
    t = t-1
    if c%2==0:
        print (cnt-1)
    else:
        print (cnt)