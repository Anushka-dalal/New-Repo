# hw task -> An employee has name, salary, and Phone. Phone means mobile number, email address.
# Employee has one operation which displays salary,email and name of employee.

class Employee:
    name = "Anushka"
    salary = 100000
    mob_no = 9130792524
    email = "anushkadalal80@gmail.com"

    def display():
        print(f"Name of Employee = {Employee.name}, Salary = {Employee.salary}, Email = {Employee.email}")
        
Employee.display()

