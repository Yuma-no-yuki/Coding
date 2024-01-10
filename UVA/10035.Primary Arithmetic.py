count=0
ans=[]
ans_str=""
car=0
while True:
    get_in=input()
    if get_in=="0 0":
        break
    a=get_in.split(" ")
    b=int(a[0])
    c=int(a[1])
    while b!=0 and c!=0:
        if b%10+c%10+car>=10:
            count+=1
            car=1
        else:
            car=0
        b=b/10
        c=c/10

    if count==0:
        ans_str+="No carry operation."
    elif count==1:
        ans_str+=f"{count} carry operation."
    else:
        ans_str+=f"{count} carry operations."
    ans.append(ans_str)
    ans_str=""
    count=0
for i in ans:
    print(i)