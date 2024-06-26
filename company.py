from funkctions import Emplyee, SalaryEmplyee, HourlyEmplyee, CommissionEmployee


class Company:

    def __init__(self):
        self.employees = []

    def add_employe(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print("Current Employees: ")
        for i in self.employees:
            print(i.fname, " ", i.lname)

    def pay_empolyees(self):
        print("Paying Empolyees: ")
        for emp in self.employees:
            # print("Emp ", emp.lname, " will get. Amount: ", emp.calculate_paycheck())
            print(
                f"Emp  {emp.lname}   will get. Amount: {emp.calculate_paycheck():.2f}"
            )


def main():
    my_company = Company()

    employee1 = SalaryEmplyee("mis", "koralgol", 9200)
    my_company.add_employe(employee1)

    employee2 = SalaryEmplyee("mis2", "koralgo2", 93200)
    my_company.add_employe(employee2)

    employee3 = SalaryEmplyee("mis3", "koralgo3", 94200)
    my_company.add_employe(employee3)

    employee4 = HourlyEmplyee("mis3", "koralgo3", 11, 12)
    my_company.add_employe(employee4)

    employee4 = CommissionEmployee("mis6", "koralgo6", 2700, 11, 12)
    my_company.add_employe(employee4)

    my_company.display_employees()
    my_company.pay_empolyees()


main()

x = 12

try:
    print("test" + x)
except:
    print("cos nie tak")
