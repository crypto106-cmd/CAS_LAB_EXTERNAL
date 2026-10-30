# Q9: Design a Banking Account System — Complete Explanation

---

## A. Understanding the Problem

### What is the question asking?
Design an **object-oriented banking system** with:
- A **BankAccount** base class.
- **SavingsAccount** subclass: enforces a minimum balance (cannot withdraw below it).
- **CurrentAccount** subclass: allows overdraft up to a limit (balance can go negative).
- Support **deposit**, **withdraw**, and **balance retrieval** operations.

### What are the OOP concepts required?
- **Encapsulation**: Balance is private, accessed only through methods.
- **Inheritance**: SavingsAccount and CurrentAccount inherit from BankAccount.
- **Constructors**: `__init__` methods to initialize accounts.
- **Method Overriding**: Each subclass overrides `withdraw()` with its own rules.
- **Polymorphism**: The same `withdraw()` call behaves differently for different account types.

### What input do we receive?
- First line: account type, account ID, initial balance, account-specific limit.
- Following lines: operations (WITHDRAW amount, DEPOSIT amount, BALANCE).

### What output do we produce?
- For each transaction: SUCCESS or FAILURE.
- For BALANCE: the current balance.

### Small Example
```
SavingsAccount S101 5000 1000
- Min balance = 1000
- WITHDRAW 3500: balance would be 1500 ≥ 1000 → SUCCESS
- BALANCE: 1500

CurrentAccount C201 1000 500
- Overdraft limit = 500
- WITHDRAW 1300: balance would be -300 ≥ -500 → SUCCESS
- BALANCE: -300
```

---

## B. Algorithm and Approach

### Approach: OOP Class Hierarchy

1. **BankAccount (Base Class)**:
   - Private `__balance` and `__account_id`.
   - Methods: `deposit()`, `withdraw()`, `get_balance()`.
   
2. **SavingsAccount (Child)**:
   - Adds `__min_balance`.
   - Overrides `withdraw()`: rejects if `balance - amount < min_balance`.
   
3. **CurrentAccount (Child)**:
   - Adds `__overdraft_limit`.
   - Overrides `withdraw()`: allows `balance - amount ≥ -overdraft_limit`.

4. **Main program**:
   - Read account type and create the appropriate object.
   - Process operations using the object's methods.

---

## C. Complete Python Code

```python
class BankAccount:
    def __init__(self, account_id, balance):
        self.__account_id = account_id
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def get_account_id(self):
        return self.__account_id
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        self.__balance -= amount
        return True
    
    def _set_balance(self, new_balance):
        self.__balance = new_balance


class SavingsAccount(BankAccount):
    def __init__(self, account_id, balance, min_balance):
        super().__init__(account_id, balance)
        self.__min_balance = min_balance
    
    def withdraw(self, amount):
        if self.get_balance() - amount >= self.__min_balance:
            super().withdraw(amount)
            return True
        else:
            return False


class CurrentAccount(BankAccount):
    def __init__(self, account_id, balance, overdraft_limit):
        super().__init__(account_id, balance)
        self.__overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if self.get_balance() - amount >= -self.__overdraft_limit:
            super().withdraw(amount)
            return True
        else:
            return False


import sys

account_line = input().split()
account_type = account_line[0]
account_id = account_line[1]
initial_balance = float(account_line[2])
limit = float(account_line[3])

if account_type == "SavingsAccount":
    account = SavingsAccount(account_id, initial_balance, limit)
elif account_type == "CurrentAccount":
    account = CurrentAccount(account_id, initial_balance, limit)

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
        if balance == int(balance):
            print(int(balance))
        else:
            print(balance)
```

---

## D. Public Test Cases

### Test Case 1
**Input:**
```
SavingsAccount S101 5000 1000
WITHDRAW 3500
BALANCE
```
**Expected Output:**
```
SUCCESS
1500
```
**Explanation:**
- Created SavingsAccount with balance 5000 and minimum balance 1000.
- WITHDRAW 3500: balance after = 5000 - 3500 = 1500 ≥ 1000 (min balance) → SUCCESS.
- BALANCE: current balance = 1500.

### Test Case 2
**Input:**
```
CurrentAccount C201 1000 500
WITHDRAW 1300
BALANCE
```
**Expected Output:**
```
SUCCESS
-300
```
**Explanation:**
- Created CurrentAccount with balance 1000 and overdraft limit 500.
- WITHDRAW 1300: balance after = 1000 - 1300 = -300 ≥ -500 (overdraft limit) → SUCCESS.
- BALANCE: current balance = -300.

