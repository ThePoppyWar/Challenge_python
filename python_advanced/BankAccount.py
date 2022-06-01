class BankAccount:
    def __init__(self, number: int):
        self.number = number
        self.cash = 0.0

    def deposit_cash(self, amount):
        if amount > 0.0:
            self.cash += amount

    def withdraw_cash(self, amount):
        if self.cash >= amount:
            self.cash -= amount
            return amount
        else:
            return self.cash

    def print_info(self):
        print(f"Your bank account is {self.number} and you have {self.cash} cash.")


account_1 = BankAccount(159876489632564987)
account_1.deposit_cash(500)
account_1.withdraw_cash(25)
account_1.print_info()

print("------------------------------------------")

account_2 = BankAccount(5962564845668645646)
account_2.deposit_cash(300)
account_2.withdraw_cash(500)
account_2.print_info()
