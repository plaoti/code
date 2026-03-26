a, b = map(int,input("큰 숫자 먼저 공백으로 구분하여 입력해 주세요").split())
while(b!=0):
    x = a; a = b; b = x%b
print("최대공약수는",a)