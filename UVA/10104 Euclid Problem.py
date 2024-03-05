ans=[]
try:
    while True:
        n1,n2 = map(int,input().split(' '))
        l = []
        def gcd(a,b):
            while a!=1 and b !=0: #輾轉相除
                l.append([a,b])
                a = a%b
                a,b = b,a
            return a
        G = gcd(n1,n2)
        l=l[::-1]
        f0 = 1
        f1 = 0
        for x in l:
            f0 = f1
            f1 = (G-f0*x[0])//x[1]
        ans.append(f"{f0} {f1} {G}")
except EOFError:
    pass
[print(x)for x in ans]