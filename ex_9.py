mass_text = []
text = ""
quantity = []
no_repetitions_mass = []

while text != " ":
    text = input()
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.lower()
    if text != " ":
        mass_text = list(text.split())
        for i in range(len(mass_text)):
            if mass_text[i] in no_repetitions_mass:
                quantity[no_repetitions_mass.index(mass_text[i])] += 1
            else:
                no_repetitions_mass.append(mass_text[i])
                quantity.append(1)

for i in range(len(quantity)-1):
    for j in range(len(quantity)-i-1):
        if quantity[j] < quantity[j+1]:
            quantity[j], quantity[j+1] = quantity[j+1], quantity[j]
            no_repetitions_mass[j], no_repetitions_mass[j + 1] = no_repetitions_mass[j + 1], no_repetitions_mass[j]

print(no_repetitions_mass)
print(quantity)