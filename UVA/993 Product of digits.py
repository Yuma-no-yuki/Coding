ans = []
for _ in range(int(input())):
    dev = [int(x)for x in range(9,1,-1)]
    count = [0]*len(dev)
    n = int(input())
    if n == 0:
        ans.append(0)
        continue
    elif n==1:
        ans.append(1)
        continue
    else:
        x = 0
        while n != 1 and x != len(dev):
            if n%dev[x] == 0:
                n = n//dev[x]
                count[x]+=1
            else:
                x += 1
        if x == len(dev):
            ans.append(-1)
            continue
        else:
            s = ''
            for i in range(len(count)):
                s+=str(dev[i])*count[i]
            ans.append(s[::-1])
            continue
[print(x)for x in ans]