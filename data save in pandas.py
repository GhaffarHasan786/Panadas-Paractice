import pandas as pd

data = {
    "name":["Ghaffar","Aman","Fizan","Mohid"],
    "age": [19,19,21,18],
    "city": ["Jhoke","Madodhas","Jhoke","Madodhas"]
}

# kisi b data ko save krny sy pehly us ka data frame banana pry ga jo k is tera
#banta ha (df = pd.dataframe(variable name))

df = pd.DataFrame(data)

print(df)

#kisi b data ko save kerna ha to (df.to_csv)ya jis format my
#  kerna ha us ka name to k baad likhna ha

#df.to_csv("output.csv", index=False) 
# ager sath index number nai lany to pher index false kr do

df.to_excel("output.xlsx", index=False)