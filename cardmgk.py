t = int(input())
while t>0:
    n = int(input())
    a = map(int, input().split())
    sor = []
    for i in a:
        sor.append(i)
    sor.sort()
    i = 0
    while a[i]<a[i+1]:
        i+=1
    for j in range(i+1):
        item = a[0]
        a.remove(item)
        a.append(item)
    if a==sor:
        print ('yes')
    else:
        print ('NO')
    t = t-1
        

