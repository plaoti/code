n = int(input())
card = {}
lst = []
lst = list(map(int,input().split()))
#print(lst)
for i in range(n):
    if(lst[i] in card):
        card[lst[i]] +=1
    else:
        card[lst[i]] = 1
m = int(input())
lst = list(map(int,input().split()))
for index in lst:
    print(card.get(index,0),end=' ')
#print(card)