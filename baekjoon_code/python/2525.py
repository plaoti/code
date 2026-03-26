hour, minu = map(int,input().split())
n = int(input())
if(minu+n>=60):
    m = (minu+n)//60
    nam = (minu+n)%60
    minu = nam
    hour = m + hour
    if(hour>=24):
        hour = hour % 24
    print(hour, minu)
else:
    print(hour,minu+n)