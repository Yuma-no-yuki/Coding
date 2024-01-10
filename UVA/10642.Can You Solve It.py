# https://cpe.cse.nsysu.edu.tw/cpe/test_data/2022-03-22
get_times=[]

def set(a1,a2,a3,a4):
    origin_x=int(a1)
    origin_y=int(a2)
    des_x=int(a3)
    des_y=int(a4)
    times=0
    while True:
        if origin_x==des_x and origin_y==des_y:
            get_times.append(times)
            break
        elif origin_y==0:
            times += 1
            origin_y=origin_x+1
            origin_x=0
        else:
            times += 1
            origin_y-=1
            origin_x+=1
get=int(input())
for i in range(get):
    a1,a2,a3,a4=map(int,input().split())
    set(a1,a2,a3,a4)
for i,v in enumerate(get_times):
    print(f"Case {i+1}: {v}")