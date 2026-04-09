sentence = input()
sentence_mass = list(sentence.split())
with_holes = 0
without_holes = 0
new_mass = []

for i in range(len(sentence_mass)):
    quantity = 0
    for j in range(len(sentence_mass[i])):
        if sentence_mass[i][j] in "abdegopq":
            with_holes += 1
            quantity += 1
        else:
            without_holes += 1
    if quantity > 1:
        new_mass.append(sentence_mass[i])

print(new_mass)
print(with_holes, without_holes)