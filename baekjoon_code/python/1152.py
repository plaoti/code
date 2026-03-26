str = input()
lst = list(str)
length = len(lst)
if(lst[0] == ' ' and lst[length-1]==' '):
    print(lst.count(' ')-1)
elif(lst[0]==' 'or lst[length-1]==' '):
    print(lst.count(' '))
else:
    print(lst.count(' ')+1)
