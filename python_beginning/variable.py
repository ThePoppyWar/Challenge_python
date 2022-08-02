user_choise = ['load data', 'export data', 'analyze & predict']
choise = x

def DisplayOptions(lista):
    choice_usra = input("1 - load data, 2 - export data, 3 - analyze & predict, Select option above or press enter to exit: ")
    return choice_usra

while choise:
    print(DisplayOptions())
