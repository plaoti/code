n = int(input())
k = n // 2
if(n%2==0):
    for i in range(n):
        for j in range(k):
            print("*",end='')
            print(" ",end='')
        print()
        for l in range(k):
            print(" ",end='')
            print("*",end='')
        print()
else:
    for i in range(n):
        for j in range(k+1):
            print("*",end='')
            print(" ",end='')
        print()
        for l in range(k):
            print(" ",end='')
            print("*",end='')
        print()