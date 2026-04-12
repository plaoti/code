n = int(input())
hanSoo = 0
for i in range(1,n+1):
    if(i>=100):
        a = str(i)
        numberList = list(a)
        #print(numberList)
        if(int(numberList[0])+int(numberList[2])==int(numberList[1])*2):
            hanSoo +=1
    else:
        hanSoo +=1
print(hanSoo)