---

## E. Detailed Code Explanation

### Line: `class BankAccount:`
- Defines the base class for all bank accounts.
- Contains common attributes (account_id, balance) and methods (deposit, withdraw, get_balance).

### Line: `self.__balance = balance`
- The double underscore `__` makes the attribute **private** (name mangling).
- Cannot be accessed directly from outside the class or subclasses.
- Must use getter/setter methods — this is **encapsulation**.

### Line: `def get_balance(self):`
- A **getter** method that provides controlled access to the private `__balance`.
- Subclasses use this to check the balance before withdrawing.

### Line: `class SavingsAccount(BankAccount):`
- **Inheritance**: SavingsAccount inherits from BankAccount.
- It gets all methods and attributes of BankAccount.
- The `(BankAccount)` part specifies the parent class.

### Line: `super().__init__(account_id, balance)`
- Calls the **parent class constructor**.
- `super()` refers to the parent class (BankAccount).
- Initializes the account_id and balance using the parent's `__init__`.

### Line: `def withdraw(self, amount):` (in SavingsAccount)
- **Method overriding**: This replaces the parent's withdraw method.
- Adds a check: `balance - amount >= min_balance`.
- If valid, calls `super().withdraw(amount)` to actually deduct the money.

### Line: `if self.get_balance() - amount >= -self.__overdraft_limit:`
- CurrentAccount allows negative balance.
- Check: remaining balance ≥ negative of overdraft limit.
- Example: balance=1000, amount=1300, limit=500 → -300 ≥ -500 → True.

### Lines: Input processing with `sys.stdin`
```python
for line in sys.stdin:
```
- Reads all remaining lines from standard input.
- Allows processing an unknown number of operations.
- Stops when input ends (Ctrl+Z on Windows, Ctrl+D on Linux/Mac).

---

## F. Python Syntax Explanation

### `class` and `__init__`
- `class` defines a blueprint for objects.
- `__init__` is the constructor — called automatically when creating an object.
- `self` refers to the current object instance.

### Private Attributes (`__`)
- `self.__balance` uses **name mangling** to make the attribute private.
- Cannot be accessed as `obj.__balance` from outside the class.
- Python changes it internally to `_ClassName__balance`.
- This enforces **encapsulation**.

### `super()`
- Returns a proxy object that refers to the parent class.
- `super().__init__(...)` calls the parent's constructor.
- `super().withdraw(...)` calls the parent's withdraw method.
- Used to reuse parent class functionality without repeating code.

### Inheritance
- `class SavingsAccount(BankAccount):` means SavingsAccount is a child of BankAccount.
- The child inherits all methods and attributes of the parent.
- The child can override methods to change behavior.

### Method Overriding
- When a child class defines a method with the same name as the parent, the child's version is used.
- `SavingsAccount.withdraw()` overrides `BankAccount.withdraw()`.
- This is how **polymorphism** works.

### `sys.stdin`
- `sys.stdin` is the standard input stream.
- `for line in sys.stdin:` reads lines until EOF.
- Works well for reading an unknown number of operations.

---

## G. Why This Method and Not Another Method?

### Why OOP?
- The problem explicitly requires OOP concepts (encapsulation, inheritance, polymorphism).
- A class hierarchy naturally models different account types.
- Adding new account types (e.g., FixedDeposit) only requires creating a new subclass.

### Why Private Attributes?
- **Encapsulation** ensures the balance can only be modified through deposit/withdraw methods.
- Prevents accidental direct modification (e.g., `account.balance = 999999`).
- The PDF explicitly says "Do not directly manipulate internal balance fields."

### Alternative 1: Dictionary-based approach
- Store accounts as dictionaries with type, balance, and limit.
- Use if-elif chains to determine withdrawal rules.
- **Rejected** because it doesn't demonstrate OOP concepts required by the PDF.

### Alternative 2: Single class with type field
- One class with a `type` attribute and if-elif in withdraw.
- **Rejected** because it doesn't demonstrate inheritance or polymorphism.

### Advantages of Our Approach:
- Clean class hierarchy with proper inheritance.
- Encapsulation protects data integrity.
- Polymorphism — the same `account.withdraw()` call works differently based on the actual type.
- Easy to extend with new account types.

---

## H. Time and Space Complexity

### Time Complexity: O(1) per operation
- Deposit: O(1) — just adds to balance.
- Withdraw: O(1) — checks condition and subtracts.
- Balance: O(1) — returns the stored value.
- No loops or recursion in any operation.

