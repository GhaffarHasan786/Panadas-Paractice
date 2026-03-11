import pandas as pd
data = {
    "name":["Ghaffar","Ali","Fizan","Mohid"],
    "age": [19,None,21,18],
    "city": ["Jhoke",None,"Jhoke","Madodhas"],
    "class": ["bsit",None,"bba","bscs"],
    
}

df =pd.DataFrame(data)
print(df)

#ager hum missing value ko drop krny ki bjaye whaha koi defualt value put krni ho 
# to pher hum .fillna() ka use krty ha is me do parameter dety ha
# .fillna(value,inplace)

df.fillna(0,inplace=True)
print(df)

# defualt value ager na lagani ho us ki jga ager kiu aur value deni ho
# to us k liye calculated value ka use krty ha jis k liye hum koi condition rkh dty ha
# df['age'].fillna[df['age'].mean(), implace = true]

df['age'] = df['age'].fillna(df['age'].mean())

print(df)