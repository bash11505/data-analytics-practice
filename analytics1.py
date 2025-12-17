#basic examples of python analytcis
import pandas as pd 
data={
    "student": ["A", "B", "A", "C", "B"],
    "subject": ["Math", "Math", "Science", "Math", "Science"],
    "marks": [80, 75, 90, 60, 85]
}
df=pd.DataFrame(data)
# calculatin total avg marks
total=df['marks'].mean()
print(total)

#2nd basic practice programme
import pandas as pd
data={
    "student": ["A", "B", "A", "C", "B", "C"],
    "subject": ["Math", "Math", "Science", "Math", "Science", "Science"],
    "marks": [80, 75, 90, 60, 85, 70]
}
df=pd.DataFrame(data)
print(df)
print(df.groupby("subject")["marks"].sum())#to find the sum
print(df.groupby("subject")["marks"].mean())#for average
print(df.groupby("subjects")["marks"].max())#for maximum
print(df.groupby("subjects")["marks"].agg(["min","max","mean"]))#for multiple aggregations
print(df.groupby(["student","subjects"])["marks"].sum())
#pivot table
pivot_df=df.pivot_table(
    index ="studen",
    columns="subjects",
    values="marks",
    aggfunc="sum"
)
print(pivot_df)
df.groupby("subject")["marks"].sum().sum()                                 # → 460



