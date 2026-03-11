import pandas as pd
#ager program file read krny my error dy to pher (encoding = "latin1" ya encoding ="utf_8") 
# ka use kry gy to sai hojaye ga
#df = pd.read_csv("path of file") ye csv file ka data read kerny k liye use kerty ha
#df = pd.read_excel("path") ye excal ki file ko read krny k liye use krty ha
df = pd.read_json("path")
print(df)
