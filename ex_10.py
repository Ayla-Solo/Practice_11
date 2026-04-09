lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst1_new = []
beginning, the_end = map(int, input().split())

for i in range(the_end, beginning-1, -1):
    lst2.append(lst1[i])
del lst1[beginning:the_end+1]

print(lst1)
print(lst2)