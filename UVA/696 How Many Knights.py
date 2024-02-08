# OOOOOO row = 1 | column = 1

# OOXXOO row = 2 | column = 2
# OOXXOO

# OXOXOX row >= 3 | column >=3
# XOXOXO
# OXOXOX
ans = []
while True:
    get = input()
    if get == '0 0':
        break
    r,c = map(int,get.split(' '))
    count = 0
    if r == 1 or c == 1:
        count += r*c
    elif r == 2:
        if c%4>=2:
            count += 4
        elif c%4==1:
            count+=2
        count += 4*(c//4)
    elif c == 2:
        if r%4>=2:
            count += 4
        elif r%4==1:
            count+=2
        count += 4*(r//4)
    elif r>=3 and c>=3:
        if r%2 == 1:
            count += (c+1)//2
        count += r//2*c
    ans.append(f"{count} knights may be placed on a {r} row {c} column board.")
[print(x)for x in ans]