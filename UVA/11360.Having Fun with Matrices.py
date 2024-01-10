li_a=[]
get_size=0

def row(a,b):
    for i in range(get_size):
        li_a[a][i],li_a[b][i]=li_a[b][i],li_a[a][i]
def col(a,b):
    for i in range(get_size):
        li_a[i][a],li_a[i][b]=li_a[i][b],li_a[i][a]
def inc():
    for i in range(get_size):
        for j in range(get_size):
            li_a[i][j]+=1
            if li_a[i][j]==10:
                li_a[i][j]=0
def dec():
    for i in range(get_size):
        for j in range(get_size):
            li_a[i][j]-=1
            if li_a[i][j]==-1:
                li_a[i][j]=9
def transpose():
    for i in range(len(li_a)):
        for j in range(0, i):
            li_a[i][j], li_a[j][i] = li_a[j][i], li_a[i][j]
def way():
    global get_size
    get_size=int(input())
    for i in range(get_size):
        li_a.append(input())
    for i in range(get_size):
        li_a[i]=list(li_a[i])
    for i in range(get_size):
        for j in range(get_size):
            li_a[i][j]=int(li_a[i][j])

get_input=int(input())
count=1
ans=""""""
for j in range(get_input):
    way()
    get_num=int(input())
    for i in range(get_num):
        get_chose=input()
        chose=get_chose.split(" ")
        if len(chose)==1:
            if chose[0]=="transpose":
                transpose()
            elif chose[0]=="inc":
                inc()
            elif chose[0]=="dec":
                dec()
        elif len(chose)==3:
            if chose[0]=="row":
                row(int(chose[1])-1,int(chose[2])-1)
            elif chose[0]=="col":
                col(int(chose[1])-1,int(chose[2])-1)
    ans += f"case #{count}\n"
    for i in range(len(li_a)):
        ans += f"{li_a[i]}\n"
    count += 1
    li_a = []
print(ans)
