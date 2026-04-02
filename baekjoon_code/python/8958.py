n = int(input())
for i in range(n):
    score = 0
    strike = 0
    str = input()
    lst = list(str)
    #print(lst)
    length = len(lst)
    if(lst[0]=='O'):
        score +=1
        strike =1
    for j in range(1,length):
        if(lst[j]=='O'):
            score = score + 1 + strike
            strike +=1
        else:
            strike = 0
    print(score)