people = 0
maximum = 0
for i in range(4):
    a, b = map(int,input().split())
    people = people + b -a
    
    if(people>maximum):
        maximum = people
print(maximum)