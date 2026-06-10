import pandas as pd

# s = pd.Series([10,20,30])
# print(s)

# data = {
#     "Name":["John","Alice"],
#     "Age":[25,30]
# }

# data = pd.DataFrame({
#     "A":[1,2,3],
#     "B":[4,5,6]
# }, columns=["AB","XS"])


# data =pd.DataFrame([
#     [1,"John"],
#     [2,"Alice"]
# ], columns=["ID","Names"])
# data = pd.DataFrame({})


# df = pd.DataFrame(data)

# data = pd.read_json("./data/data.json")



data = pd.read_csv("./data/ai_student.csv")
# print(data.describe())
# print(data.info())
# print(data.head())
# print(data.tail())

# print(data.columns[7])
# print(data.dtypes)
# print(data[["Student_ID", "Year_of_Study" ]])

# print(data.loc[1, "Student_ID"])
# print(data[(data["Pre_Semester_GPA"] > 3.70) & (data["Skill_Retention_Score"] > 80)])
# print(data[(data["Pre_Semester_GPA"] > 3.70)])
# print(data.isnull())
# print(data.isnull().sum())

# data = data.rename(
#  columns={"Major_Category":"Major_Categories"}
# )
data["Post_Semester_GPA"] = data["Post_Semester_GPA"].astype(int)
print(data["Post_Semester_GPA"])