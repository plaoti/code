year = 0
b = 1000000

while(b<2000000):
    year +=1
    b = int(b*1.05)
print(f"{year}년 저금 하시면 {b}원 됩니다. (5% 이율)")