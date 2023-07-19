import pandas as pd
import numpy as np


data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns=["Columns1","Columns2","Columns3","Columns4","Columns5"])

column_info = df.columns # column bilgilerini verir.
result1 = df.head()  # ilk beş satır(row) bilgisini bize verir.
result2 = df.head(7)  # istediğim kadar row bilgisini yazırabiliriz.
result3 = df.tail()  # head() ile aynı mantıpa sahip olu sdaece sondaki row lardan bize veri veri. burda sondaki 5 tane row bilgisini bize verir.
result4 = df.tail(7) # sondan 7 row bilgisini bize verir.
result5 = df["Columns1"].head() # istenilen column dan 5 tane row bilgisi getirlir bize
result6 = df.Columns1.head()   # result5 deki kullanımla ynı kullanımdır.
result7 = df[["Columns1","Columns4"]].head()  # istediğin column bilgilerin alabilirsin.
result8 = df[["Columns1","Columns4"]].tail()
result9 = df[5:15][["Columns1","Columns4"]].head() # istenilen row ve column bilgileri arasında ilk 5 row bilgisini bize verdi.
result10 = df[5:15][["Columns1","Columns4"]].tail()


result11 = df > 50  # 50 büyük değerleri True yapar 
result12 = df[df > 50] # 50 den küçk değerleri verir.
result13 = df[df % 2 == 0] # df yi True yapan değerleri verir.
result14 = df["Columns1"] > 50  # Burda sadece 1. column daki bilgieri True verir.
result15 = df[df["Columns1"] > 50] # Burda sadece 1. column daki bilgierdeki doğruluğu sağalayn rowlrı içeren bir matris gelir.
result16 = df[df["Columns1"] > 50][["Columns1","Columns4"]]
result17 = df[((df["Columns2"]>50) & (df["Columns1"]<=70))]  #burdaki koşulumuz and koşuludur.# tüm columnlardaki istediğimiz dğerleri sağlayan rowlrı yazdırır.
result18 = df[((df["Columns2"]>50) | (df["Columns1"]<=70))]
result19 = df[((df["Columns2"]>50) | (df["Columns1"]<=70))][["Columns1","Columns4"]]  # tüm columnlardan istediğimiz değeri sağlayan row bilgilerini aldıktan sonra da istediğimiz column bilgierinide alabilirz. bir nevi filtreleme işlemi gibi.

result20 = df.query("Columns1 >= 50 & Columns1 % 2==0") # yukrdaki kullanımın bir kullanım versiyonu.

result21 = df.query("Columns1 >= 50 & Columns1 % 2==0")[["Columns1","Columns4"]]




print(df)
print(column_info)  
"""
Index(['Columns1', 'Columns2', 'Columns3', 'Columns4', 'Columns5'], dtype='object')
"""

print(result1)
"""
   Columns1  Columns2  Columns3  Columns4  Columns5
0        39        69        82        57        33
1        16        87        66        23        73
2        66        18        69        52        38
3        15        54        91        28        92
4        50        93        92        70        19
"""


print(result2)
"""
   Columns1  Columns2  Columns3  Columns4  Columns5
0        98        52        41        68        14
1        61        88        83        80        26
2        56        77        73        96        49
3        26        24        54        83        41
4        19        83        36        86        21
5        10        32        86        31        40
6        90        48        28        46        10
"""


print(result3)
"""
    Columns1  Columns2  Columns3  Columns4  Columns5
10        19        44        23        62        10
11        88        11        35        42        64
12        14        13        56        79        84
13        74        47        70        20        30
14        11        84        54        35        85
"""


print(result5)
"""
0    76
1    59
2    29
3    33
4    74
Name: Columns1, dtype: int32
"""

print(result6)
"""
0    84
1    21
2    18
3    57
4    22
Name: Columns1, dtype: int32
"""

print(result7)
"""
   Columns1  Columns4
0        43        78
1        30        32
2        69        35
3        15        45
4        65        98
"""


print(result8)
"""
    Columns1  Columns4
10        50        87
11        99        35
12        10        51
13        53        62
14        96        83
"""

