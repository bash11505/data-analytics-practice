import pandas as pd

df = pd.DataFrame({
    "Employee": ["Anil", "Bhanu", "Charan", "Deepak", "Esha"],
    "Age": ["22", "twenty five", "30", None, "40"],
    "Salary": ["45000", "55000", "60k", "70000", ""],
    "Bonus": [5000, "3000", None, "four thousand", 2000],
    "Joining_Date": ["2022-01-15", "15-02-2023", "2021/07/10", "not_joined", None],
    "Rating": ["4.5", "3", "five", 4, None]
})

df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['Bonus'] = pd.to_numeric(df['Bonus'], errors='coerce')
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df['Joining_Date'] = pd.to_datetime(df['Joining_Date'], errors='coerce')

print(df)
print("\nData Types:\n")
print(df.dtypes)
print("\nMissing Values:\n")
print(df.isna().sum())


#Second DataFrame -
df = pd.DataFrame({
    "Employee": ["Anil", "Bhanu", "Charan", "Deepak", "Esha"],
    "Age": ["22", "twenty five", "30", None, "40"],
    "Salary": ["45000", "55000", "60k", "70000", ""],
    "Bonus": [5000, "3000", None, "four thousand", 2000],
    "Joining_Date": ["2022-01-15", "15-02-2023", "2021/07/10", "not_joined", None],
    "Rating": ["4.5", "3", "five", 4, None]
})

df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['Bonus'] = pd.to_numeric(df['Bonus'], errors='coerce')
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df['Joining_Date'] = pd.to_datetime(df['Joining_Date'], errors='coerce')

df.dtypes
df.isna().sum()
df.describe()