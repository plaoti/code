month = int(input())
startDay = [4,0,0,3,5,1,3,6,2,4,0,2] #시작요일
monthDay = [31,28,31,30,31,30,31,31,30,31,30,31] #일.

for i in range(startDay[month-1]):
    print("    ", end="")

for i in range(1, monthDay[month-1]+1):
    print(f"{i:3d}", end=" ")

    if (startDay[month-1]+i)%7 == 0:
        print()