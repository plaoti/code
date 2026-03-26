sum = 0
for i in range(3):
    a, b, c, d = map(int, input().split(' '))
    sum = sum + a + b+ c+ d
    if(sum==3): print("A");
    if(sum == 2): print("B")
    if(sum==1): print("C");
    if(sum==0): print("D");
    if(sum==4): print("E");
    sum = 0
    