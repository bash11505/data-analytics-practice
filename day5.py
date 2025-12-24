import pandas as pd

df = pd.DataFrame({
    "Student": ["Arjun", "Bhavya", "Kiran", "Manoj", "Nisha"],
    "Age": ["18", "nineteen", None, "21", "20"],
    "Marks": ["450", "480", "four hundred", "500", ""],
    "Attendance": ["95.5", "90", "eighty", None, 88],
    "Fee_Paid": ["True", "False", "yes", "no", None],
    "Admission_Date": ["2023-06-15", "15/07/2023", "2022.08.01", "not_admitted", None]
})
# check data types
print("original data frame:\n")
print(df.dtypes)

#convert numeric columns safely
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Marks'] = pd.to_numeric(df['Marks'], errors='coerce')
df['Attendance']=pd.to_numeric(df['Attendance'],errors='coerce')

#convert age to integer type
df['Age'] = df['Age'].astype('Int64')


#convert admission_date to datetime
df['Admission_Date']=pd.to_datetime(df['Admission_Date'],errors='coerce')


#  Print cleaned data
print("\nCleaned Data:\n")
print(df)

#  Final data types
print("\nFinal dtypes:\n")
print(df.dtypes)

#  Missing values count
print("\nMissing values count:\n")
print(df.isna().sum())
