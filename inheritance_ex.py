class Person:  #base class Parent class
    def __init__(self, name, age , address):
        self.__name = name  # private
        self._age = age  # protected
        self.address = address  #public

    def display(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self._age}")
        print(f"Address: {self.address}")


class Employee(Person):  #derived class   child class
    def __init__(self, name, age, address, empid, salary, dept):
        super().__init__(name,age,address)
        self.empid = empid
        self.salary = salary
        self.dept = dept

    def display(self):
        super().display()
        print(f"Emp ID: {self.empid}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.dept}")

    def __repr__(self):
        return f"Employee of {self.empid}"

    def __str__(self):
        return f"Employee of {self.empid}"

# p = Person("Shree", 21, "Pune")
# p.display()

e = Employee("Shree", 21, "Pune",101, 24000,"Admin")
e.display()

print(e._Person__name)  # _className__variableName
print(e)