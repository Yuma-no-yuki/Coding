ans = []
while True:
    get = input()
    if get == '0 0':
        break
    n1,n2 = map(int,get.split(' '))
    l = []
    def search(i,j):
        if i-1>=0 and l[i-1][j] == "@":
            l[i - 1][j] = '*'
            search(i-1,j)
        if i+1<=n1-1 and l[i+1][j] == "@":
            l[i + 1][j] = '*'
            search(i+1,j)
        if j-1>=0 and l[i][j-1] == "@":
            l[i][j-1] = '*'
            search(i,j-1)
        if j+1 <=n2-1 and l[i][j+1] == "@":
            l[i][j+1] = '*'
            search(i,j+1)
        if i-1>=0 and j-1>= 0 and l[i-1][j-1] == "@":
            l[i - 1][j-1] = '*'
            search(i-1,j-1)
        if i-1>=0 and j+1 <=n2-1 and l[i-1][j+1] == "@":
            l[i - 1][j+1] = '*'
            search(i-1,j+1)
        if i+1<=n1-1 and j+1<=n2-1 and l[i+1][j+1] == "@":
            l[i + 1][j+1] = '*'
            search(i+1,j+1)
        if i+1<=n1-1 and j-1>=0 and l[i+1][j-1] == "@":
            l[i + 1][j-1] = '*'
            search(i+1,j-1)
    for _ in range(n1):
        l.append(list(input()))
    count = 0
    for i in range(n1):
        for j in range(n2):
            if l[i][j]=='@':
                count+=1
                search(i,j)
    ans.append(count)
[print(x)for x in ans]