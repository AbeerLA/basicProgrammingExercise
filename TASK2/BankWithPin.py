class BankAccount:
    def __init__(self, owner, account_number, balance=0, pin=1234):
        self.account_holder = owner  # Public attribute
        self._balance = balance  # Protected attribute
        self.__pin = pin  # Private attribute
        self.account_number = account_number

    def get_balance(self):
        return self._balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative!")
    
    def verify_pin(self, pin):
        return pin == self.__pin

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.account_holder} deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount, pin):
        if self.verify_pin(pin):
            if 0 < amount <= self._balance:
                self._balance -= amount
                print(f"{self.account_holder} withdrew ${amount}. New balance: ${self._balance}")
            else:
                print("Invalid withdraw amount or insufficient funds!")
        else:
            print("Incorrect PIN!")

# Creating an account instance
account = BankAccount("John Doe", 1001, 500, 5678)

# Accessing the public attribute
print("Account Holder:", account.account_holder)

# Attempting to access the protected attribute
print("Balance (Accessing Protected Attribute):", account._balance)

# Attempting to access the private attribute (Will raise an error)
try:
    print("PIN (Trying to Access Private Attribute):", account.__pin)
except AttributeError:
    print("Cannot access private attribute __pin directly!")

# Using getter and setter methods
print("Balance (Using Getter Method):", account.get_balance())
account.set_balance(1000)  # Updating balance
print("Updated Balance (Using Setter Method):", account.get_balance())

# Verifying PIN
print("PIN Verification (Correct):", account.verify_pin(5678))
print("PIN Verification (Incorrect):", account.verify_pin(1234))

# Performing deposit and withdrawal operations
account.deposit(200)
account.withdraw(300, 5678)  # Correct PIN
account.withdraw(500, 1234)  # Incorrect PIN
