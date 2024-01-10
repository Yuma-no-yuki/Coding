#2023/3/25
l=[['#','#','#','#']
    ,['#','J','F','#']
    ,['#','.','.','#']
   ,['#','.','.','#']]
# l=[['#','#','#'],['#','J','.'],['#','.','F']]
for x in range(len(l)):
    if "F" in l[x]:
        if l[x-1][l[x].index('F')]=='.':
            l[x - 1][l[x].index('F')]='F'
        if l[x][l[x].index('F')-1]=='.':
            l[x][l[x].index('F')-1]='F'
        if x+1>= len(l):
            break
        if l[x+1][l[x].index('F')]=='.':
            l[x + 1][l[x].index('F')]='F'
        if l[x][l[x].index('F')+1]=='.':
            l[x][l[x].index('F')+1]='F'
for x in range(len(l)):
    if "J" in l[x]:
        if l[x-1][l[x].index('J')]=='.':
            l[x - 1][l[x].index('J')]='J'
        if l[x][l[x].index('J')-1]=='.':
            l[x][l[x].index('J')-1]='J'
        if x+1>= len(l):break
        if l[x+1][l[x].index('J')]=='.':
            l[x + 1][l[x].index('J')]='J'

        if l[x][l[x].index('J')+1]=='.':
            l[x][l[x].index('J')+1]='J'

[print(_) for _ in l]


