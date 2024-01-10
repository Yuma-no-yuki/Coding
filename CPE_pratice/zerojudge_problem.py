# https://zerojudge.tw/ShowProblem?problemid=d637
# 6
# # 10 10
# # 25 25
# # 65 75
# # 25 29
# # 25 17
# # 15 20
c=[0]*101
for i in range(int(input())):
    w = [int(i) for i in input().split(' ')]
    for j in range(100, w[0]-1, -1):
        c[j] = max(c[j-w[0]]+w[1], c[j])
print(c[-1])

# from itertools import combinations
#
# l = int(input())
# t1=[]
# t2=[]
# for i in range(l):
#     t=input()
#     t_1,t_2=t.split(" ")
#     t1.append(int(t_1))
#     t2.append(int(t_2))
# ll = []
# ll_c=[]
# for i in range(2,5):
#     s=list(combinations([0,1,2,3,4,5],i))
#     ans = 100
#     ans_l=[]
#     contrast=0
#     for j in range(len(s)):
#         [ans_l.append(x) for x in s[j]]
#         for t in ans_l:
#             contrast+=t1[t]
#         if contrast==100:
#             ll.append(ans_l)
#         contrast=0
#         ans_l=[]
# s1=0
# for i in ll:
#     for j in i:
#         s1+=t2[j]
#     ll_c.append(s1)
#     s1=0
# print(max(ll_c))
