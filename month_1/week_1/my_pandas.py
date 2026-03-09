import pandas as pd

# data = {
#     "Name": ["Ali", "Sara", "Ahmed"],
#     "Age": [22, 23, 25],
#     "Salary": [50000, 60000, 70000],
#     "Gender": ["M", "F", None]
# }
# df = pd.DataFrame(data)
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
# print(df)

# print(df.groupby("Gender")["Salary"].mean())

# df["Salary"].plot(kind="hist")
# print(df.groupby("Department")["Salary"].sum().plot(kind="bar"))


# data = {
#     "Name": ["Ali", "Sara", "Ahmed", "Zara"],
#     "Age": [22, 23, 25, 21],
#     "Salary": [50000, 60000, 70000, 55000]
# }

# df = pd.DataFrame(data)
# print(df.iloc[0:2])

# print(df.loc[0])
# print(df.iloc[0])
# print(df.loc[2, ["Name"]])

# print(df[(df["Age"] > 22) & (df["Salary"] > 60000)])
# print(df[(df["Salary"] > 55000) ])


data = pd.read_csv("./archive/airline_losses_estimate.csv")
estimated_loss = data["cancelled_flights"].sum()
# print(data.shape)
# print(estimated_loss)
# print(data.describe())
# print(data.duplicated())
# print(data.isnull().values.any())
# print((data == 0).sum())
# data['estimated_daily_loss_usd'] = pd.to_numeric(data['estimated_daily_loss_usd'], errors='coerce')
# print(data)


# top_lost_airlines = data[["airline","estimated_daily_loss_usd"]].sort_values(by="estimated_daily_loss_usd", ascending=False)
# print(top_lost_airlines)

# grouped = data.groupby("country", sort=False)["airline"].nunique()
# loss_per_passenger= data["estimated_daily_loss_usd"]/data["passengers_impacted"]
# print(loss_per_passenger)

# data["fuel_cost_ratio"] = data["additional_fuel_cost_usd"] / data["estimated_daily_loss_usd"]
# data["loss_per_passenger"]= data["estimated_daily_loss_usd"]/data["passengers_impacted"]

import numpy as np

# mean_loss = np.std(data["estimated_daily_loss_usd"])
# data.corr()



