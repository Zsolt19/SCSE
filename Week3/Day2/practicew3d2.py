class Student:
    def __init__(self, name, age, grade, height):
        self.name=name
        self.age=age
        self.grade=grade
        self.height=height
    def __str__(self):
        return f"Student name: {self.name}, Age:{self.age}, Grade: {self.grade}, Height: {self.height}"

new_student=Student("Calum",20,"A",165)
old_student=Student("Dan",18,"A",164)
print(new_student.name)
print(old_student.grade)
print(new_student)