count = 0
ans = []
while True:
    get = input()
    if get == "":
        continue
    count += 1
    n,d = float(get.split(" ")[0]),float(get.split(" ")[1])

    if n == 0 and d == 0:
        break

    dd = d * d
    total = 0
    dot = []

    for i in range(int(n)):
        x, y = map(float, input().split())
        temp = dd - y * y
        if temp < 0.0:
            total = -1
        else:
            temp = temp**0.5
            dot.append([x - temp, x + temp]) #min_dot max_dot

    if total == 0:
        dot.sort(key=lambda v: v[1])
        idx = 0
        while idx < n:
            total += 1
            x = dot[idx][1]
            idx += 1
            while idx < n and dot[idx][0] <= x:
                idx += 1
    dot.clear()
    ans.append(f"Case {count}: {total}")
[print(x)for x in ans]

