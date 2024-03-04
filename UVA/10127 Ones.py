ans = []
try:
    while True:
        n = int(input())
        d = 1 #代表餘數
        count = 1
        while d % n != 0:
            d = (d*10+1) % n #應用同餘理論
            count += 1
        ans.append(count)
except EOFError:
    pass
[print(x)for x in ans]