#7/(-2) = -3...1
#-3/(-2) = 1...-1

#7/(-2) = -3...1
#-3/(-2) = 2...1
#2/(-2) = -1...0
#-1/(-2) = 1...1
#1
#11011

#-2/(-2) = 1...0
#1
#01

#1/(-2) = 0...1
#0
#10

#-1/(-2) = 1...1
#1
#11

#4/(-2) = -2...0
#-2/(-2) = 1...0
ans=[]
for x in range(int(input())):
    a=int(input())
    s=""
    if a == 1:
        ans.append(f"Case #{x+1}: 1")
    elif a == 0:
        ans.append(f"Case #{x+1}: 0")
    else:
        while True:
            na = int(a / (-2))
            ma = a - na * (-2)
            if ma < 0:
                na += 1
                ma = a - na * (-2)
            s += str(ma)
            a = na
            if a == 0 or a == 1:
                s += str(a)
                break
        s = s[::-1]
        ans.append(f"Case #{x+1}: {s}")
[print(x)for x in ans]
