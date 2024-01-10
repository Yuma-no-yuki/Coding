#102
ans=[]
while True:
    goal=int(input())
    if goal==0:
        break
    n=goal
    a=[]
    while True:
        for i in range(1,n+1):
            if n % i == 0 :
                a.append(i)
        if sum(a)==goal:
            break
        elif n==1:
            a.clear()
            a.append(-1)
            break
        else:
            n = n - 1
            a.clear()
    ans.append(max(a))
for get_ans in range(len(ans)):
    print(f"Case {get_ans+1}: {ans[get_ans]}")