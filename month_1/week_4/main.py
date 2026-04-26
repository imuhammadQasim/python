# def double(n):
#     return n*2

# def add(n):
#     return n+10

# def square(n):
#     return n*n

# def process_callbacks(num , *callback):
#     result = num
#     for cb in callback:
#         result = cb(result)
#     return result

# print(process_callbacks(2, double, add, square))
        
    
# def add(a, b):
#     return a+b

# sum = lambda a,b: a+b

# print(add(2,3))
# print(sum(2,3))


# nums = 9

# result = lambda x: x*2 if x > 10 else x+5 if x < 5 else x-1
# print(result(nums))


# class User:
#     count = 0
    
#     def __init__(self, name):
#         self.name = name
#         User.count += 1
        
#     def greet(self):
#         return f"Hello {self.name}"
    
#     @classmethod
#     def totalUser(cls):
#         return cls.count


# u1 = User("Max")
# u2 = User("Ali")

# print(u1.greet())   # Hello Max
# print(u2.greet())   # Hello Ali

# print(User.totalUser())  # 


# class Student:
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         Student.count +=1
    
#     def introduce(self):
#         return f"I am {self.name}"
    
#     @classmethod
#     def totalStudent(cls):
#         return cls.count
    
# a = Student('Muhammad')
# b = Student('Umair')

# print(a.introduce())
# print(a.totalStudent())


# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         return f"{self.name} Animal Speak"
    
#     def play(self):
#         return f"{self.name} play"
    

# class Dog(Animal):
#     pass
#     def speak(self):
#         return super().speak() + f" {self.name} Bark"

# d = Dog('German')
# print(d.speak())
# print(d.play())


# class A:
#     def show(self):
#         return "A"

# class B:
#     def show(self):
#         return "B"

# class C(A, B):
#     pass

# obj = C()
# print(obj.show())

# class User:
#     def __init__(self, name):
#         self.name = name
        
# class Student(User):
#     def __init__(self, name, age, gender):
#         super().__init__(name)
#         self.age = age
#         self.gender = gender
    
#     def intro(self):
#         return f"My name is {self.name}, age is {self.age}, gender is {self.gender}"
        

# s = Student('Ali', 12, 'Male')

# print(s.intro())


# class A:
#     def show(self):
#         return "A"

# class B:
#     def show(self):
#         return "B"
# class D:
#     def show(self):
#         return "D"

# class C(D, A, B):
#     pass

# obj = C()
# print(obj.show())
# print(C.mro())


# class BankAccount:
    
#     def __init__(self, balance):
#         self.__balance= balance
        
#     def get_balance(self):
#         return self.__balance
    
#     def add_balance(self, amount):
#         if amount < 0:
#             return "Amount should be postive"
#         self.__balance= self.__balance + amount
#         return f"{amount} is credit to your bank account. now total amount is {self.__balance}"
    
    
# a = BankAccount(200)
# print(a.get_balance())
# print(a.add_balance(100))


# class MyClass:
#     def __new__(cls):
#         print("1. __new__ called")
#         return super().__new__(cls)

#     def __init__(self):
#         print("2. __init__ called")

# a = MyClass()



# class User:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"User: {self.name}"

# u = User("Max")
# print(u)

# class User:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"DEBUG: User({self.name})"

# u = User("Max")
# print(u)


# def decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")
#     return wrapper


# def hello():
#     print("Hello Max")

# hello = decorator(hello)

# hello()


# try:
#     x = 10/2
#     print("Result:", x)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# else:
#     print("No error occurred")
# finally:
#      print("Execution finished")
    
    
# class Iterator:
#     def __init__(self):
#         self.num = 0
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         self.num +=1
#         if self.num > 2:
#             raise StopIteration
#         return self.num
    
# a = Iterator()
# print(next(a))
# print(next(a))
# print(next(a))


# def gen():
#     yield 1
#     yield "Qasim"
#     yield 3

# g = gen()
# print(next(g))
# print(next(g))
# print(next(g))


# def numbers():
#     for i in range(3):
#         yield i

# for num in numbers():
#     print(num)

# def read_large_file(file_path):
#     with open(file_path, "r") as f:
#         for line in f:
#             yield line


# l = read_large_file("main.py")
# print(l)


# squares = [x * x for x in range(5) if x%2==0]
# print(squares)

# dictionary = {x: x*x for x in range(5)}
# print(dictionary)

# unique = {len(word) for word in ["apple", "cat", "banana"]}
# print(unique)
# result = [x * y for x in range(10) for y in range(10) if x % 2 == 0 and y % 3 == 0]
# print(result)

