n = int(input())
sum = 0
lst = list(map(int, input().split()))
lst.sort()
for i in range(n):
    sum += lst[i] * (i - (n-i-1))
print(sum*2)