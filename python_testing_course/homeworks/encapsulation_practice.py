class BankAccount:
    def __init__(self):
        self.__balance = 0

    @property  # This is getter - get balance info.
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,new_balance):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = new_balance

    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount should be greater than 0")
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount cannot be zero or negative")
        
        if amount > self.balance:
            raise ValueError("Cannot withdraw more than available balance")
        
        self.balance -= amount

my_bank_acount = BankAccount()
my_bank_acount.deposit(100)
print(my_bank_acount.balance)
my_bank_acount.withdraw(50)
print(my_bank_acount.balance)


my_bank_acount.withdraw(50)
print(my_bank_acount.balance)

# my_bank_acount.deposit(0)
# print(my_bank_acount.balance)

#my_bank_acount.withdraw(-10)
#print(my_bank_acount.balance)

# my_bank_acount.withdraw(10)
# print(my_bank_acount.balance)
