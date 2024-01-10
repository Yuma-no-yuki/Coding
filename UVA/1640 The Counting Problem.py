ans=[]
while True:
    k = input()
    if k=="0 0":
        break
    a,b=k.split(" ")
    c=[0,0,0,0,0,0,0,0,0,0]
    if int(a)>int(b):
        a,b=b,a
    for i in range(int(a),int(b)+1):
        t=str(i)
        for j in t:
            c[int(j)]+=1
    s=""
    s=" ".join(map(str,c))
    ans.append(s)
for i in ans:
    print(i)
#TLE

# k=input()
# a,b=k.split(" ")
# c=[0,0,0,0,0,0,0,0,0,0]
# for i in range(int(a),int(b)+1):
#     t=str(i)
#     for j in t:
#         c[int(j)]+=1
# s=""
# s=" ".join(map(str,c))
# ans.append(s)
# print(ans)


# ans=[]
# while True:
#     k = input()
#     if k=="0 0":
#         break
#     a,b=k.split(" ")
#     if int(a)>int(b):
#         a,b=b,a
#     t=''
#     for i in range(int(a),int(b)+1):
#         t+=str(i)
#     c=[t.count('0'),t.count('1'),t.count('2'),t.count('3'),t.count('4'),t.count('5'),t.count('6'),t.count('7'),t.count('8'),t.count('9')]
#     s = ""
#     s = " ".join(map(str, c))
#     t=''
#     ans.append(s)
# for i in ans:
#     print(i)

#1000~1200   9:20+10*2 2:20+10*2+1 1:20+10*2+100+201
#1000~1120   1:12+10*1+21+121
#1000~1020   1:2+10+21

#1~1000 1:100+10*10+100+1
#1~1020 1:102+10*10+100+21+10


#20=1*10+10 有幾個十位數+在十位數時出現幾次
#300=20*10+100 有幾個百位數+在百位數時出現幾次
#可推斷當需求範圍為 1~999 時 300*10+1000=4000 , 4000為 1~999 1~9出現次數