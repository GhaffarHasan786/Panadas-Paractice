import pandas as pd
data = {
    "name":["Ghaffar",None,"Fizan","Mohid"],
    "age": [19,None,21,18],
    "city": ["Jhoke",None,"Jhoke","Madodhas"],
    "class": ["bsit",None,"bba","bscs"],
    
}

df =pd.DataFrame(data)
print(df)

print(df.isnull().sum())
