import pandas as pd
data = {
    "name":["Ghaffar","Aman","Fizan","Mohid"],
    "age": [19,19,21,18],
    "city": ["Jhoke","Madodhas","Jhoke","Madodhas"],
    "class": ["bsit","bscs","bba","bscs"],
    
}

df =pd.DataFrame(data)
print(df)

#ager kisi b data ya colunm ko remove kerna ho to pher hum pher kuch method use kr skty ha
# is k liye hum drop function use krty ha
# df.drop(column = ["column_name"], inplace = true)


# ager ik column ko remove krna ho to pher hum ye drop use krty ha agr multiple column ko remove krna ho 
#to pher comma lga ker bs dusry column ka name likh do

print("Modified the data")
df.drop(columns= ["city","age"], inplace=True)
print(df)