from itertools import combinations
ans = []
for _ in range(int(input())):
    goal = int(input())
    e = input()
    l = [int(x) for x in input().split(' ')]
    con = 'NO'
    if goal == 0:
        con = "YES"
    for i in range(1,len(l)+1):
        for x in list(combinations(l,i)):
            if sum(x) == goal:
                con = "YES"
            if con == 'Yes':
                break
    ans.append(con)
[print(x)for x in ans]