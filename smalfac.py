t = int(input())
while t>0:
    n = int(input())
    s = 0
    while n>0:
        s = s+(n%10)
        n = int(n/10)
    print (s)
    t -= 1