#dupilcates
import pandas as pd
data = {
    'Name': ['A', 'B', 'A', 'C', 'B'],
    'Age': [20, 25, 20, 30, 25]
}

df = pd.DataFrame(data)
print(df)
#find dupilcates
df.duplicated()
print("dupilcates in data farmes:")
df[df.duplicated()]
print("\n removing dupilcates:")
