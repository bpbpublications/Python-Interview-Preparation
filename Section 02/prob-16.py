class BankAccount:
    def __init__(self, balance=0):
        # Initialize the bank account with an optional starting balance
        self.balance = balance
 
    def deposit(self, amount):
        # Adds the deposit amount to the balance
        if amount > 0:
            self.balance += amount
            return f"Successfully deposited {amount}."
        else:
            return "Deposit amount must be positive."
 
    def withdraw(self, amount):
        # Withdraws the amount if balance is sufficient, otherwise returns an error
        if amount > self.balance:
            return "Insufficient funds for this withdrawal."
        elif amount <= 0:
            return "Withdrawal amount must be positive."
        else:
            self.balance -= amount
            return f"Successfully withdrew {amount}."
 
    def get_balance(self):
        # Returns the current balance of the account
        return self.balance
