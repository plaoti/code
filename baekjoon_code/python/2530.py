hour, minu, sec = map(int, input().split())
n = int(input())
secmoak = n // 60; secnam = n % 60;
sec = sec + secnam;
if(sec >=60):
    secmoak = secmoak + sec // 60;
    sec = sec % 60;
minu = minu + secmoak;
if(minu >=60):
    minmoak = minu // 60; minnam = minu % 60;
    minu = minnam; hour = hour + minmoak
if(hour>=24):
    hour = hour % 24;
print(hour, minu, sec)