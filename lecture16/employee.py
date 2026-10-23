class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value

    @salary.deleter
    def salary(self):
        del self.__salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_info(self):
        print(f"სახელი: {self.name}, განყოფილება: {self.department}, ხელფასი: {self.salary} ლარი")