class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: ₹{amount:.2f}")
            print(f"₹{amount:.2f} deposited successfully.")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: ₹{amount:.2f}")
            print(f"₹{amount:.2f} withdrawn successfully.")

    def check_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance:.2f}")

    def show_transactions(self):
        print("\n--- Transaction History ---")

        if not self.transactions:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(transaction)


print("------------- SIMPLE BANKING SYSTEM ------------")

name = input("Enter your name: ")
account_number = input("Enter account number: ")

account = BankAccount(name, account_number)

while True:
    print("\n===== MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Account Details")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: ₹"))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: ₹"))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        account.show_transactions()

    elif choice == "5":
        print("\n--- Account Details ---")
        print("Name:", account.name)
        print("Account Number:", account.account_number)
        print(f"Balance: ₹{account.balance:.2f}")

    elif choice == "6":
        print("\nThank you for using our banking system!")
        break

    else:
        print("Invalid choice! Please try again.")