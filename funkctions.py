import random


def greeting(name):
    print("Hello " + name)


greeting("mis")


def rollDice():
    number = random.randint(1, 6)
    return number


for i in range(10):
    print(rollDice())


class Emplyee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


class SalaryEmplyee(Emplyee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)  # wtedy
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary / 12


class HourlyEmplyee(Emplyee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)  # wtedy
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self):
        return self.hourly_rate * self.weekly_hours


class CommissionEmployee(SalaryEmplyee):
    def __init__(self, fname, lname, salary, sales_num, com_rate):
        super().__init__(fname, lname, salary)
        self.sales_num = sales_num
        self.com_rate = com_rate

    def calculate_paycheck(self):
        # return self.salary / 12 + self.sales_num * self.com_rate
        regular_salary = super().calculate_paycheck()
        comision = self.sales_num * self.com_rate
        return regular_salary + comision


print(SalaryEmplyee("mis", "koralgol", 1200))
print(SalaryEmplyee("mis", "koralgol", 1200).salary)
print(SalaryEmplyee("mis", "koralgol", 1200).calculate_paycheck())
