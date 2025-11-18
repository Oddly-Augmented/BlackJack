class Car:
    def __init__(self,make,year):
        self.make = make
        self.year = year
    def displayinfo(self):
        print(f"Make: {self.make}\nYear: {self.year}")

c = Car("Toyota",1999)
c.displayinfo()

class Book:
    def __init__(self, title, author,):
        self.title = title
        self.author = author
        
    def describe(self):
        print(f"Title: {self.title}\nBy: {self.author}")

b1 = Book("book","jones")
b1.describe()


class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def is_passing(self):
        if self.grade >= 60:
            return True
        else:
            return False
student_list = []

for _ in range(5):
    new_student = Student(input("Enter name:"), int(input("Enter Grade:")))
    student_list.append(new_student)

for student in student_list:
    if student.is_passing():
        print(student.name, "is Passing")
    else:
        print(student.name, "is failing")


        