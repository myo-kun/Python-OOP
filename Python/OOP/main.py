from Python.OOP.Developer import Developer
from Python.OOP.Employee import Employee
from Python.OOP.Manager import Manager

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(dev_1.pay)

dev_1.apply_raise()
print(dev_1.pay)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.__repr__())
print(emp_1.__str__())

emp_1.fullname = 'John Smith'
print(emp_1.fullname)

del emp_1.fullname
