class Student:

    # class level attributes
    collage = "GDC Lahore"
    number_of_students = 2000

# constructor or instence level attributes
    def __init__(self, name):
        self.name = name

# class level methods
    @classmethod
    def principle_name(cls):
        cls.number_of_students += 100
        return "GDC Lahore Principle is Zerwali shah."

# instence level methods
    def greeting(self):
        self.number_of_students -= 100
        return f"Hi {self.name}, Welcom to Pakistan :). "


# class methods can access only class level attributes while instence level can access both the class and instence level attributes.


print(Student.collage)
print(Student.principle_name())

student_1 = Student("M Imran")
print(student_1.greeting())
print(student_1.collage)

student_2 = Student("M Nasir")
print(student_2.greeting())
print(student_2.principle_name())

# it print 2000 because it's incresed twice in class level method (principle_name()) and decresed twice in instence level method (greeting())
print(student_1.number_of_students)
