l = [0]*100 #每100個一次循環
count = 0
dic = {}
for i in range(1,101):
    count += i**i
    dic[i] = count%10
while True:
    n = input()
    if n == "0":
        break
    if int(n[-2:])==0:
        print(dic[100])
    else:
        print(dic[int(n[-2:])])