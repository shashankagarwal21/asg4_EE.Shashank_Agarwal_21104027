class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def __del__(self):
        print("object is deleted")


student_1 = Student("Shashank", 21104072)
print(student_1.name)
del student_1
