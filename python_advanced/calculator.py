
class Calculator:
    def __init__(self):
        self.list = []

    def add(self, num1, num2):
        result = num1 + num2
        self.list.append(f'Add {num1} to {num2} got {result}')

    def multiply(self, num1, num2):
        result = num1 * num2
        self.list.append(f"Multiplied {num1} with {num2} got {result}")

    def print_operation(self):
        for one_list in self.list:
            print(one_list)

calculator_1 = Calculator()
calculator_2 = Calculator()

calculator_1.add(5, 14)
calculator_2.multiply(10, 20)

calculator_2.print_operation()
calculator_1.print_operation()