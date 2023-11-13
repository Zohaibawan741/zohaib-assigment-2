class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee Details:")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")
        print()

# Creating instances of the Employee class
employee1 = Employee(name="ali", employee_id="E12345", salary=50000)
employee2 = Employee(name="zohaib", employee_id="E67890", salary=60000)

# Displaying employee details
employee1.display_details()
employee2.display_details()

