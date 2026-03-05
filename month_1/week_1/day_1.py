# message = 'Hello Wolrd'
# message.replace('Hello', 'Yellow')
# print(len(message))
# print(message[2:])
# print(message.upper())

# pra = '''Here is the long 
# paragraph which is written by MQ'''

# name = 'Muhammad'
# greet= 'Good Morning'
# msg = f'{greet}  {name.upper()}! Thank you'
# print(msg)

# print(help(str.capitalize))
# print(dir(int))

# print(3//2)
# print(3/2)

# print(3 !='3')

l = [1,2,2,33.4, "Muhammad"]

# print(type(l))
# print(dir(list))

# l.append([1,2])
# l.extend([1,2])
# l.insert(1,2)
# print(l.remove(2))
# print(l)
# l.pop(0)
# print(l.count(2))


# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# fruits.count('apple')

# fruits.count('tangerine')

# fruits.index('banana')

# fruits.index('banana', 4)  # Find next banana starting at position 4

# fruits.reverse()
# fruits

# fruits.append('grape')
# fruits

# fruits.sort()
# fruits

# fruits.pop()



# Using Lists as Queues


# from collections import deque

# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")           # Terry arrives
# queue.append("Graham")          # Graham arrives
# queue.popleft()                 # The first to arrive now leaves

# queue.popleft()                 # The second to arrive now leaves

# print(queue)                           # Remaining queue in order of arrival


# l = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# squares = list(map(lambda x: x**2, range(10)))
# print(squares)

# l = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# result = list(map(lambda x: x/2,l))

# print(result)


# combs= []

# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x!=y:
#             combs.append((x, y))

# print(combs)


# vec = [-4, -2, 0, 2, 4]
# v = [ x*2 for x in vec]

# v = [abs(x*2) for x in vec ]
# print(v)

# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']

# n = [w.strip() for w in freshfruit]
# print(freshfruit)
# print(n)


# vec = [-4, -2, 0, 2, 4]
# v = [(x, x*2) for x in vec]
# print(v)

# vec = [[1,2,3], [4,5,6], [7,8,9]]
# v = [num for elem in vec for num in elem]
# print(v)


# from math import pi

# print([(str(round(pi,i))) for i in range (6)])


# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# # print([n for elem in matrix for n in elem])
# n = []

# for i in range(4):
#     temp=[]
#     for row in matrix:
#         temp.append(row[i])
#     n.append(temp)

# print(n)


# matrix = [
#     [1, 2, 3, 4],    # Row 0
#     [5, 6, 7, 8],    # Row 1
#     [9,10,11,12],    # Row 2
# ]

# transposed = []

# for i in range(4):         # Outer loop -> column index
#     column = []
#     print(f"\nStarting outer loop i={i} (column index)")
#     for row in matrix:      # Inner loop -> iterate rows
#         print(f"  row={row}, row[{i}]={row[i]}")
#         column.append(row[i])
#     print(f"  Column {i} completed: {column}")
#     transposed.append(column)

# print("\nFinal transposed matrix:")
# print(transposed)


# for n in range(1,6):
#     for l in "Qasim":
#         print(n, l)


# def isPalindrome(s):
#     l = 0
#     r= len(s)-1
#     while(l<=r):
#         print("l and r ", l, r)
#         if s[l] !=s[r]:
#             return "Not Palindrom"
#         l+=1
#         r-=1
#     return "Palindrome"

# print(isPalindrome("riir"))


# for x in range(1,6):
#     for y in range(1,x):
#         print(x*y, end=" ")
#     print()


# my_list = [1,2,3]
# my_tuple = (1,2,3)

# t = 10, 20, 30

# print(type(t))

# tuple = (5,)
# # print(type(tuple))
# print(tuple[0])

# t = (10,20,20,30,40)

# a=t[0]
# print(t.count(20))
# print(t[-2:])



# t = (1,2,(3,4,5))

# print(t[2])
# print(t[2][1])

# t = (1,2,3)

# l = list(t)
# print(l.pop())
# print(l)


# def get_user():
#     return ("Qasim", 25, "Pakistan")
# a = get_user()
# print(get_user()[0])


# newTuple = (5, 10, 15, 20)

# print(newTuple.index(20))


# t = ("Ali", 22, "Lahore")
# a,b,c =t
# print(a,b,c)

# t = (10,20,30,40)
# a = list(t)

# print(a)


# numbers = (12, 45, 7, 89, 23)

# max = numbers[0]
# for x in numbers:
#     if max <= x:
#         max=x

# print(max)  



# product = ("Laptop", 80000, 2)
# def display(prod):
#     name, price ,quantity = prod
#     totalPrice= price* quantity
#     print("Product: ", name)
#     print("Total_Price: ", totalPrice)
# display(product)


# import my_module as mm
# import sys
# course = ["a", "b", "c", "d"]

# # mm.search_index(course, "x")

# print(sys.path)


# import math

# print(math.pow(16,2))

# import random

# print(random.randint(1,10))

# import datetime

# today = datetime.datetime.now()

# print(today)


# import os

# print(dir(os)))
# os.makedirs("folder1/folder2/folder3")
# os.removedirs("folder1/folder2/folder3")
# print(os.path.exists("my_module.py"))


# size = os.path.getsize("day_1.py")
# print(size)


# for root, dirs, files in os.walk("Week_1"):
#     print("Folder:", root)
#     print("Subfolders:", dirs)
#     print("Files:", files)


# print(os.environ)
# os.system("dir")

# print(os.getpid())


# import json

# data = {
#     "name": "Qasim",
#     "age": 25,
#     "city": "Lahore",
#     "skills": ["Python", "JavaScript"]
# }

# json_string = json.dumps(data, indent=4)
# print(json_string)


# import json

# # Python dictionary
# data = {"name": "Qasim", "age": 25}

# # Save to file
# with open("data.json", "w") as f:
#     json.dump(data, f, indent=4)

# # Later read from file
# with open("data.json", "r") as f:
#     new_data = json.load(f)

# print(new_data["name"])  


# import os

# print(os.environ.get('Downloads'))


# with open('data.json', 'r') as f:
#     f_contents= f.readlines()
#     for i in f_contents:
#         print(i, end=" ")