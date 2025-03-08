# Base class Employee
class Employee:
    def __init__(self, name, emp_id, salary):
        """Initialize Employee with name, ID, and base salary."""
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def calculate_salary(self):
        """Returns the base salary (to be overridden by subclasses)."""
        return self.salary  

    def show_details(self):
        """Displays employee details including calculated salary."""
        print(f"Employee ID: {self.emp_id}, Name: {self.name}, Salary: ${self.calculate_salary()}")

# Manager subclass inherits from Employee
class Manager(Employee):
    def calculate_salary(self):
        """Manager gets a 20% bonus on top of base salary."""
        return self.salary + (0.2 * self.salary)

# Engineer subclass inherits from Employee
class Engineer(Employee):
    def calculate_salary(self):
        """Engineer gets a 10% performance bonus on top of base salary."""
        return self.salary + (0.1 * self.salary)

# Intern subclass inherits from Employee
class Intern(Employee):
    def __init__(self, name, emp_id, stipend):
        """Interns have a fixed stipend instead of a base salary."""
        super().__init__(name, emp_id, stipend)

    def calculate_salary(self):
        """Interns only receive their stipend (no bonuses)."""
        return self.salary  

# Creating instances of different employees
manager = Manager("Alice Johnson", 101, 5000)   # Manager with base salary $5000
engineer = Engineer("Bob Smith", 102, 4000)     # Engineer with base salary $4000
intern = Intern("Charlie Brown", 103, 1000)     # Intern with fixed stipend $1000

# Displaying payroll details
print("\nEmployee Payroll Details:")
manager.show_details()
engineer.show_details()
intern.show_details()
