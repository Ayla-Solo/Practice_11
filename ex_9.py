
mass_text = []  # список слов из текущей строки
text = ""       # вводимая строка
quantity = []   # количество повторений слов
no_repetitions_mass = []  # список уникальных слов


while text != " ":
    text = input()
    text = text.replace(",", "")  
    text = text.replace(".", "")  
    text = text.lower()     
    if text != " ":
        mass_text = list(text.split())  # разбиваем строку на слова
        for i in range(len(mass_text)):
            if mass_text[i] in no_repetitions_mass:
                # увеличиваем счетчик слова
                quantity[no_repetitions_mass.index(mass_text[i])] += 1
            else:
                # добавляем новое слово
                no_repetitions_mass.append(mass_text[i])
                quantity.append(1)

# сортировка по убыванию частоты 
for i in range(len(quantity)-1):
    for j in range(len(quantity)-i-1):
        if quantity[j] < quantity[j+1]:
            quantity[j], quantity[j+1] = quantity[j+1], quantity[j]
            no_repetitions_mass[j], no_repetitions_mass[j + 1] = no_repetitions_mass[j + 1], no_repetitions_mass[j]

print(no_repetitions_mass)
print(quantity)
