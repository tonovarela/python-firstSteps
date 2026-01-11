class BankAccount:

     def __init__(self,balance):
        self.__balance = balance

     def deposit(self, amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposit {amount} in your acccount, after ${self.__balance- amount}, before ${self.__balance} ")
 
     def get_balance(self):
        return self.__balance        




account = BankAccount(1500)
account.deposit(100)
print(account.get_balance())