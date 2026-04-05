lst = []
sum = 0
for i in range(42):
    lst.append(0)
for i in range(10):
    n = int(input())
    lst[(n%42)-1] +=1
for i in range(42):
    if(lst[i]!=0):
        sum +=1
print(sum)