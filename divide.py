number1 = input("Give a number 1: ")
number2 = input("Give a number 2: ")

def divide(a, b):
    try:
        number1 = int(a)
        number2 = int(b)
    except ValueError:
        print("It's not a natural number")
        return None
    try:
        result = number1/number2
    except ZeroDivisionError:
        return None
    return result

print(divide(number1,number2))

