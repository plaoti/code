lst = []
for i in range(9):
    n = int(input())
    lst.append(n)
Max = max(lst)
for i in range(9):
    if(lst[i]==Max):
        num = i+1
print(f"{Max}\n{num}")