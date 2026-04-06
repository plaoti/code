n = int(input())
lst = []
skip = 0
for i in range(n):
    a = input()
    lst = list(a)
    length = len(lst)
    o = 0; c = 0;
    for i in range(length):
        if(lst[i]=='('):
            o +=1
        if(lst[i]==')'):
            c +=1
            if(o<c and skip==0):
                print("NO")
                skip = 1
    if(o!=c and skip==0):
        print("NO")
        #break
    elif(o==c and skip ==0):
        print("YES")
    skip = 0
    