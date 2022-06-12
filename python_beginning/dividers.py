def dividers(number):
    list_dividers = []
    for i in range(1, number + 1):
        if number % i == 0:
            list_dividers.append(i)
    return list_dividers

for i in dividers(6):
    print(i)
