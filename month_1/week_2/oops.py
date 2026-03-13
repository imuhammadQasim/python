# class Employee:
    
#     def __init__(self, fname, lname, email, pay):
#         self.first_name= fname
#         self.last_name=lname
#         self.email=email
#         self.pay=pay

#     def greet(self):
#         return 'Good Morning ' + self.first_name

# emp_1 = Employee("Muhammad", "Qasim", 'mq@gmail.com', 50000)
# emp_2 = Employee("Yousaf", "Khan", "yousaf@gmail.com", 4000)

# print(emp_1.email)
# print(emp_1.greet())


class Student:
    def __init__(self, name , age , marks):
        self.name= name
        self.age = age
        self.marks = marks

    def dispkay_name(self):
        return 'The student '+ self.name + 'age is' + self.age
    
st1 = Student("Muhammad", 'ma@gmail.com' , 0)
print(st1.dispkay_name())
print(st1.name)
