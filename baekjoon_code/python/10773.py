n = int(input())
lst = []
sum = 0
for i in range(n):
    a = int(input())
    if(a!=0):
        lst.append(a)
    else:
        length = len(lst)
        del lst[length-1]
    #print(lst)
length = len(lst)
for i in range(length):
    sum += lst[i]
print(sum)