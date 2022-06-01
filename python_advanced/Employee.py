class Employee:
    def __init__(self, id_employee :int, first_name, last_name):
        self.id_employee = id_employee
        self.first_name = first_name
        self.last_name = last_name

    def set_salary(self, salary):
        if salary >=0 and isinstance(salary, (float, int)):
            self._salary = salary

    def print_employee(self):
        print(f"Employee id: {self.id_employee}, first name: {self.first_name}, last name: {self.last_name}, salary:{self._salary}")


employee_1 = Employee(1, "Bodzio", "Martyniuk")
print(employee_1)
employee_1.set_salary(15)
print(employee_1)
employee_1.print_employee()
