s="`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
a=input().lower()
out=""
for x in a:
    if x ==' ':
        out+=' '
    else:
        out+=s[s.find(x)-2]
print(out)
