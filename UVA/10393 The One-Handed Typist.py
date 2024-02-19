dic = {
    1:'qaz ',
    2:'wsx' ,
    3:'edc',
    4:'rfvtgb',
    5:' ',
    6:' ',
    7:'yhnujm',
    8:'ik',
    9:'ol',
    10:'p;/'
}
ans = []
try:
    while True:
        get = list(input().split(' '))
        i1,i2 = int(get[0]),int(get[1])
        l1 = [int(x)for x in input().split(' ')]
        l2 = []
        s=""
        for x in l1:
            s+=dic[x]
        [l2.append(input())for x in range(i2)]
        M = 0
        for x in range(len(l2)):
            for i in l2[x]:
                if i in s:
                    l2[x]=""
                    continue
            if M< len(l2[x]):
                M = len(l2[x])
        count = 0
        out = []
        if M == 0:
            ans.append(0)
        else:
            for x in l2:
                if len(x) == M:
                    if x in out:
                        continue
                    count +=1
                    out.append(x)
            ans.append(count)
            [ans.append(x)for x in out]
except EOFError:
    pass
[print(x)for x in ans]
