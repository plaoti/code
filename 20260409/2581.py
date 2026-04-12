m = int(input())
n = int(input())
Sum = 0
Sosu = []
def sosuCheck(n):
    sosu = 1
    for i in range(2,n):
        if(n%i==0):
            sosu = 0
            break
    return sosu
if(m==1):
    m=2
for i in range(m,n+1):
    if(sosuCheck(i)!=0):
        Sum += i
        Sosu.append(i)
if(Sum!=0):
    print(Sum)
    print(Sosu[0])
else:
    print(-1)
    