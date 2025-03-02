# base class (parent class)
class Employee:

    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def calculate_pay(self):
        return self.base_salary

    def get_role(self):
        return f"Hi, I'm {self.name} and work as a {self.employee_id}"


# sub_class inherits form "Employee" base class
class Manager(Employee):

    def __init__(self, name, employee_id, base_salary, bouns_percentage):
        super().__init__(name, employee_id, base_salary)
        self.bouns_percentage = bouns_percentage  # 10 for 10% bouns

# override the base class "calculate_pay" method
    def calculate_pay(self):
        bouns = self.base_salary * (self.bouns_percentage/12)
        return f"My salary is : ${round(self.base_salary + bouns)}"

# override the base class "get_role" method
    def get_role(self):
        return f"Hi, I'm {self.name} and work as a Manager.Employee ID :{self.employee_id}"

# sub_class inherits form "Employee" base class


class Developer(Employee):

    def __init__(self, name, employee_id, base_salary, overtime_hours,):
        super().__init__(name, employee_id, base_salary)
        self.overtime_hours = overtime_hours
        self.overtime_rate = 50  # $50 per overtime hour

# override the base class "calculate_pay" method
    def calculate_pay(self):
        overtime_pay = self.overtime_hours * self.overtime_rate
        return f"My salary is : ${self.base_salary + overtime_pay}"
# override the base class "get_role" method

    def get_role(self):
        return f"Hi, I'm {self.name} and work as a Web Developrer.Employee ID :{self.employee_id}"


manager = Manager("M Imran", "M001", 20000, 20)

print(manager.get_role())
print(manager.calculate_pay())
print(manager.name)
print(manager.employee_id)

developer_1 = Developer("M Nasir", "E005", 15000, 3)

print(developer_1.get_role())
print(developer_1.calculate_pay())
print(developer_1.name)
print(developer_1.employee_id)

developer_2 = Developer("M Salman", "E201", 12000, 5)

print(developer_2.get_role())
print(developer_2.calculate_pay())
print(developer_2.name)
print(developer_2.employee_id)
