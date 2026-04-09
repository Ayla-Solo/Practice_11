def string_to_characters(string):
    sentence_mass = []
    for i in range(len(string)):
        sentence_mass.append(string[i])
    sentence_mass.sort()
    string = "".join(sentence_mass)
    return string


string = input()
print(string_to_characters(string))