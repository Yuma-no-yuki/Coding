ans=[]
while True:
    get_num=int(input())
    if get_num==0:
        break
    def GCD(i, j):
        if (j == 0):
            return i
        else:
            return GCD(j,i%j)
    G=0
    for i in range(get_num):
        for j in range(i+1,get_num):
            G+=GCD(i+1,j+1)
    ans.append(G)
for i in ans:
    print(i)