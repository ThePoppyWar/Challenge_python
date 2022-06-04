def middle_elements(sequences):
    result = []
    for sequences in sequences:
        if len(sequences) == 0:
            continue
        ind = len(sequences) // 2
        result.append(sequences[ind])
    return result


print(middle_elements(
    [[6, 7, 8, 9, 10], ["Kto", "to", "taki?"], [], ["sześć", "siedem", "osiem", "dziewięć"], [8, "to", "osiem"]]))


def middle_elements_2(sequences):
    if len(sequences) == 0:
        return "List is empty"
    else:
        return sequences[int(len(sequences) / 2)]


lista1 = [6, 7, 8, 9, 10]
lista2 = ["Kto", "to", "taki?"]
lista3 = []
lista4 = ["sześć", "siedem", "osiem", "dziewięć"]
lista5 = [8, "to", "osiem"]

print(middle_elements_2(lista1))
print(middle_elements_2(lista2))
print(middle_elements_2(lista3))
print(middle_elements_2(lista4))
print(middle_elements_2(lista5))
