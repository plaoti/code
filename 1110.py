k = int(input())
sum = 0
count = 0
a=0;b=0;c=0;d=0
n = k
u = -1
while(u!=k):
    if(n>=10):
        a, b =map(int,str(n))
    else:
        a = 0; b = n
    sum = a + b
    if(sum>=10):
        c, d = map(int,str(sum))
    else:
        d = sum
    n = 10*b + d;
    count += 1
    u = n
    #print(f"test:  {b} {d} {count} {n}")
print(count)