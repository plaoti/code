n = int(input())
for i in range(n):
    for l in range(i):
        print(" ",end='')
    for j in range(2*(n-i)-1):
        print("*",end='')
    print("")
for i in range(n-1):
    for l in range(n-i-2):
        print(' ',end='')
    for j in range(2*(i+1)+1):
        print("*",end='')
    print("")