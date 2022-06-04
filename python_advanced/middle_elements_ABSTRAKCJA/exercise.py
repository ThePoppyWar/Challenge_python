from math import ceil


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

class SequeneceOfNumbers:
    def __init__(self, start:int, stop:int, step: int):
        self.start = start
        self.stop = stop
        self.step = step

    def __len__(self):
        result = ceil((self.stop - self.start) / self.step)
        return result

    def __getitem__(self, index):
        if (index >= 0) and index < len(self):
            return self.start + index * self.step
        else:
            return "IndexError: 'Negative indexes are not supported, sorry!'"

print("========================================")
nums = SequeneceOfNumbers(14, 46, 4)
print(len(nums))
print("========================================")
print(nums[8])
print("========================================")
print(nums[2])
