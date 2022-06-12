def name_sorter(names):
    result = {'female': [], 'male': []}
    for name in names:
        if name[-1] == "a":
            result['female'].append(name)
        else:
            result['male'].append(name)
    return result

names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]
print(name_sorter(names))
