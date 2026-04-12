lst = [0] *20000
for i in range(10000):
    result = 0
    for j in str(i):
        result += int(j)
    lst[result + i] +=1
for i in range(10000):
    if(lst[i]==0):
        print(i)