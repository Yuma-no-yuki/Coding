ans = []
# 已於UVA中測試->AC
try:
    while True:
        n1,n2 = map(float,input().split(' '))
        n1,n2 = min(n1,n2),max(n1,n2)
        Min = round(n1/2,4) #n1&n2中的最小值/2為最小值的x 另一個x為0
        if int(str(Min).split('.')[1][-1])>=5: #因使用python進行浮點數計算->數值需進行微調
            Min += 0.0001
            Min = round(Min,3)
        Max = round(((n1+n2)-(n1**2-n1*n2+n2**2)**0.5)/6,3) #一次微分求極大值
        Min = f"{str(Min).split('.')[0]}.{str(Min).split('.')[1].ljust(3,'0')}"
        Max = f"{str(Max).split('.')[0]}.{str(Max).split('.')[1].ljust(3,'0')}"
        ans.append(f"{Max} 0.000 {Min}")
except EOFError:
    pass
[print(x)for x in ans]