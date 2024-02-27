ans = []
count = 0
while True:
    count += 1
    s = ''
    finp = int(input())
    if finp == 0:
        break
    for i in range(finp):
        get = input()
        s+=get
    s2 = ''
    for i in range(int(input())):
        get2 = input()
        s2+=get2
    check = '0123456789'
    c1=''
    c2=''
    c1 = [str(x)for x in s if x in check]
    c2 = [str(x)for x in s2 if x in check]
    if get == get2:
        ans.append(f'Run #{count}: Accepted')
    else:
        if c1 == c2:
            ans.append(f'Run #{count}: Presentation Error')
        else:
            ans.append(f'Run #{count}: Wrong Answer')
[print(x)for x in ans]

# Sample input
# 2
# The answer is: 10
# The answer is: 5
# 2
# The answer is: 10
# The answer is: 5
# 2
# The answer is: 10
# The answer is: 5
# 2
# The answer is: 10
# The answer is: 15
# 2
# The answer is: 10
# The answer is:  5
# 2
# The answer is: 10
# The answer is: 5
# 3
# Input Set #1: YES
# Input Set #2: NO
# Input Set #3: NO
# 3
# Input Set #0: YES
# Input Set #1: NO
# Input Set #2: NO
# 1
# 1 0 1 0
# 1
# 1010
# 1
# The judges are mean!
# 1
# The judges are good!
# 0