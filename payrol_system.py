# a python program to print out the payrolls of various employees in a company
class Employee:
    def __init__(self, name, id):
        self.name=name
        self.id=id

class SalaryEmployee(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary=salary

    def calculate_salary(self):
        return self.salary

class Comission_Employee(SalaryEmployee):

    def __init__(self, name, id, salary, sales, commission_rate):

        super().__init__(name, id, salary)
        self.commission_rate= commission_rate
        self.sales= sales

    def calculate_salary(self):

        return super().calculate_salary() + (self.sales * self.commission_rate)


class HourlyEmployee(Employee):
    def __init__(self, name, id, hours_worked, rate_per_hour):
        super().__init__(name, id,)
        self.hours_worked= hours_worked
        self.rate_per_hour= rate_per_hour

    def calculate_salary(self):
       return self.hours_worked * self.rate_per_hour


salary_employee= SalaryEmployee("Josphat Mwatha", "SE-04/122", 42000)
commission_employee= Comission_Employee("Tracy Robins", "CE-04/156", 35000, 250000 ,1.5)
hourly_employee= HourlyEmployee("Peter Mwiti", "HE-04/173", 150, 300)

print("\n")

print("** Salary Employee Earnings**")
print(salary_employee.name)
print(salary_employee.id)
print(salary_employee.salary, "\n")

print("**Commission Employee Salary**")
print(commission_employee.name)
print(commission_employee.id)
print(commission_employee.salary, "\n")

print("****Hourly Employee Salary**")
print(hourly_employee.name)
print(hourly_employee.id)
print(hourly_employee.calculate_salary())

