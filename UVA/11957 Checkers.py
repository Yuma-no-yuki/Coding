ans=[]
for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        index2 = 0
        ch = []
        for x in input():
            if x == '.':
                x = 0
            elif x == 'W':
                x = 1
                W_l = [i,index2]
            else:
                x = -1
            ch.append(x)
            index2 +=1
        l.append(ch)
    W_l[0] = -(W_l[0] - n + 1)
    l = l[::-1]
    l = l[W_l[0]:]
    for i in range(n-W_l[0]):
        for j in range(n):
            if i-1>=0 and j-1>=0 and l[i-1][j-1] >= 0 and l[i][j] != -1:
                l[i][j] += l[i-1][j-1]
            if i-2>=0 and j-2>=0 and l[i-1][j-1] == -1 and l[i][j]!= -1 and l[i-2][j-2]>=0:
                l[i][j] += l[i-2][j-2]
            if i-1>=0 and j+1<=n-1 and l[i-1][j+1] >= 0 and l[i][j] != -1:
                l[i][j] += l[i-1][j+1]
            if i - 2 >= 0 and j + 2 <= n - 1 and l[i - 1][j + 1] == -1 and l[i][j] != -1 and l[i-2][j+2]>=0:
                l[i][j] += l[i - 2][j + 2]
    cal = 0
    for x in l[-1]:
        if x >0:
            cal +=x
    ans.append(f"Case {_+1}: {cal%1000007}")
[print(_)for _ in ans]
# 4
# ....
# ....
# .B..
# ..W.
# 8
# .B.B.B..
# ........
# ........
# ..B.....
# ........
# ..B.....
# .W......
# ........