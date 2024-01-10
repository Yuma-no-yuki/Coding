# ans=[]
# try:
#     while True:
#         m=input()
#         coin=[1,5,10,25,50]
#         c=[0]*7490
#         c[0]=1
#         for i in range(len(coin)):
#             for j in range(coin[i],int(m)+1):
#                 c[j]+=c[j-coin[i]]
#         ans.append(c[int(m)])
# except EOFError:
#     pass
# [print(get)for get in ans]

#DP
m=int(input())
coin=[1,5,10,25,50]
c=[0]*7490
c[0]=1
for i in range(len(coin)):
    for j in range(coin[i],int(m)+1):
        c[j]+=c[j-coin[i]]
        print(f"c[{j}]+=c[{j-coin[i]}],i={i},j={j}")
print(c[int(m)])
# TLE 窮舉法
# import itertools
# ans_out=[]
# while True:
#     a=[]
#     b=[]
#     c=[]
#     d=[]
#     t=[50,25,10,5]
#     t2=[]
#     ans_in=input()
#     if ans_in=='':
#         break
#     for i in t:
#         t2.append(int(int(ans_in)/i))
#     [a.append(i)for i in range(t2[0]+1)]
#     [b.append(i)for i in range(t2[1]+1)]
#     [c.append(i)for i in range(t2[2]+1)]
#     [d.append(i)for i in range(t2[3]+1)]
#     if c==[]:
#         r = itertools.product(d)
#     elif b==[]:
#         r = itertools.product(c, d)
#     elif a==[]:
#         r = itertools.product(b, c, d)
#     else:
#         r = itertools.product(a, b, c, d)
#     count=0
#     store=0
#     for i in list(r):
#         for j in range(len(i)):
#             store+=i[j]*t[j]
#         if store<=int(ans_in):
#             count+=1
#         store=0
#     # ans_out.append(count)
#     ans_out.append([ans_in,count])
# [print(i)for i in ans_out]