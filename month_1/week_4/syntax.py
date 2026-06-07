# squares = [x * x for x in range(5)]
# print(squares)

# dictionary = {x:x*x for x in range(5)}
# print(dictionary)


# even =[x for x in range(19) if x%2 == 0]
# print(even)


# a, b = [1, 2]

# print(a)
# print(b)


# first, *middle, last = [1, 2, 3, 4, 5]

# print(middle)


# def add(*args):
#     print(args)
#     return sum(args)

# def show(**kwargs):
#     print(kwargs)
    
# print(add(1, 2, 3, 4))
# show(name="Max", age=25)


# try:
#     x = 10 / 0

# except ZeroDivisionError:
#     print("Cannot divide by zero")
# finally:
#     print("Always runs")


# with open("file.txt") as file:
#     data = file.read()
#     print(data)
    
#


# file = open('file.txt')
# data = file.read()
# print(data)
# file.close()


# def count():
#     yield 1
#     yield 2
#     yield 3
    
    
# for x in count():
#     print(x)

# def logger(func):
#     def wrapper():
#         print("Function start from here ....")
#         func()
#         print("Function end from here ....")
#     return wrapper

# @logger

# def add(*arg):
#     return sum(arg)

# add = logger(add(1, 2, 3, 4))

# print(add(1, 2, 3, 4))


# def logger(func):
#     def wrapper():
#         print("Running")
#         func()
#     return wrapper

# @logger
# def hello():
#     print("Hello")
    

# hello = logger(hello)

# age = 20
# status= "Adult" if age >= 18 else "Minor"
# print(status)
#

# def add(a: int, b: int) -> int:
#     return a + b

# result = add("Hello ", "World")
# print(type(result))



# car = {
#     "brand": "Toyota",
#     "start": lambda: print("Engine started")
# }


# print(car["start"])
# class Vehicle:
#     def __init__(self, name):
#         self.name = name
#         print(f"Vehicle created: {name}")


# class Car(Vehicle):
#     def __init__(self, name):
#         super().__init__(name)
#         print(f"Car created: {name}")
#         pass
    
#     def start(self):
#         print("Engine started")
        
#     def race(self):
#         print(f"{self.name} Lets go to the race.")
        
        
# car = Car("Oddy")
# car.start()
# car.race()


# class User:
#     def __init__(self, age):
#         self.age = age
        
        
# u = User(25)

# print(u.age)


class User:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
        
        
        
u = User(25)

u.set_age(30)

print(u.get_age())