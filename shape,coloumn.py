"""
ager hum ny kisi b data ki shape ka pta kerna ho k is my 
kitni row aur coloum ha to pher hum shape attribute ka use krty ha
aur ager hum ny column ka pta kerna ho to pher coloum attribute
"""
import pandas as pd

data = {
    "name":["Ghaffar","Aman","Fizan","Mohid"],
    "age": [19,19,21,18],
    "city": ["Jhoke","Madodhas","Jhoke","Madodhas"]
}

df = pd.DataFrame(data)
print(df)
print(f'shape: {df.shape}')
print(f'columns: {df.columns}')