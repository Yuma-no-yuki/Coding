from itertools import combinations
fff_ans=[]
ans_final = ""
while True:
    get_input=input()
    if get_input == "":
        break

    a = input()
    store = a.split(" ")
    store = [int(x) for x in store]
    store = [-x for x in store]
    ans = []
    c = 1
    c_2 = 0
    ans2 = sum(store)
    if len(store)==1:
        ans_final+="x"
        if ans2>0:
            ans_final+="+"
        ans_final+=f"{ans2}"
    else:
        for i in range(2, len(store) + 1):
            a = combinations(range(len(store)), i)
            k = list(a)
            for j in k:
                if len(j) > 1:
                    c = 1
                    for t in j:
                        c *= store[t]
                c_2 += c
            ans.append(c_2)
            c_2 = 0
        ans_final+=f"x^{len(store)}"
        if ans2 != 0 and len(store) - 1 == 0:
            if ans2 > 0:
                ans_final += "+"
            ans_final += "0"
        elif ans2 != 0 and len(store) - 1 == 1:
            if ans2 > 0:
                ans_final += "+"
            ans_final += f"{ans2}x"
        elif ans2 != 0:
            if ans2 > 0:
                ans_final += "+"
            ans_final += f"{ans2}x^{len(store) - 1}"
        for i in range(len(ans)):
            if len(store) - 2 - i == 1 and ans[i] != 0:
                if ans[i] > 0:
                    ans_final += "+"
                ans_final += f"{ans[i]}x"
            elif ans[i] == 0 and len(store) - 2 - i == 0:
                ans_final += "+0"
            elif ans[i] != 0:
                if ans[i] > 0:
                    ans_final += "+"
                ans_final += f"{ans[i]}x^{len(store) - 2 - i}"
    ans_final=ans_final.replace("x0","x+0")
    ans_final = ans_final.replace("x^0", "")
    ans_final = ans_final.replace("1x", "x")
    ans_final=ans_final.replace("+"," + ")
    ans_final=ans_final.replace("-"," - ")
    ans_final+=" = 0"
    fff_ans.append(ans_final)
    ans_final=""
for i in fff_ans:
    print(i)