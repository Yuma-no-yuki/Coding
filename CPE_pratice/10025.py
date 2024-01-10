#10025 The ? 1 ? 2 ? ... ? n = k problem

# 1  +1
# 2  -1+2
# 3  +1+2
# 4  -1+2+3
# 5  +1+2+3+4-5
# 6  +1+2+3
# 7  +1+2+3-4+5
# 8  -1+2+3+4
# 9  +1+2-3+4+5
# 10 +1+2+3+4
get_count=int(input())
ans=[]
for index in range(get_count):
    a=[]
    goal=int(input())
    i=1
    t=0
    if goal==0:
        ans.append(3)
        continue
    elif goal<0:
        goal*=-1
    while t<goal:
        a.append(i)
        i+=1
        t=sum(a)
    while (t-goal)%2==1:
        a.append(i)
        i+=1
        t=sum(a)
    ans.append(len(a))
for get in ans:
    print(get)
    # default=int((t-goal)/2)
    # k=0
    # while sum(a)!=goal:
    #     if sum(a)-goal/2>=a[-k]:
    #         a[-k]*=-1
    #     k+=1
    # print(a)