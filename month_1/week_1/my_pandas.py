import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed"],
    "Age": [22, 23, 25],
    "Salary": [50000, 60000, 70000],
    "Gender": ["M", "F", None]
}
df = pd.DataFrame(data)
# print(df[df["Salary"]> 60000])
# print(df["Salary"].describe())
# print(df)

# print(df.sort_values("Age", ascending=False))

# print(df.dropna())
# print(df[df["Gender"].fillna(10)])

# print(df.isna())

# df["Bonus"] = df["Salary"]*0.2

# print(df)
# df.drop("Bonus", axis=1, inplace=True)
print(df)

print(df.groupby("Gender")["Salary"].mean())