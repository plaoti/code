
n = int(input("윤년인지 판단하고자 하는 년도를 입력해 주세요.(정수 형태) : "))
if(n%4==0 and n%100!=0):
    print(1)
elif(n%4==0 and n%400==0):
    print(1)
else:
    print(0)
print("1이면 윤년, 0이면 아님")
    
