def div(numb):
    div_list = []
    for i in range(1, int(numb ** 0.5) + 1):
        if numb % i == 0:
            div_list.append(i)
            if i != numb // i:
                div_list.append(numb // i)

    return sorted(div_list)


n = int(input())
print(div(n))