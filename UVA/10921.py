set = {
    'A':2,
    'B':2,
    'C':2,
    'D':3,
    'E':3,
    'F':3,
    'G':4,
    'H':4,
    'I':4,
    'J':5,
    'K':5,
    'L':5,
    'M':6,
    'N':6,
    'O':6,
    'P':7,
    'Q':7,
    'R':7,
    'S':7,
    'T':8,
    'U':8,
    'V':8,
    'W':9,
    'X':9,
    'Y':9,
    'Z':9
}
ans = []
try:
    while True:
        s=input()
        s2 = ''
        count1 = 0
        count2 = 0
        for x in s:
            if x in list(set.keys()):
                s2+=str(set[x])
            else:
                s2+=x
            if x == '-':
                count2+=1
            else:
                count1 += 1
        ans.append(s2)
except EOFError:
    pass
[print(x)for x in ans]
