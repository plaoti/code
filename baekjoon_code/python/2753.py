year = int(input())
if(year%4==0 and year %100!=0):
    #print(f"{year}년은 윤년입니다.")
    print(1)
elif(year%400==0):
    #print(f"{year}년은 윤년입니다.")
    print(1)
else:
    #print(f"{year}년은 윤년이 아닙니다.")
    print(0)