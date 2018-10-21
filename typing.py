t = int(input())
while t>0:
    n = int(input())
    wordstr = []
    for i in range(n):
        wordstr.append(input())
    lh = ['d','f']
    rh = ['j','k']
    processed = {}
    res = []
    for word in wordstr:
        if word in processed:
            res.append(processed[word]/2.0)
            continue
        time = 2
        if word[0] in lh:
            flag = 0
        else:
            flag = 1
        for j in range(1,len(word)):
            if flag == 0 and word[j] in lh:
                time = time+4
                flag = 0
            elif flag == 0 and word[j] in rh:
                time = time+2
                flag = 1
            elif flag == 1 and word[j] in lh:
                time = time+2
                flag = 0
            elif flag == 1 and word[j] in rh:
                time = time+4
                flag = 1
        res.append(time)
        processed[word]=time
    print (int(sum(res)))
    t = t-1