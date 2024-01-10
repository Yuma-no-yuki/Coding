setting=int(input())
final_ans=[]
for index in range(setting):
    get_day=int(input())
    ans=[0]*get_day
    h=int(input())
    h_set=[]
    for i in range(h):
        h_set.append(int(input()))
    for i in range(get_day):
        if i==5 or i==6:
            ans[i]=0
        elif i>7 and i%7==5 or i%7==6 and i>7:
            ans[i]=0
        else:
            for j in range(len(h_set)):
                if i%h_set[j]==h_set[j]-1:
                    ans[i]=1
    final_ans.append(sum(ans))
for get in final_ans:
    print(get)