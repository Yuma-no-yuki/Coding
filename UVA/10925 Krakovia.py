ans = []
count = 0
while True:
    n1,n2 = map(int,input().split(' '))
    if n1==0 and n2==0:
        break
    count += 1
    s = ''
    for i in range(n1):
        s+=input()
        if i == n1-1:
            break
        s+='+'
    ans.append(f'Bill #{count} costs {eval(s)}: each friend should pay {int(eval(f"{eval(s)}//{n2}"))}')
    ans.append('')
[print(x)for x in ans]