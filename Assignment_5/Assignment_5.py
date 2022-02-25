# create a class called employee with s no, name and salary as value
class Employee:
    def __init__(self, s_no, name, salary):
        self.s_no = s_no
        self.name = name
        self.salary = salary

    # function to update salary of employee
    def salary_update(self, new_salary):
        self.salary = new_salary
        print("salary of " + self.name + " has been updated")

    def __del__(self):
        print("Employee " + self.name + " is deleted")


# create 3 object with name and salary of employee
employee_1 = Employee(1, "Mehak", 40000)
employee_2 = Employee(2, "Ashok", 50000)
employee_3 = Employee(3, "Viren", 60000)

# delete the employee Viren
del employee_3

# update salary of Mehak
employee_1.salary_update(7000)
