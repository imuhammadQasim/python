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


# class Student:
#     def __init__(self, name , age , marks):
#         self.name= name
#         self.age = age
#         self.marks = marks

#     def dispkay_name(self):
#         return 'The student '+ self.name + 'age is' + self.age
    
# st1 = Student("Muhammad", 'ma@gmail.com' , 0)
# print(st1.dispkay_name())
# print(st1.name)


# class Person:
#     species = "Human"

#     def __init__(self, name):
#         self.name = name

#     @classmethod
#     def get_species(cls):
#         return cls.species


# print(Person.get_species())


# class Person:

#     @staticmethod
#     def static_method():
#         print("This is a static method")

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_year(cls, name, year):
#         age = 2026 - year
#         return cls(name, age)

# p = Person.from_birth_year("Max", 2000)
# p.static_method()


# class MathUtils:

#     @staticmethod
#     def add(a, b):
#         return a + b


# print(MathUtils.add(5, 3))


# def binarySearch(arr, target):
#     left = 0
#     right = len(arr)-1
#     while (left <= right):
#         mid = (left + right)//2
#         print('left',left, 'right',  right)
#         if target == arr[mid]:
#             return mid
#         if target > arr[mid] :
#             left = mid + 1
#         else:
#             right = mid -1
#     return "Target not found in the array"


# arr =[1,2,3,4,5,6,7]
# print(binarySearch(arr, 7))


# def linearSearch(arr, target):
#     print(len(arr))
#     for x in range(len(arr)):
#         print("x",arr[x])
#         if arr[x]==target:
#             return x
#     return "Not FOund"


# arr =[1,2,3,4,5,6,7]
# # print(linearSearch(arr, 7))
# from datetime import datetime , date
# class Car:
#     def __init__(self, brand, model , year):
#         self.brand= brand
#         self.model = model
#         self.year = year
    
#     def display_info(self):
#         return f"The Car {self.brand} is {self.model} and year is {self.year}"
    
# car1 = Car('Oddy', 'ETRON-GT', 2022)
# car2 = Car('Honda', 'ETRON-GT', 2022)

# print(car1.display_info())
# class Student:
#     current_year = date.today().year
#     # year = current_date
#     def __init__(self, name, age , grade):
#         self.name= name
#         self.age = age
#         self.grade = grade
    
#     def introduce(self):
#         return f"The Name os the Studentis {self.name} is {self.age} and year is {self.grade}"
#     def calculateDateOfBirth(self):
#         return self.current_year -self.age
# stu1 = Student('Muhammad', 22, 'A')
# stu2 = Student('Yousaf', 23, 'A')

# print(stu2.introduce())
# print('The date of birth which is derived form the age is : ',stu1.calculateDateOfBirth())


# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         if amount <= 0 :
#             return "Please enter the amount greater than zero"
#         self.balance = self.balance + amount
#         return f"You have successfully deposit the {amount} amount"
    
#     def withdraw(self, amount):
#         if amount > self.balance :
#             return "Insufficient funds to withdraw amount"
#         self.balance = self.balance - amount
#         return f"You have successfully withdraw the {amount} amount"
    
#     def show_balance(self):
#         return print(f"Your current balance is {self.balance}")

# acc1 = BankAccount("Muhammad", 1000)

# print(acc1.deposit(-500))
# print(acc1.withdraw(7000))
# acc1.show_balance()


# class Student:
#     school_name = "ABC School"

#     def __init__(self, name):
#         self.name = name

#     @classmethod
#     def change_school(cls, new_name):
#         cls.school_name = new_name



# s1 = Student("Ali")
# print(s1.school_name)
# Student.change_school("Superior College")


# class MathUtils:

#     @staticmethod
#     def add(a, b):
#         return a + b

# m = MathUtils()

# # print(MathUtils.add(5, 3))
# print(m.add(5, 3))


# class Employee:

#     company_name = "Google"

#     @staticmethod
#     def isvalid_salary(salary):
#         return salary > 0

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     @classmethod
#     def change_company(cls, new_name):
#         cls.company_name = new_name

# e = Employee('Muhammad' , '100k')
# # Employee.company_name = 'Meta'
# e.change_company('Meta')
# print(e.isvalid_salary(100))
# print(e.company_name)

# class BankAccount:

#     def __init__(self, balance):
#         self._balance = balance

#     def get_balance(self):
#         return self._balance

#     def set_balance(self, amount):
#         if amount < 0:
#             print("Balance cannot be negative")
#         else:
#             self._balance = amount


# acc = BankAccount(1000)

# print(acc.get_balance())

# acc.set_balance(2000)


# print(acc.get_balance())
# acc._balance = -10000
# print(acc._balance)


# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance


# acc = BankAccount(1000)

# print(acc.__dict__)


# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         return print(f"{self.name} makes a sound")
    
# class Dog(Animal):
#     def bark(self):
#         return print(f"{self.name} barks loudly.")
    

# d = Dog("Tommy")
# d.speak()
# d.bark()


# class Flyer:
#     def fly(slef):
#         return print("I can fly")
# class Swimmer:
#     def swim(slef):
#         return print("I can swimmer")
# class Duck(Flyer, Swimmer):
#     def qauck(slef):
#         return print("Quack quack!")
    
# donald = Duck()

# donald.fly()
# donald.swim()
# donald.qauck()


# class A:
#     def show(self):
#         print("A show")

# class B:
#     def show(self):
#         print("B show")

# class C(A, B):
#     pass

# obj = C()
# obj.show()  # Output: "A show"  -> follows MRO: C -> A -> B



# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         return print(f"{self.name} makes a sound")
# class Mammal(Animal):    
#     def walk(self):
#         return print(f"{self.name} Can walk 100km in a day.")
    
# class Dog(Mammal):
#     def bark(self):
#         return print(f"{self.name} barks loudly.")
    

# d = Dog("Tommy")
# d.speak()
# d.walk()
# d.bark()



# class Vehicle:
#     def start(self):
#         print("Vehicle started")

# class Car(Vehicle):   # Car inherits from Vehicle
#     def wheels(self):
#         print("Car has 4 wheels")

# class Bike(Vehicle):  # Bike inherits from Vehicle
#     def wheels(self):
#         print("Bike has 2 wheels")


# # Usage
# car1 = Car()
# bike1 = Bike()

# car1.start()   # from Vehicle
# car1.wheels()  # from Car

# bike1.start()  # from Vehicle
# bike1.wheels() # from Bike


# class Animal:
#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):
#     def sound(self):
#         print("Bark")


# d = Dog()

# d.sound()

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"  # For users

    def __repr__(self):
        return f"Car('{self.brand}', '{self.model}')"  # For developers

car = Car("Audi", "R8")

print(car)       # Calls __str__
print(repr(car)) # Calls __repr__