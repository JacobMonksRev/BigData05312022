class Employee:
    isHuman = True
    type_employee = 'Employee'
    def __init__(self, name, salary, dept):
        self.name = name
        self.salary = salary
        self.dept = dept
    def work(self):
        print(self.name, "is working.")

class Trainee(Employee):
    type_employee = 'Trainee'
    def work(self):
        print(self.name, "is watching a training video.")
            
class Manager(Employee):
    type_employee = 'Manager'
    def work(self):
        print(self.name, "is in a meeting.")

def main():
    emp1 = Employee('Bob', 60000, 'sales')
    emp2 = Employee('Cindy', 70000, 'HR')


    # You can create a child class using a predefined class
    # This is called 'inheritance'


    # A child class cna have the parent functions re-declared and do something different
    # This is called 'method overriding'

    man1 = Manager('Bill', 100000, 'sales')
    train1 = Trainee('Angela', 40000, 'marketing')