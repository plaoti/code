n = int(input())
lst= []
for i in range(n):
    k = int(input())
    lst.append(k)
lst.sort()
for i in range(n):
    print(lst[i])
    