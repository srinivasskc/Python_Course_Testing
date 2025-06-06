"""
Exercise 3: Track a bank account balance

Task:
Create a class BankAccount
Add an __init__ method with starting balance
Add methods:
deposit(self, amount) → adds to balance
withdraw(self, amount) → subtracts from balance
"""

class BankAccount:
    """
    A class to represent a bank account with methods to deposit and withdraw funds.
    """
    def __init__(self, starting_balance):
        self.balance = starting_balance
    
    def deposit(self, amount):
        """Method to deposit an amount into the account."""
        print(f"Depositing {amount} to the account.")
        if amount > 0:
            self.balance = self.balance + amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """Method to withdraw an amount from the account."""
        print(f"Withdrawing {amount} from the account.")
        if amount <= self.balance and amount > 0:
            self.balance = self.balance - amount
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.")
    
my_deposit = BankAccount(100)
my_deposit.deposit(100)
my_deposit.withdraw(50)
print(f'current balance is : {my_deposit.balance}')
