import time
def fibo(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    a, b = 0,1
    for i in range(2,n+1):
        a, b = b, a+b
    return b
n = int(input("Enter n: "))
start = time.time()
print(f"{n}번째 피보나치 {fibo(n)}")
print(f"걸린 시간{time.time()-start}")
