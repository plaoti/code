n = int(input())
bookDick = {}
for i in range(n):
    word = input()
    if(word in bookDick):
        bookDick[word] +=1
    else:
        bookDick[word] = 1
Max = max(bookDick.values())

lst = []
for key, value in bookDick.items():
    if(value == Max):
        lst.append(key)

lst.sort()
print(lst[0])