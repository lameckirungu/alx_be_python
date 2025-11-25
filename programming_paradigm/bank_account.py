class BankAccount:
    """
    A Simple class to represent a bank account with deposit,
    withdraw, and display balance functionality.
    """
    def __init__(self, initial_balance=0.0):
        """Initializes the account balance. Defaults to 0.0 if no balance is provided."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Adds the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """Deducts the amount from the balance if funds are sufficient."""
        
        if amount <= self.account_balance and amount > 0:
            self.account_balance -= amount
            return True
        else:
            return False
    
    
    def display_balance(self):
        """Prints the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")