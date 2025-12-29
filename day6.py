import pandas as pd

df = pd.DataFrame({
    "Name": ["Ravi", "Amit", "Sita", "Ramesh"],
    "Age": [25, 30, 28, 40],
    "Salary": [50000, 60000, 70000, 80000]
})

print(df)
print(df[df['Age'] > 26])
print(df[df['Salary'] >= 60000])
print(df[(df['Age'] > 26) & (df['Salary'] > 60000)])


