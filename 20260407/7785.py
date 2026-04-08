n = int(input())
nameList = []
s = set()
for i in range(n):
    name, check = input().split(' ')
    if(check=='enter'):
        s.add(name)
    if(check=='leave'):
        s.remove(name)
nameList.sort()
for name in sorted(s, reverse=True):
    print(name)