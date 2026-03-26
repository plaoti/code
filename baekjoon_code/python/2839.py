n = int(input())
count = -1

for i in range(n//5,-1,-1):
    r = n - 5 * i
    if(r%3==0):
        count = r//3 + i
        break

print(count)