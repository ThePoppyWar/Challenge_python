from random import randint


def d6(num):
    sum = 0
    for roll in range(1, num + 1):
        dice = randint(1, 6)
        sum += dice
    return sum

trial_one = d6(5)
print(trial_one)