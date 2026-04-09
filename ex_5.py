number = input()
number_mass = list(map(int, number.split()))
summ = sum(number_mass)
print(summ/len(number_mass))