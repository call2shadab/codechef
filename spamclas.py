t = int(input())
while t:
    wt = []
    b = []
    n, minx, maxx = map(int, input().split())
    for i in range(n):
        temp = list(map(int, input().split()))
        wt.append(temp[0]%2)
        b.append(temp[1]%2)
        sp, nsp = 0,0

    print (wt, b)

    for i in range(minx,maxx+1):
        l = i%2
        for j in range(n):
            if l==0 and wt[j]==0 and b[j]==0:
                l = 0
            elif l==0 and wt[j]==0 and b[j]==1:
                l = 1
            elif l==1 and wt[j]==1 and b[j]==1:
                l = 0
            elif l==1 and wt[j]==1 and b[j]==0:
                l = 1
            elif ((l==1 and wt[j]==0) or (l==0 and wt[j]==1)) and b[j]==0:
                l = 0
            elif ((l==1 and wt[j]==0) or (l==0 and wt[j]==1)) and b[j]==1:
                l = 1
        if l==0:
            nsp += 1
        else:
            sp += 1

    print (nsp, sp)