# create a class called students
class Student:
    # create an object with value name and roll number
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def __del__(self):
        print("object is deleted")


# add a student to class
student_1 = Student("Shashank", 21104072)
# print the student name
print(student_1.name)
# delete the object
del student_1
