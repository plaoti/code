n, m = map(int, input().split())
notHear = set()
notSee = set()
for i in range(n):
    a = input()
    notHear.add(a)
for i in range(m):
    a = input()
    notSee.add(a)
Good = notHear&notSee
result = sorted(Good)
print(len(result))
for i in range(len(result)):
    print(result[i])