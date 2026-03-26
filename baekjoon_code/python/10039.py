sum = 0
for i in range(5):
    n = int(input())
    if(n>=40):
        sum = sum + n
    else:
        sum = sum + 40
print(sum//5)