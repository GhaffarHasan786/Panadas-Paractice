# ager hum ny koi column add krna ho to do tariraqy ha 
# no1 direct method df["bonus"] = df[column_name]
# no2 using insert method df.insert(location, "column_name", some data)
     #EXAMPAL


import pandas as pd
data = {
    "name":["Ghaffar","Aman","Fizan","Mohid"],
    "age": [19,19,21,18],
    "city": ["Jhoke","Madodhas","Jhoke","Madodhas"],
    "class": ["bsit","bscs","bba","bscs"],
    
}

df =pd.DataFrame(data)
print(df)
#using direct
df["ID"]  = 1,2,3,4
print(df)

#using insert

df.insert(5,"Student_ID", [1,2,3,4])
print(df)
