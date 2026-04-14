def fibo(n):
    if(n==0):
        return 0
    elif n==1:
        return 1
    else: return fibo(n-1) + fibo(n-2)

n = int(input("피보나치하고 싶은 수: "))
print(f"{n}번째 피보나치 수: {fibo(n)}")