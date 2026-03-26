import time, math

n = int(input("소수 판별 원하는 숫자"))

start_time = time.time()
for i in range(2,int(math.sqrt(n))+1):
    if(n%i==0):
        print(f"{n}은 {i}로 나누어 떨어짐")
        break
else:
    print(f"{n}은 소수가 맞음.")

print("걸린 시간: ",time.time() - start_time)