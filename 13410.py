n, k = map(int,input().split())
num = []
newnum = []
for i in range(k):
    num.append(n*(i+1))
    newnum.append(n*(i+1))
    #print(num[i],end=' ')
    newnum[i] = int(str(num[i])[::-1])
    #print(newnum[i])
n = max(newnum)
print(n)