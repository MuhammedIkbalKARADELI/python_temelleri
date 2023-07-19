import pandas as pd
import numpy as np


data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data, index=["a","c","e","f","h"], columns=["Column1","Column2","Column3"])


df = df.reindex(["a","b","c","d","e","f","g","h"])




print(df)
"""
   Column1  Column2  Column3
a     73.0     33.0     68.0
b      NaN      NaN      NaN
c     54.0     97.0     99.0
d      NaN      NaN      NaN
e     20.0     96.0     42.0
f     62.0     48.0     99.0
g      NaN      NaN      NaN
h     89.0     62.0     15.0
"""

result1 = df.drop("Column1", axis = 1)  # axis=1 column olduğunu bellirtir.
print(result1)
"""
   Column2  Column3
a     25.0     29.0
b      NaN      NaN
c     35.0     62.0
d      NaN      NaN
e     44.0     50.0
f     52.0     22.0
g      NaN      NaN
h     21.0     94.0
"""


result2 = df.drop(["Column1","Column3"], axis = 1)
print(result2)
"""
   Column2
a     46.0
b      NaN
c     57.0
d      NaN
e     51.0
f     64.0
g      NaN
h     43.0
"""

result3 = df.drop("a",axis=0)  # axis=0 row olduğunu belirtir.
print(result3)
"""
   Column1  Column2  Column3
b      NaN      NaN      NaN
c     41.0     89.0     34.0
d      NaN      NaN      NaN
e     99.0     17.0     58.0
f     27.0     31.0     98.0
g      NaN      NaN      NaN
h     74.0     99.0     77.0
"""

result4 = df.drop(["a","b","h"],axis=0)
print(result4)
"""
   Column1  Column2  Column3
c     60.0     12.0     65.0
d      NaN      NaN      NaN
e     23.0     62.0     65.0
f     62.0     32.0     65.0
g      NaN      NaN      NaN
"""



result5 = df.isnull()  # Nan olan değerleri True değer yapar.
print(result5)
"""
   Column1  Column2  Column3
a    False    False    False
b     True     True     True
c    False    False    False
d     True     True     True
e    False    False    False
f    False    False    False
g     True     True     True
h    False    False    False
"""


result6 = df.notnull()  # Nan olan değerler False olarak gelir.
print(result6)
"""
   Column1  Column2  Column3
a     True     True     True
b    False    False    False
c     True     True     True
d    False    False    False
e     True     True     True
f     True     True     True
g    False    False    False
h     True     True     True
"""



result7 = df.isnull().sum() # Nan değerlerin adedini söyler.
print(result7)
"""
Column1    3
Column2    3
Column3    3
dtype: int64
"""

result8 = df["Column1"].isnull().sum() # column1 deki değerlerin Nan değer sayısını bize verir. 
print(result8) # 3



newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["Column4"] = newColumn

print(df)
"""
   Column1  Column2  Column3  Column4
a     80.0     29.0     82.0      NaN
b      NaN      NaN      NaN     30.0
c     51.0     87.0     59.0      NaN
d      NaN      NaN      NaN     51.0
e     70.0     54.0     22.0      NaN
f     80.0     86.0     30.0     30.0
g      NaN      NaN      NaN      NaN
h     84.0     50.0     69.0     10.0
"""


result9 = df["Column1"].isnull()
print(result9)
"""
a    False
b     True
c    False
d     True
e    False
f    False
g     True
h    False
Name: Column1, dtype: bool
"""


result10 = df[df["Column1"].isnull()]  # Column1 deki nan olan satırlar, tüm columnlar tarafından yazdıırlır.
print(result10)
"""
   Column1  Column2  Column3  Column4
b      NaN      NaN      NaN     30.0
d      NaN      NaN      NaN     51.0
g      NaN      NaN      NaN      NaN
"""


result11 = df[df["Column1"].isnull()]["Column1"] 
print(result11)
"""
b   NaN
d   NaN
g   NaN
Name: Column1, dtype: float64
"""
result12 = df[df["Column1"].notnull()]["Column1"] 
print(result12)
"""
a    55.0
c    87.0
e    29.0
f    11.0
h    71.0
Name: Column1, dtype: float64
"""



result13 = df.dropna()  #  axis=0  row da Nan  olan rowları getirmez
print(result13)

"""
   Column1  Column2  Column3  Column4
f     52.0     73.0     21.0     30.0
h     50.0     68.0     90.0     10.0"""


result14 = df.dropna(axis=1)  # columns da Nan olan columnları yazmaz
print(result14)
"""
Empty DataFrame
Columns: []
Index: [a, b, c, d, e, f, g, h]
"""

print(df)



result15 = df.dropna(how = "any")  # row da Nan  olan rowları getirmez
print(result15)
"""
   Column1  Column2  Column3  Column4
f     80.0     16.0     66.0     30.0
h     72.0     37.0     89.0     10.0
"""

