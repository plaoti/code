sum = 0
for i in range(4):
    time = int(input())
    sum = sum + time
minu = sum // 60
sec = sum % 60
print(f'{minu}\n{sec}')