def uclid(a,b):
    if(b==0):
        return a
    else:
        return uclid(b,a%b)
a, b = map(int,input("공백 구분해서 입력").split())
print(f"{a}와 {b}의 최대공약수는 {uclid(a,b)}입니다.")