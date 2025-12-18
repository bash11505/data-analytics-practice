#1st  basic commands
# 1️⃣ Basic Commands
import pandas as pd
data = {
    "Name": ["Ravi", "Amit", "Ravi", None, "Sita"],
    "Age": [25, None, 25, 30, 28],
    "City": ["Delhi ", "Mumbai", "Delhi ", "Chennai", " mumbai"],
    "Salary": [50000, 60000, 50000, 70000, None]
}
df = pd.DataFrame(data)
# Show first 5 rows
print("First 5 rows:")
print(df.head())
# Show last 5 rows
print("\nLast 5 rows:")
print(df.tail())
# Show statistical summary
print("\nStatistical summary:")
print(df.describe())
# Show column names
print("\nColumn names:")
print(df.columns)
# Show info about DataFrame (data types, non-null counts)
print("\nDataFrame info:")
df.info()   # info() already prints, no need for print()




#2nd programme missing values
import pandas as pd
data ={
    "Name": ["Ravi", "Amit", "Ravi", None, "Sita"],
    "Age": [25, None, 25, 30, 28],
    "City": ["Delhi ", "Mumbai", "Delhi ", "Chennai", " mumbai"],
    "Salary": [50000, 60000, 50000, 70000, None]
} 

df = pd.DataFrame(data)
# Check missing values
print(df.isnull())
print(df.isnull().sum())
# Drop rows with missing values (optional)
df_cleaned = df.dropna()
# Fill missing values
df_filled = df.fillna(0)
df['Age'] = df['Age'].fillna(df['Age'].mean())

print(df)
