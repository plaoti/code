M=int(input())

Month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

lst = [4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2]
start_day = lst[M-1]
print(f"         {M}월     ")
if(start_day==0):
    print("일 월 화 수 목 금 토",end='')
else:
    print("일 월 화 수 목 금 토")

day=1
output_n = 0

for i in range(lst[M-1]):
    print("  ",end=" ")
    output_n +=1
while(day!=Month[M-1]+1):
    if output_n%7==0: 
        print(" ")
    if(day<10):
        print(f'{day}',end="  ")
    else:
        print(day,end=" ")
    day+=1
    output_n +=1