# 2 -> 1 2
# 3 -> 1 3
# 4 -> 1 2 4
# 5 -> 1 5
# 6 -> 1 2 3 6
# 7 -> 1 7
# 8 -> 1 2 4 8
# 9 -> 1 3 9
# 10 -> 1 2 5 10
# 右邊的因數相加為所需要的輸出
ans = []
while True:
    a = int(input())
    if a == 0:
        break
    l=1
    ret = 0
    while l<=a:
        times = int(a/l) # times 為左區間l所出現的次數
        r = int(a/times) # r 為右區間,a/times可得知右區間的最大值
        ret += times*((l+r)*(r-l+1)/2)
        l = r+1
    ans.append(int(ret-1))
[print(x)for x in ans]