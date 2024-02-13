get_input=int(input())
list_set=[]
i=1
store_ans=""
while True:
    list_set.append(i)
    i+=1
    if get_input==0:
        print(store_ans)
        break
    elif list_set.count(sum(list_set)-get_input)==1:
        store_ans+=f"{sum(list_set)-get_input} {len(list_set)}"+"\n"
        get_input=int(input())
        list_set.clear()
        i=1