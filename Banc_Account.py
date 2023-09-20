class BankAccount:
    def __init__(self,name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self,new_balance):
        self.balance += new_balance

    def cash(self, new_balance):
        self.balance -= new_balance

    def my_balance(self):
        return self.balance