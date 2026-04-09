lst1 = list(map(int, input().split()))
command = input()

if command == "R5":
    temp = lst1[0:4]
    del lst1[0:4]
    for i in range(len(temp)):
        lst1.append(temp[i])
else:
    temp = lst1[0:2]
    del lst1[0:2]
    for i in range(len(temp)):
        lst1.append(temp[i])
print(lst1)