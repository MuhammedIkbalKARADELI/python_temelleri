import pandas as pd
import numpy as np

data = {
    "Column1" : [1,2,3,4,5,6,7,8],
    "Column2" : [10,20,13,45,25,45,20,13],
    "Column3" : ["abc","bca","ad","cba","dead","as","afg","tfdg"]
}

df = pd.DataFrame(data)
print(df)
"""
   Column1  Column2 Column3
0        1       10     abc
1        2       20     bca
2        3       13      ad
3        4       45     cba
4        5       25    dead
5        6       45      as
6        7       20     afg
7        8       13    tfdg
"""


result1 = df["Column2"].unique() # burda birbirini tekrar edenleri yazdırmaz.
print(result1)
"""
[10 20 13 45 25]
"""

result2 = df["Column2"].nunique() # biribirinden farklı sayıların adadeni verir.
print(result2) # 5


result3 = df["Column2"].value_counts()  
print(result3) 
"""
20    2
13    2
45    2
10    1
25    1
Name: Column2, dtype: int64
"""

result4 = df["Column2"] * 2  # bizim değerleri iki katını verir bize. 
print(result4)
"""
0    20
1    40
2    26
3    90
4    50
5    90
6    40
7    26
Name: Column2, dtype: int64
"""


# kareal2 = lambda x: x*x 
# burdak ikullanımla aşağıdaki kullanım aynıdır.

def kareal(x):
    return x * x

# result5  = df["Column2"].apply(lambda x: x*x)
result5  = df["Column2"].apply(kareal)  # bizim değerleri sanki for döngüsü kullanımı gibi yapıp tüm değerleri func ile işleyebildik.
print(result5)    
"""
0     100
1     400
2     169
3    2025
4     625
5    2025
6     400
7     169
Name: Column2, dtype: int64
"""


result6 = df["Column3"].apply(len)
print(result6)
"""
0    3
1    3
2    2
3    3
4    4
5    2
6    3
7    4
Name: Column3, dtype: int64
"""



df["Column4"] = df["Column3"].apply(len)
print(df)



result7 = df.columns
print(result7)  # Index(['Column1', 'Column2', 'Column3', 'Column4'], dtype='object')


result8 = len(df.columns)
print(result8)  # 4


result9 = df.index
print(result9)  # RangeIndex(start=0, stop=8, step=1)


result10 = len(df.index)
print(result10)  # 8


result11 = df.info
print(result11)
"""
<bound method DataFrame.info of    Column1  Column2 Column3  Column4
0        1       10     abc        3
1        2       20     bca        3
2        3       13      ad        2
3        4       45     cba        3
4        5       25    dead        4
5        6       45      as        2
6        7       20     afg        3
7        8       13    tfdg        4>
"""


result12 = df.sort_values("Column2") # column2 ye göre artan sıralayarak bir df oluştururuz.
print(result12)
"""
   Column1  Column2 Column3  Column4
0        1       10     abc        3
2        3       13      ad        2
7        8       13    tfdg        4
1        2       20     bca        3
6        7       20     afg        3
4        5       25    dead        4
3        4       45     cba        3
5        6       45      as        2
"""

result13 = df.sort_values("Column3") # column3 ye göre artan sıralayarak bir df oluştururuz.
print(result13)
"""
   Column1  Column2 Column3  Column4
0        1       10     abc        3
2        3       13      ad        2
6        7       20     afg        3
5        6       45      as        2
1        2       20     bca        3
3        4       45     cba        3
4        5       25    dead        4
7        8       13    tfdg        4
"""



result12 = df.sort_values("Column2", ascending = False) # column2 ye göre azalan sıralayarak bir df oluştururuz.
print(result12)
"""
   Column1  Column2 Column3  Column4
3        4       45     cba        3
5        6       45      as        2
4        5       25    dead        4
1        2       20     bca        3
6        7       20     afg        3
2        3       13      ad        2
7        8       13    tfdg        4
0        1       10     abc        3
"""





veri = {
    "Ay" : ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori" : ["Elektrik","Elektrik","Elektrik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir" : [20,30,15,14,32,42,12,36,52]
}

df_veri = pd.DataFrame(veri)

result14 = df_veri.pivot_table(index= "Ay", columns= "Kategori", values= "Gelir")
print(result14)
"""
Kategori  Elektrik  Giyim  Kitap
Ay
Haziran         30     36     32
Mayıs           20     12     14
Nisan           15     52     42
"""
