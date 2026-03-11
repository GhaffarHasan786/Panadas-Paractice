import pandas as pd
data = {
    "name":["Ghaffar",None,"Fizan","Mohid"],
    "age": [19,None,21,18],
    "city": ["Jhoke",None,"Jhoke","Madodhas"],
    "class": ["bsit",None,"bba","bscs"],
    
}

df =pd.DataFrame(data)
print(df)

# jha missing value ha ager wha hum ny koi value drop yani hatani ho to us k liye hum 
# dropna(inplace = true/false) ka use krty ha

df.dropna(inplace=True)
print(df)