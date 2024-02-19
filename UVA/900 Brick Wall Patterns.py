l = [1,1]
for i in range(2,50):
    l.append(l[i-1]+l[i-2])
ans=[]
while True:
    a = int(input())
    if a == 0:
        break
    ans.append(l[a])
[print(x)for x in ans]