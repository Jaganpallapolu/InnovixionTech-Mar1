class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def display_balance(self):
        print(f"Account Balance for {self.account_holder}: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} into {self.account_holder}'s account.")
            self.display_balance()
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw ${amount:.2f} from {self.account_holder}'s accouunt.")
            self.display_balance()
        else:
            print("Invalid withdrawl amount or insufficient funds.")


if __name__ == "__main__":
    account_holder = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance(if any): "))
    account = BankAccount(account_holder, initial_balance)
    while True:
        print("\nOptions:")
        print("1. Check Balance ")
        print("2. Make a Deposit")
        print("3. Make a Withdrawl")
        print("4.Exit")
        choice = input("Enter your choice(1-4): ")
        if choice == '1':
            account.display_balance()
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 4.")


