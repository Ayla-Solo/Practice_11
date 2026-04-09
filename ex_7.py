number = input()
number_mass = list(map(int, number.split()))
summ_even = 0
summ_odd = 0

for i in range(len(number_mass)):
    if number_mass[i] % 2 == 0:
        summ_even += number_mass[i]
    else:
        summ_odd += number_mass[i]

print(summ_even, summ_odd)