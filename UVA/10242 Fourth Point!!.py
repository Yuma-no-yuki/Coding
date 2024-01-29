ans = []
try:
    while True:
        ll = []
        con = [int(float(x) * 1000) for x in input().split(" ")]
        for i in range(4):
            ll.append([con[2 * i + 0], con[2 * i + 1]])
        for x in range(4):
            if ll.count(ll[x]) == 2:
                if x == 0:
                    ll[x], ll[x + 1] = ll[x + 1], ll[x]
                if x == 3:
                    ll[x - 1], ll[x] = ll[x], ll[x - 1]
        SI = []
        for i in ll:
            for j in i:
                SI.append(j)
        x = (SI[0] - (SI[2] - SI[6])) / 1000
        y = (SI[7] - (SI[3] - SI[1])) / 1000
        s = f"{str(x).split('.')[0]}.{str(x).split('.')[1].ljust(3, '0')} {str(y).split('.')[0]}.{str(y).split('.')[1].ljust(3, '0')}"
        ans.append(s)
except EOFError:
    pass
[print(x)for x in ans]

# Sample input
# 0.000 0.000 0.000 1.000 0.000 1.000 1.000 1.000
# 1.000 0.000 3.500 3.500 3.500 3.500 0.000 1.000
# 1.866 0.000 3.127 3.543 3.127 3.543 1.412 3.145

# Test
# -2.120 -10.728 -10.893 -23.084 -2.120 -10.728 8.773 12.356
