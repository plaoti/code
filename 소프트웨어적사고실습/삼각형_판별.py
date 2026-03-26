a, b, c = map(int,input("무슨 삼각형인지 판단하고자 하는 삼각형의 세 변을 공백으로 구분해 정수 형태로 입력해 주세요: ").split())
p = 0
a, b, c = sorted([a,b,c])
if(a+b>c and a+c>b and b+c>a):
    print("삼각형 성립요")
    p = 1
else:
    print("삼각형이 안됨요")
if((a**2+b**2)==c**2 and p==1):
    print("직각 삼각형이네요 !")
elif((a**2+b**2)<c**2 and p==1):
    print("둔각삼각형이네요 !")
elif((a**2+b**2)>c**2 and p==1):
    print("예각삼각형이네요 !")