print(result9)
"""
   Columns1  Columns4
5        73        73
6        12        79
7        35        80
8        56        68
9        73        28
"""

print(result10)
"""
    Columns1  Columns4
10        83        77
11        48        54
12        16        77
13        22        54
14        71        61
"""

print(result11)
"""
    Columns1  Columns2  Columns3  Columns4  Columns5
0       True     False      True     False      True
1      False      True      True     False     False
2       True      True      True      True      True
3       True     False     False      True      True
4      False     False     False     False      True
5      False      True      True      True     False
6      False      True      True     False      True
7       True     False     False      True      True
8       True     False      True      True     False
9      False      True     False      True      True
10      True      True      True      True     False
11     False      True      True      True     False
12      True     False     False     False     False
13      True     False     False      True      True
14     False     False      True     False      True
"""


print(result12)
"""
  Columns1  Columns2  Columns3  Columns4  Columns5
0       60.0       NaN      62.0       NaN      65.0
1        NaN      83.0      81.0       NaN       NaN
2       64.0      55.0      71.0      74.0      76.0
3       63.0       NaN       NaN      97.0      91.0
4        NaN       NaN       NaN       NaN      69.0
5        NaN      80.0      88.0      73.0       NaN
6        NaN      66.0      94.0       NaN      84.0
7       79.0       NaN       NaN      93.0      56.0
8       53.0       NaN      72.0      79.0       NaN
9        NaN      52.0       NaN      93.0      58.0
10      74.0      84.0      52.0      88.0       NaN
11       NaN      53.0      99.0      55.0       NaN
12      61.0       NaN       NaN       NaN       NaN
13      99.0       NaN       NaN      69.0      80.0
14       NaN       NaN      81.0       NaN      60.0
"""

print(result13)
"""
   Columns1  Columns2  Columns3  Columns4  Columns5
0       60.0      26.0      62.0      36.0       NaN
1       40.0       NaN       NaN      44.0      16.0
2       64.0       NaN       NaN      74.0      76.0
3        NaN      46.0       NaN       NaN       NaN
4       38.0       NaN       NaN      24.0       NaN
5        NaN      80.0      88.0       NaN       NaN
6       36.0      66.0      94.0       NaN      84.0
7        NaN       NaN      38.0       NaN      56.0
8        NaN       NaN      72.0       NaN       NaN
9       44.0      52.0      50.0       NaN      58.0
10      74.0      84.0      52.0      88.0      14.0
11       NaN       NaN       NaN       NaN      38.0
12       NaN      48.0      32.0      46.0      14.0
13       NaN      18.0      38.0       NaN      80.0
14      30.0       NaN       NaN       NaN      60.0"""



print(result14)
"""
0      True
1     False
2      True
3      True
4     False
5     False
6     False
7      True
8      True
9     False
10     True
11    False
12     True
13     True
14    False
Name: Columns1, dtype: bool"""


print(result15)
"""
Name: Columns1, dtype: bool
    Columns1  Columns2  Columns3  Columns4  Columns5
0         60        26        62        36        65
2         64        55        71        74        76
3         63        46        43        97        91
7         79        33        38        93        56
8         53        39        72        79        47
10        74        84        52        88        14
12        61        48        32        46        14
13        99        18        38        69        80"""

print(result16)
"""
    Columns1  Columns4  
0         60        36
2         64        74
3         63        97
7         79        93
8         53        79
10        74        88
12        61        46
13        99        69"""

print(result17)
"""
    Columns1  Columns2  Columns3  Columns4  Columns5
2         54        78        98        99        36
10        28        67        32        86        11
11        68        99        59        61        20
"""

print(result18)

print(result19)

print(result20)
"""
    Columns1  Columns2  Columns3  Columns4  Columns5
0         64        34        19        74        25
1         58        52        29        52        29
2         64        30        54        65        99
6         66        55        14        13        69
14        50        65        67        78        18
"""

print(result21)
"""
    Columns1  Columns4
4         84        95
6         78        85
8         94        64
12        76        37
"""


