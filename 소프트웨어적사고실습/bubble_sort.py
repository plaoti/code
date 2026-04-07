lst = list(map(int, input().split()))
print(lst)
n = len(lst)
for i in range(n):
    for j in range(i, n):
        if(lst[j]<=lst[i]):
            tmp = lst[j]
            lst[j] = lst[i]
            lst[i] = tmp
print(lst)