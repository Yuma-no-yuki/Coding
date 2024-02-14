table = [0] * 1000001
M_table = [0] * 1000001
max_n = 0
for i in range(1, 1000001):#建立 1~1000000 的因數表
    for j in range(i, 1000001, i):
        table[j] += 1
    if max_n <= table[i]: #進行最多因數數量比較，若當前索引>=max_n 進行改寫
        max_n = table[i]
        M_table[i] = i
    else:
        M_table[i] = M_table[i - 1] #若不成立 最多因數則為上一個
ans = []
for x in range(int(input())):
    ans.append(M_table[int(input())])
[print(x)for x in ans]