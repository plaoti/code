import sys

people, n = map(int, input().split())
input = sys.stdin.readline
lst = {}
for i in range(n):
    Id = input().strip()
    lst[Id] = i+1;
lst_sorted = []
lst_sorted = sorted(lst.items(), key=lambda x: x[1])
#print(lst_sorted)
if(people>len(lst_sorted)):
    people = len(lst_sorted)
for i in range(people):
    print(lst_sorted[i][0])