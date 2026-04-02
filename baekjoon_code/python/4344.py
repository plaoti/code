n = int(input())
for i in range(n):
    avgUp = 0
    lst = list(map(int,input().split()))
    hap = sum(lst) - lst[0]
    avg = sum(lst) // lst[0]
    #print(f'평균 : {avg}')
    for j in range(1,lst[0]+1):
        if(lst[j]>=avg):
            avgUp +=1
    percent = (avgUp / lst[0]) * 100
    print("{:.3f}%".format(percent))