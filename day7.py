import pandas as pd 

data = {
    "Name": ["Basha", "Aman", "Ravi", "Sita"],
    "Age": [23, 21, 25, 22],
    "Salary": [30000, 25000, 40000, 35000]
}
df =pd.DataFrame(data)
df.sort_values('Age', inplace=True)
df.sort_values('Salary', inplace=True)
print(df)