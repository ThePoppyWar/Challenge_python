import random


def roll (count_dick, typ_dick= 6, modyfi_result = 0):
    result = 0
    for _ in range(count_dick):
        if typ_dick not in (3, 4, 6, 8,10, 12, 100):
            raise Exception("No such dice!")
        else:
            result += random.randint(1, typ_dick)
            result += modyfi_result
    return result

print(roll(2))
print(roll(4, 10, 7))
print(roll(1, 2))