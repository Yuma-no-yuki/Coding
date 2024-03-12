ans = []
for _ in range(int(input())):
    input()
    n1,n2 = map(int,input().split(' '))
    dic = {}
    for i in range(n1):
        d0,d1 = input().split(' ')
        if d0[0] in dic.keys():
            l = list(dic[d0[0]])
            l.append(d1[0])
            dic[d0[0]]=l
        else:
            dic[d0[0]] = list(d1[0])
    for j in range(n2):
        a1,a2 = input().split(' ')
        a1 = a1[0]
        a2 = a2[0]
        s1 = a1
        s2 = a2
        while a1 != 'R':
            for k in dic:
                if a1 in dic[k]:
                    a1 = k
                    s1 += a1
        while a2 != 'R':
            for k in dic:
                if a2 in dic[k]:
                    a2 = k
                    s2 += a2
        count = 0
        for i in range(min(len(s1), len(s2))):
            if s1[::-1][i] == s2[::-1][i]:
                count += 1
        s2 = s2[::-1]
        if count - 1 == 0:
            ans.append(s1+s2[count:])
        else:
            ans.append(s1[:-(count-1)] + s2[count:])
    ans.append('')
[print(x)for x in ans[:-1]]