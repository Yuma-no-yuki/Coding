s = ''
ans = []
try:
    while True:
        a = input()
        if a[-1]!='#':
            s += a
        else:
            s += a
            s = s[:-1]
            s = int(str(s),2)
            if eval(f"{s}%131071")==0:
                ans.append("YES")
                s = ''
            else:
                ans.append("NO")
                s = ''
except EOFError:
    pass
[print(x)for x in ans]