ans=[]
k=input()
while True:
    try:
        a=input()
        if a=='-1':
            break
        a1,a2=a.split(" ")
        tier=int(a1)-1
        num=int(a2)-1
        t=[]
        store = [
            ['1']
        ]
        for i in range(0,tier):
            t.append([x + '0' for x in store[i]])
            t.append([x + '1' for x in store[i]])
            store.append(t[0] + t[1])
            t = []
        ans.append(int(store[tier][num],2))
    except EOFError:
        pass
[print(get)for get in ans]
print()


# ans=[]
# k=int(input())
# for run in range(k):
#     a=input()
#     a1,a2=a.split(" ")
#     tier=int(a1)-1
#     num=int(a2)-1
#     t=[]
#     store = [
#         ['1']
#     ]
#     for i in range(0,tier):
#         t.append([x + '0' for x in store[i]])
#         t.append([x + '1' for x in store[i]])
#         store.append(t[0] + t[1])
#         t = []
#     ans.append(int(store[tier][num],2))
# [print(get)for get in ans]