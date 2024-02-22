ans = []
try:
    while True:
        s1,s2 = input().split(' ')
        if len(s1)>len(s2):
            s1,s2=s2,s1
        i = 0
        j = 0
        while i<len(s1) and j<len(s2):
            if s1[i] == s2[j]:
                i+=1
                j+=1
            else:
                j+=1
        if i == len(s1):
            ans.append('Yes')
        else:
            ans.append('No')
except EOFError:
    pass
[print(_)for _ in ans]