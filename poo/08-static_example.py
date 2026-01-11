class BankAccount:
    interest_rate = 0.02 

    def __init__(self,holder, initial_balance=0):
        self.holder = holder
        self.balance = initial_balance 

    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate   
        print(f"Interest rate updated to {cls.interest_rate * 100}%")

    @staticmethod
    def validate_amount(amount):
        if amount <= 0:
            raise ValueError("Amount must be non-negative")
        return True  

    def withdraw(self, amount):
        self.validate_amount(amount)  
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}")

    def deposit(self, amount):
        self.validate_amount(amount)  
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")    


account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

account1.deposit(200)
account2.withdraw(700)