#未完成
from itertools import permutations
print(list(permutations([1,2,3])))
print(list(permutations([1,2,3,4])))
get = 3
l=[]
#123
#Y#123 132 231 213 321
#N#312


[l.append(x+1)for x in range(get)]
s=[]
for i in range(len(l)):
    s.append(l.pop())
print(s)

[l.append(x+1)for x in range(get)]
s=[]
s.append(l.pop(0))
for i in range(len(l)):
    s.append(l.pop())
print(s)

[l.append(x+1)for x in range(get)]
s=[]
s.append(l.pop(1))
for i in range(len(l)):
    s.append(l.pop())
print(s)