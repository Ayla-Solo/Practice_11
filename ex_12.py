sentence = input()  # ввод строки
sentence_mass = list(sentence.split())  # разбиваем на слова
with_holes = 0      # счетчик букв с отверстиями
without_holes = 0   # счетчик букв без отверстий
new_mass = []       # слова с >= 2 буквами с отверстиями

# перебор слов
for i in range(len(sentence_mass)):
    quantity = 0  # количество "дырявых" букв в слове
    for j in range(len(sentence_mass[i])):
        # проверка на буквы с отверстиями
        if sentence_mass[i][j] in "abdegopq":
            with_holes += 1
            quantity += 1
        else:
            without_holes += 1
    # если в слове больше одной такой буквы — добавляем
    if quantity > 1:
        new_mass.append(sentence_mass[i])

print(new_mass) 
print(with_holes, without_holes) 
