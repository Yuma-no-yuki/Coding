ans = []
for _ in range(int(input())):
    num = int(input())
    s = input()
    coin = [int(x)for x in s.split(' ')]
    add = 0
    index = 0
    count = 0
    while index != num:
        if add >= coin[index]:
            add -= coin[index-1]
            count -= 1
        add += coin[index]
        count += 1
        index += 1
    ans.append(count)
[print(x)for x in ans]