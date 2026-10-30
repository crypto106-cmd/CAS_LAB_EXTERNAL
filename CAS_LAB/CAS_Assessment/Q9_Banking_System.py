# Q9: Design a Banking Account System
# Concepts: OOP - Encapsulation, Inheritance, Polymorphism, Constructors
# Time Complexity: O(1) per operation

class BankAccount:
    """
    Base class for all bank accounts.
    Demonstrates encapsulation: balance is private (__balance).
    """
    
    def __init__(self, account_id, balance):
        """Constructor: initializes account with ID and balance."""
        self.__account_id = account_id     # Private attribute
        self.__balance = balance            # Private attribute (encapsulation)
    
    def get_balance(self):
        """Getter method to access private balance."""
        return self.__balance
    
    def get_account_id(self):
        """Getter method to access private account ID."""
        return self.__account_id
    
    def deposit(self, amount):
        """Deposit money into the account."""
        self.__balance += amount
    
    def withdraw(self, amount):
        """
        Withdraw money from the account.
        This method is overridden by subclasses to add specific rules.
        Returns True if withdrawal is successful, False otherwise.
        """
        self.__balance -= amount
        return True
    
    def _set_balance(self, new_balance):
        """Protected method to allow subclasses to modify balance."""
        self.__balance = new_balance


class SavingsAccount(BankAccount):
    """
    Savings account with a minimum balance requirement.
    Cannot withdraw if it would bring balance below minimum.
    """
    
    def __init__(self, account_id, balance, min_balance):
        """Constructor: calls parent constructor and sets minimum balance."""
        super().__init__(account_id, balance)
        self.__min_balance = min_balance
    
    def withdraw(self, amount):
        """
        Override: withdraw only if balance after withdrawal >= minimum balance.
        Returns True if successful, False otherwise.
        """
        if self.get_balance() - amount >= self.__min_balance:
            # Use parent's withdraw method
            super().withdraw(amount)
            return True
        else:
            return False


class CurrentAccount(BankAccount):
    """
    Current account with an overdraft limit.
    Can withdraw beyond zero up to the overdraft limit.
    """
    
    def __init__(self, account_id, balance, overdraft_limit):
        """Constructor: calls parent constructor and sets overdraft limit."""
        super().__init__(account_id, balance)
        self.__overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        """
        Override: withdraw allowed if balance after withdrawal >= -overdraft_limit.
        Returns True if successful, False otherwise.
        """
        if self.get_balance() - amount >= -self.__overdraft_limit:
            super().withdraw(amount)
            return True
        else:
            return False


# ---- Main Program ----
# Read account details
account_line = input().split()
account_type = account_line[0]
account_id = account_line[1]
initial_balance = float(account_line[2])
limit = float(account_line[3])

# Create the appropriate account object (polymorphism)
if account_type == "SavingsAccount":
    account = SavingsAccount(account_id, initial_balance, limit)
elif account_type == "CurrentAccount":
    account = CurrentAccount(account_id, initial_balance, limit)

# Process operations
import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split()
    operation = parts[0]
    
    if operation == "DEPOSIT":
        amount = float(parts[1])
        account.deposit(amount)
        print("SUCCESS")
    
    elif operation == "WITHDRAW":
        amount = float(parts[1])
        result = account.withdraw(amount)
        if result:
            print("SUCCESS")
        else:
            print("FAILURE")
    
    elif operation == "BALANCE":
        balance = account.get_balance()
        # Print as integer if it's a whole number
        if balance == int(balance):
            print(int(balance))
        else:
            print(balance)
