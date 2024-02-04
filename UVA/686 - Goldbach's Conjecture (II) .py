prime = [0] * 32769  # Max = 2^15 + 1
a = 1
for i in range(2, 32769):
    if prime[i] == 0:
        j = i
        while j*i<=32768:
            prime[i * j] = 1
            j+=1
ans = []
while a != 0:
    a = int(input())
    if a == 0:
        break
    count = 0
    for i in range(2, a // 2 + 1):
        if prime[i] == 0 and prime[a - i] == 0:
            count += 1
    ans.append(count)
[print(x)for x in ans]