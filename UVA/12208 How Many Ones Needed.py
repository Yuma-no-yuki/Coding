l=[1]+[0]*30
dic = {0:1,1:2}
for i in range(1,len(l)):
    l[i]= 2**(i)+l[i-1]*2
    dic[i+1] = 2**(i)+l[i-1]*2+1 #dic[最高位元]=共有幾個1
def Count(x):
    s = str(bin(x))[2:]
    bit = len(s)
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            count += dic[bit-i-1]
            if s[:i].count('1')>0:
                count += s[:i].count('1')*(2**(bit-i-1))
    return count
ans = []
index = 0
while True:
    get = input()
    if get == '0 0':
        break
    index+=1
    a,b = map(int,get.split(' '))
    if a == 0:
        ans.append(f"Case {index}: {Count(b)}")
        continue
    a-=1
    ans.append(f"Case {index}: {Count(b)-Count(a)}")
[print(x)for x in ans]
# 1 1
# 2 4  (2^1+2*1)
# 3 12 (2^2+2*4)
# 4 32 (2^3+2*12)

# 1~3 4
# 1~7 12
# 1~15 32

# 10(1010) -> 13 + 2 + 2
# 11(1011) -> 13 + (2 + 2) + (1 + 2)
# 12(1100) -> 13 + 5 + 4