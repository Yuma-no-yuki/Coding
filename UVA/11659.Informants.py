# a=input()
# b=a.split()
# num_rela=int(b[1])
# num_amount=int(b[0])
num_rela=5
num_amount=4
l1=[]
l2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#1 2
l2[0][1]=1
#1 -4
l2[0][3]=-1
#2 -3
l2[1][2]=-1
#3 1
l2[2][0]=1
#3 4
l2[2][3]=1
con=[]
print(l2)
for i in range(4):
    for j in range(i+1,4):
        if l2[i][j]>0 or l2[j][i]>0 and l2[i][j]!=-1 and l2[j][i]!=-1:
            con.append([i,j])
uncon_default=[]
for i in con:
    for j in range(4):
        if l2[j][i[0]]<0 or l2[j][i[1]]<0:
            uncon_default.append([i[0],i[1]])
for i in range(len(uncon_default)):
    if con.count(uncon_default[i])>=1:
        con.remove(uncon_default[i])
for i in con:
    print(len(i))
#未完成
