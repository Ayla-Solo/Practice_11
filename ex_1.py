mass_number = []
mass_number_new = []
for i in range(10):
    mass_number.append(int(input()))
for i in range(1, 10):
    mass_number_new.append(mass_number[i-1]+mass_number[i])
print(mass_number_new)