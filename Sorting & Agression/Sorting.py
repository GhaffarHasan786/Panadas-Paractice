# ager hum ny kisi b data ko sorted krna ho yani kisi order my lana ho to pher
# sort function use krty ha
# df.sort_value(by="column name",assending = true/false, inplace = true)

import pandas as pd

Data = {
    "Name":['Ghaffar','Ali','Ahmad'],
    "Age":[22,23,45],
    "Salary":[20000,30000,40000]
}

df =pd.DataFrame(Data)
print(df)

# ager hum ny single column ko sorted krna ho to pher hum syntax my single colmn name likhy gy
# aur ager multiple column ko krna ha to pher multiple ka name likh dy gy

# as a single column

df.sort_values(by=["Age","Salary" ], ascending=False, inplace=True)
print(df)