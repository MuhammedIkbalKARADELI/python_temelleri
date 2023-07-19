import pandas as pd


df1 = pd.read_csv("oscars_df.csv")
print(df1)
"""
     Unnamed: 0  ...                               Film ID
0             0  ...  2becf7d5-a3de-46ab-ae45-abdd6b588067
1             1  ...  19ed3295-a878-4fd2-8e60-5cd7b5f93dad
2             2  ...  3111c2d8-0908-4093-8ff3-99c89f2f2f08
3             3  ...  de063f3f-2d35-4e1c-8636-6eb4c16bd236
4             4  ...  609887c2-877c-43a4-b88c-e40e31096a98
..          ...  ...                                   ...
566         566  ...  47d4ae4f-e782-4cd9-9508-4a07302b1c1a
567         567  ...  7262b3a8-214d-4205-985c-70e0860f3236
568         568  ...  d64c669b-7a73-496a-bddb-19cb09264371
569         569  ...  647357e9-c067-46bd-aaeb-24d4344ec124
570         570  ...  cecbca48-f19c-43f4-81d2-da130facda95

[571 rows x 30 columns]
"""

df2 = pd.read_json("sample.json")
print(df2)
"""
     Name  Grade
0   Ahmet     96
1     Ali     60
2   Yasin     78
3  Mehmet     92
"""


df3 = pd.read_excel("Sample.xlsx")
print(df3)
"""
     Ali   90 
0  Ahmet   70
1  Fatma   80
2   Ayse  100
"""



df4 = pd.read_csv("dataset/mods_dataset.csv") # bir klasörün içindeki bilgileri alabiliri böylelikle.
print(df4)



############## bu kısımda sqlite3 kullanılacak bunu daha görmedik ama pandas ile kullanıldığınıda söylemek için göseriyoruz.

import sqlite3

connection = sqlite3.connect("sample.db") # örnek bir dosya adı
df = pd.read_sql_query("SELECT * FROM students", connection)
print(df)
