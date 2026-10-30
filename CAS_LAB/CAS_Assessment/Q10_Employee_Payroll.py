# Q10: Employee Payroll System
# Concepts: OOP - Abstract Class, Inheritance, Polymorphism, Encapsulation
# Time Complexity: O(n)

from abc import ABC, abstractmethod

class Employee(ABC):
    """
    Abstract base class for all employees.
    Cannot be instantiated directly.
    Each subclass must implement calculate_bonus().
    """
    
    def __init__(self, emp_id, name, base_salary):
        """Constructor: initializes employee details."""
        self.__emp_id = emp_id           # Private attribute
        self.__name = name               # Private attribute
        self.__base_salary = base_salary # Private attribute
    
    def get_emp_id(self):
        """Getter for employee ID."""
        return self.__emp_id
    
    def get_name(self):
        """Getter for employee name."""
        return self.__name
    
    def get_base_salary(self):
        """Getter for base salary."""
        return self.__base_salary
    
    @abstractmethod
    def calculate_bonus(self):
        """
        Abstract method: must be implemented by each subclass.
        Returns the bonus amount based on employee type.
        """
        pass
    
    def calculate_final_salary(self):
        """Final salary = base salary + bonus."""
        return self.__base_salary + self.calculate_bonus()


class Developer(Employee):
    """Developer: 10% bonus on base salary."""
    
    def calculate_bonus(self):
        """Developer bonus = 10% of base salary."""
        return self.get_base_salary() * 0.10


class Manager(Employee):
    """Manager: 20% bonus on base salary."""
    
    def calculate_bonus(self):
        """Manager bonus = 20% of base salary."""
        return self.get_base_salary() * 0.20


class Intern(Employee):
    """Intern: 5% bonus on base salary."""
    
    def calculate_bonus(self):
        """Intern bonus = 5% of base salary."""
        return self.get_base_salary() * 0.05


# ---- Main Program ----
# Read number of employees
n = int(input())

# Dictionary to map type names to classes (avoids if-elif chain)
employee_classes = {
    "Developer": Developer,
    "Manager": Manager,
    "Intern": Intern
}

total_payroll = 0

for i in range(n):
    parts = input().split()
    emp_type = parts[0]
    emp_id = parts[1]
    name = parts[2]
    base_salary = float(parts[3])
    
    # Create employee object using polymorphism
    employee = employee_classes[emp_type](emp_id, name, base_salary)
    
    # Calculate bonus and final salary
    bonus = employee.calculate_bonus()
    final_salary = employee.calculate_final_salary()
    
    # Print employee details
    print(f"{emp_id} {int(bonus)} {int(final_salary)}")
    
    # Add to total payroll
    total_payroll += final_salary

# Print total payroll
print(f"TOTAL {int(total_payroll)}")
