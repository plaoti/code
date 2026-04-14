import time
def fibo(n):
    if(n==1) or (n==2):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n = int(input("Enter n: "))
start = time.time()
print(f"{n}번째 피보나치 {fibo(n)}")
print(f"걸린 시간{time.time()-start}")