### Space Complexity: O(1)
- Each account object stores a constant number of attributes (id, balance, limit).
- No additional data structures are needed.

---

## I. Faculty Viva Questions and Answers

### Q1: What is encapsulation?
**A:** Encapsulation is bundling data (attributes) and methods that operate on that data within a class, and restricting direct access to internal data. In our code, `__balance` is private and can only be accessed through `get_balance()`.

### Q2: What is inheritance?
**A:** Inheritance allows a child class to inherit attributes and methods from a parent class. `SavingsAccount` inherits from `BankAccount`, so it gets `deposit()`, `get_balance()`, etc., without rewriting them.

### Q3: What is polymorphism?
**A:** Polymorphism means the same method call produces different behavior depending on the object type. `account.withdraw(100)` checks minimum balance for SavingsAccount but checks overdraft for CurrentAccount.

### Q4: What is method overriding?
**A:** When a child class defines a method with the same name as the parent, the child's version replaces it. `SavingsAccount.withdraw()` overrides `BankAccount.withdraw()` to add the minimum balance check.

### Q5: What does `super()` do?
**A:** `super()` gives access to the parent class. `super().__init__(...)` calls the parent's constructor. `super().withdraw(...)` calls the parent's withdraw method. It allows code reuse.

### Q6: What is name mangling in Python?
**A:** When an attribute starts with double underscore (`__balance`), Python internally renames it to `_ClassName__balance`. This makes it harder to access from outside, implementing privacy.

### Q7: Why not make balance a public attribute?
**A:** The problem says "do not directly manipulate internal balance fields." Public attributes can be changed by anyone (`account.balance = 999999`), breaking the withdrawal rules. Private attributes + methods enforce controlled access.

### Q8: How would you add a new account type?
**A:** Create a new subclass of BankAccount, override `withdraw()` with the new rules, and add the new type to the if-elif in the main program. No changes to existing classes needed. This is the **Open-Closed Principle**.

### Q9: What is the difference between `self` and `super()`?
**A:** `self` refers to the current object instance (used to access its own attributes/methods). `super()` refers to the parent class (used to access inherited or overridden methods).

### Q10: What is a constructor?
**A:** A constructor (`__init__`) is a special method that runs automatically when an object is created. It initializes the object's attributes. `BankAccount("S101", 5000)` triggers `__init__`.

### Q11: Can SavingsAccount access `__balance` directly?
**A:** No, because `__balance` is private to `BankAccount` (name mangling). SavingsAccount must use `self.get_balance()` to read it and `super().withdraw()` to modify it. This enforces encapsulation even between parent and child.

### Q12: What is the difference between SavingsAccount and CurrentAccount?
**A:** SavingsAccount enforces a minimum balance — you can never go below it. CurrentAccount allows overdraft — your balance can go negative up to the overdraft limit. Both inherit from BankAccount but override `withdraw()` differently.

---

## J. VS Code Execution

### Step-by-Step:
1. Open VS Code → open `Q9_Banking_System.py`.
2. Open terminal.
3. Run: `python Q9_Banking_System.py`
4. Type the input line by line.
5. After the last operation, press **Ctrl+Z** then **Enter** (Windows) to signal end of input.

### Terminal Example — Test Case 1:
```
PS C:\...\CAS_Assessment> python Q9_Banking_System.py
SavingsAccount S101 5000 1000
WITHDRAW 3500
BALANCE
SUCCESS
1500
```
(Press Ctrl+Z, then Enter to finish)

### Terminal Example — Test Case 2:
```
PS C:\...\CAS_Assessment> python Q9_Banking_System.py
CurrentAccount C201 1000 500
WITHDRAW 1300
BALANCE
SUCCESS
-300
```

---

## K. Quick Revision

| Item | Details |
|------|---------|
| **Concepts** | OOP: Encapsulation, Inheritance, Polymorphism, Constructors |
| **Data Structure** | Class hierarchy (BankAccount → SavingsAccount, CurrentAccount) |
| **Core Logic** | 1. Base class handles deposit/balance. 2. SavingsAccount checks minimum balance. 3. CurrentAccount checks overdraft limit. 4. Both override withdraw(). |
| **Memory Trick** | "Private balance, super() to parent, override withdraw for rules" |
| **One Sentence** | A class hierarchy where BankAccount provides core functionality while SavingsAccount and CurrentAccount override withdraw() with their own balance constraints. |
