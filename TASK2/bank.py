class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

# List to store accounts
accounts = []
account_number_counter = 1000  # Auto-generate account numbers

while True:
    print("\n--Menu--")
    print("1. List Accounts")
    print("2. Create Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

    menu = input("Select menu: ")

    if menu == "1":
        if not accounts:
            print("No accounts available.")
        else:
            for index, account in enumerate(accounts):
                print(f"{index}: {account.owner}, Account No: {account.account_number}, Balance: ${account.balance}")

    elif menu == "2":
        name = input("Insert name: ")
        balance = int(input("Insert balance: "))
        accounts.append(BankAccount(name, account_number_counter, balance))
        print(f"Account created! Account Number: {account_number_counter}")
        account_number_counter += 1  # Increment for the next account

    elif menu == "3":
        index = int(input("Choose account index: "))
        if 0 <= index < len(accounts):  # Prevent index out of range error
            amount = int(input("Insert deposit amount: "))
            accounts[index].deposit(amount)
        else:
            print("Invalid account index!")

    elif menu == "4":
        index = int(input("Choose account index: "))
        if 0 <= index < len(accounts):  # Prevent index out of range error
            amount = int(input("Insert withdraw amount: "))
            accounts[index].withdraw(amount)
        else:
            print("Invalid account index!")

    elif menu == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid option! Please select a valid menu option.")
