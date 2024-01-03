# Single Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("name",self.name, "Age:" ,self.age)

class Student(Person):
    def __init__(self, name, age, student_id):
        # Call constructor of the base class (Person)
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print("Student ID:", self.student_id)
#hierarchial inheritance
class Professor(Person):
    def __init__(self, name, age, employee_id):
        # Call constructor of the base class (Person)
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_info(self):
        super().display_info()
        print("Employee ID:", self.employee_id)

# Multiple Inheritance

class TA(Student, Professor):
    def __init__(self, name, age, student_id, employee_id, course):
        # Call constructors of both Student and Professor
        Student.__init__(self, name, age, student_id)
        Professor.__init__(self, name, age, employee_id)
        self.course = course

    def display_info(self):
        super(Student, self).display_info()  # Calling Student's display_info
        super(Professor, self).display_info()  # Calling Professor's display_info
        print(f"Teaching Assistant for: {self.course}")

# Multilevel Inheritance

class HeadofDept(Professor):
    def __init__(self, name, age, employee_id, department):
        # Call constructor of the base class (Professor)
        super().__init__(name, age, employee_id)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

# Creating instances and demonstrating inheritance

# Single Inheritance
student = Student("Alice", 20, "S12345")
student.display_info()

professor = Professor("Dr. Smith", 45, "P98765")
professor.display_info()

# Multiple Inheritance
ta = TA("Bob", 25, "S56789", "P54321", "Computer Science")
ta.display_info()

# Multilevel Inheritance
head_professor = HeadofDept("Prof. Johnson", 55, "P11111", "Mathematics")
head_professor.display_info()
