import math
word_list = list(input().strip())  
length = len(word_list)
summ = 0
for i in word_list:
    if('a'<=i<='z'):
        summ = summ + ord(i) - ord('a')+1
    if('A'<=i<='Z'):
        summ = summ + ord(i) - ord('A')+27
for i in range(2,int(math.sqrt(summ))+1):
    if(summ%i==0): 
        print("It is not a prime word.")
        break
else:
    print("It is a prime word.")