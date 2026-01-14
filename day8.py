import pandas as pd 
data ={
    "name":["alice","bob","charlie","dog"],
    "age":[25,30,35,40],
    "Salary": [30000, 25000, 40000, 35000]
}
df=pd.DataFrame(data)
df.groupby('age')['Salary'].mean()
print(df)


#2nd programme
import pandas as pd 

data = {
    "name": ["alice","bob","charlie","dog"],
    "age": [25,30,35,40],
    "Salary": [30000, 25000, 40000, 35000]
}

df = pd.DataFrame(data)

print(df.groupby('name').agg({'Salary':'mean','age':'max'}))
print(df)
