import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# df = pd.read_excel('f22_morning.xlsx' , engine='openpyxl')
# print(stu.describe())
# print(stu.info())
# df[['Name', 'Email Address']]
# stu_array = stu.to_numpy()

# print(stu_array)


# df = pd.read_excel('f22_morning.xlsx')

# while True:
#     print("\n1. Show All")
#     print("2. Search Student")
#     print("3. Random Student")
#     print("4. Email Domains")
#     print("5. Exit")

#     choice = input("Choose: ")

#     if choice == "1":
#         print(df)

#     elif choice == "2":
#         name = input("Enter name: ")
#         print(df[df['Name'].str.contains(name, case=False)])

#     elif choice == "3":
#         print(df.sample(1))

#     elif choice == "4":
#         df['Domain'] = df['Email'].apply(lambda x: x.split('@')[-1])
#         print(df['Domain'].value_counts())

#     elif choice == "5":
#         break


import pandas as pd
import openpyxl
# s = pd.Series([10, 20, 30])
# print(s)

# data = {
#     "name": ["Ali", "Qasim", "Sara"],
#     "age": [22, 23, 21]
# }

# df = pd.DataFrame(data)

# print(df)


# df = pd.read_json('products.json')
# print(df)

df = pd.read_excel("f22_morning.xlsx" , header=1,  engine='openpyxl')

# print(df[df['sr #']>30])
# print(df.loc[1])
# print(df.fillna(0))

# df.rename(columns={"Name": "full_name"}, inplace=True)
# df.sort_values(by="sr #", ascending=False)
# print(df)

# df["sr #"].plot(kind="bar")
# plt.show()

# df["Email Address"][0] = 'muhammad.qasim.dev07@gmail.com'
# df.iloc[0,3]= 'mq80140@gmail.com'
# df.to_excel("f22_morning.xlsx", index=False)
# print(df)