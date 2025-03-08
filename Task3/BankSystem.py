class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Withdrawal amount exceeds account balance.")

    def display_account_details(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self.withdrawal_limit = 500

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print(f"Cannot withdraw more than ${self.withdrawal_limit} in a single transaction.")
        else:
            super().withdraw(amount)


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self.withdrawal_limit = 2000  # Higher withdrawal limit


# Testing the accounts
def main():
    # Create accounts
    basic_account = BankAccount("12345")
    savings_account = SavingsAccount("67890", 1000)
    premium_account = PremiumSavingsAccount("54321", 3000)

    # Display initial account details
    basic_account.display_account_details()
    savings_account.display_account_details()
    premium_account.display_account_details()

    # Test deposits
    basic_account.deposit(500)
    savings_account.deposit(300)
    premium_account.deposit(700)

    # Test withdrawals
    savings_account.withdraw(600)  # Should fail
    savings_account.withdraw(400)  # Should succeed

    premium_account.withdraw(2500)  # Should fail
    premium_account.withdraw(1500)  # Should succeed

    # Display final account details
    basic_account.display_account_details()
    savings_account.display_account_details()
    premium_account.display_account_details()


if __name__ == "__main__":
    main()