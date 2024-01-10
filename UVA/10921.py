ans=[]
try:
    while True:
        a=input()
        count1=0
        count2=0
        change=[]
        for i in a:
            for j in range(65,90):
                if chr(j)==i:
                    count1+=1
        d={
            "A":2,
            "B":2,
            "C":2,
            "D":3,
            "E":3,
            "F":3,
            "G":4,
            "H":4,
            "I":4,
            "J":5,
            "K":5,
            "L":5,
            "M":6,
            "N":6,
            "O":6,
            "P":7,
            "Q":7,
            "R":7,
            "S":7,
            "T":8,
            "U":8,
            "V":8,
            "W":9,
            "X":9,
            "Y":9,
            "Z":9
        }
        for i in a:
            if i in d.keys():
                change.append(d.get(i))
            else:
                change.append(i)
        t="".join(map(str,change))
        ans.append(t)
except EOFError:
    pass
for get in ans:
    print(get)