result16 = df.dropna(how = "all") # row da tüm rowu nan olanları getirmez
print(result16)
"""
   Column1  Column2  Column3  Column4
a     93.0     74.0     37.0      NaN
b      NaN      NaN      NaN     30.0
c     70.0     68.0     37.0      NaN
d      NaN      NaN      NaN     51.0
e     36.0     87.0     93.0      NaN
f     80.0     16.0     66.0     30.0
h     72.0     37.0     89.0     10.0
"""


result17 = df.dropna(subset = ["Column1"])  # Column1 de nan olan rowları yazdırmaz.
print(result17)
"""
   Column1  Column2  Column3  Column4
a     68.0     15.0     85.0      NaN
c     32.0     50.0     79.0      NaN
e     11.0     44.0     86.0      NaN
f     23.0     58.0     98.0     30.0
h     71.0     37.0     70.0     10.0
"""

result18 = df.dropna(subset = ["Column1","Column2"])  # Column1 ve Column2 deki nan olan rowları yazdırmaz. 
print(result18)
"""
   Column1  Column2  Column3  Column4
a     41.0     37.0     93.0      NaN
c     71.0     97.0     52.0      NaN
e     12.0     72.0     42.0      NaN
f     37.0     54.0     54.0     30.0
h     29.0     74.0     99.0     10.0
"""

result19 = df.dropna(subset = ["Column4"])  # Column4 de nan olan rowları yazdırmaz.
print(result19)
"""
   Column1  Column2  Column3  Column4
b      NaN      NaN      NaN     30.0
d      NaN      NaN      NaN     51.0
f     60.0     23.0     30.0     30.0
h     68.0     77.0     31.0     10.0
"""

result20 = df.dropna(subset = ["Column1","Column4"], how = "all") # Column1 ve Column4 de ikisinde nan var olan rowlar yazılmaz
print(result20)
"""
   Column1  Column2  Column3  Column4
a     50.0     48.0     57.0      NaN
b      NaN      NaN      NaN     30.0
c     85.0     26.0     72.0      NaN
d      NaN      NaN      NaN     51.0
e     53.0     25.0     44.0      NaN
f     76.0     16.0     60.0     30.0
h     48.0     43.0     60.0     10.0
"""

result21 = df.dropna(subset = ["Column1","Column4"], how = "any") # Column1 ve Column4 daki nan var olan rowlar yazılmaz
print(result21)
"""
   Column1  Column2  Column3  Column4
f     13.0     84.0     57.0     30.0
h     76.0     20.0     39.0     10.0
"""

result22 = df.dropna(thresh = 2)  # burda  rowlarda nan dışındaki değer sayısı en az iki değer olanları yazar.
print(result22)
"""
   Column1  Column2  Column3  Column4
a     66.0     71.0     54.0      NaN
c     78.0     34.0     48.0      NaN
e     38.0     45.0     80.0      NaN
f     93.0     89.0     85.0     30.0
h     72.0     88.0     81.0     10.0
"""

result23 = df.dropna(thresh = 4)  # en az sayıda normal veri 
print(result23)
"""
   Column1  Column2  Column3  Column4
f     93.0     89.0     85.0     30.0
h     72.0     88.0     81.0     10.0
"""


result24 = df.fillna(value = "No input") # nan olan değerleri "No input" olarak değiştirdik.
print(result24)
"""
    Column1   Column2   Column3   Column4
a      81.0      29.0      78.0  No input
b  No input  No input  No input      30.0
c      99.0      19.0      86.0  No input
d  No input  No input  No input      51.0
e      38.0      95.0      40.0  No input
f      86.0      50.0      97.0      30.0
g  No input  No input  No input  No input
h      23.0      25.0      97.0      10.0
"""

result24 = df.fillna(value = 1) 
print(result24)
"""
   Column1  Column2  Column3  Column4
a     58.0     81.0     41.0      1.0
b      1.0      1.0      1.0     30.0
c     15.0     43.0     96.0      1.0
d      1.0      1.0      1.0     51.0
e     49.0     90.0     13.0      1.0
f     55.0     16.0     88.0     30.0
g      1.0      1.0      1.0      1.0
h     42.0     33.0     73.0     10.0
"""

print(df.sum())
"""
Column1    256.0
Column2    235.0
Column3    339.0
Column4    121.0
dtype: float64
"""
print(df.sum().sum())
"""953.0"""

print(df.isnull().sum())
"""
Column1    3
Column2    3
Column3    3
Column4    4
dtype: int64
"""
print(df.isnull().sum().sum()) # 13 tane nan değer var.



def ortalama(df):
   toplam = df.sum().sum() # değerler toplamı
   adet = df.size - df.isnull().sum().sum()
   return toplam/adet


result25 = df.fillna(value = ortalama(df))
print(result25)
"""
     Column1    Column2    Column3    Column4
a  14.000000  52.000000  59.000000  43.526316
b  43.526316  43.526316  43.526316  30.000000
c  30.000000  77.000000  30.000000  43.526316
d  43.526316  43.526316  43.526316  51.000000
e  19.000000  78.000000  46.000000  43.526316
f  68.000000  15.000000  43.000000  30.000000
g  43.526316  43.526316  43.526316  43.526316
h  50.000000  30.000000  95.000000  10.000000
"""

