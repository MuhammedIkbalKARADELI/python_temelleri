import pandas as pd
import numpy as np


# pandas_series = pd.Series()  # Series([], dtype: float64)
# print(pandas_series)

# data 

numbers = [20,30,40,50]
leteers = ["a","b","c","d","e"]
randomm = ["a","b",40,50,"e"]
scalar = 5
dict = {"Ali": 123, "Mehmet": 456, "Veli": 324, "Yasin": 576}

random_numbers = np.random.randint(10,100,6)
np_numbers = np.array([20,30,40,50,60])


pandas_series1 = pd.Series(numbers)
print(pandas_series1)
"""
0    20   # baştaki index sayıları kendiliğinde natanıyor çünkü bzi atamdık
1    30
2    40
3    50
dtype: int64
"""


pandas_series2 = pd.Series(leteers)
print(pandas_series2)
"""
0    a
1    b
2    c
3    d
4    e
dtype: object
"""


pandas_series3 = pd.Series(randomm)
print(pandas_series3)
"""
0     a
1     b
2    40
3    50
4     e
dtype: object
"""


pandas_series4 = pd.Series(scalar)
print(pandas_series4)
"""
0    5
dtype: int64
"""


pandas_series5 = pd.Series(5, [0,1,2,3,4])
print(pandas_series5)
"""
0    5
1    5
2    5
3    5
4    5
dtype: int64
"""


pandas_series6 = pd.Series(numbers, ["a","b","c","d"]) # burda biz index numaralarını biz kendimiz vermiş olduk.
print(pandas_series6)
"""
a    20
b    30
c    40
d    50
dtype: int64
"""

pandas_series7 = pd.Series(dict)  # burda herhangi bir index bilgisi vermemize gerek yok(yukardaki pandas_series6 daki gibi) çünkü burda bia dic formatında oluşturmuş oluyoruz.
print(pandas_series7)
"""
Ali       123
Mehmet    456
Veli      324
Yasin     576
dtype: int64
"""


pandas_series8 = pd.Series(random_numbers)  # numpy kütüphanesi pandas ile kullanılabileceğinin bir örneğidir.
print(pandas_series8)

"""
0    56
1    70
2    60
3    81
4    77
5    17
dtype: int32
"""


pandas_series9 = pd.Series(np_numbers)
print(pandas_series9)
"""
0    20
1    30
2    40
3    50
4    60
dtype: int32
"""

#################################indexing skills##################

pandas_series10 = pd.Series([10,20,30,40,50,60,70,80,90],["a","b","c","d","e","f","g","h","i"])
print(pandas_series10)
"""
a    10
b    20
c    30
d    40
e    50
f    60
g    70
h    80
i    90
dtype: int64
"""



result1 = pandas_series10[0] # 10
# burda yukarda indexleri kendimiz tanımlamıza rağmen 0. index istediğimizde karşılığını verir bize.
print(result1)  # 10

result2 = pandas_series10[-1]
print(result2)  # 90

result3 = pandas_series10[:2]
print(result3)
"""
a    10
b    20
dtype: int64"""

result4 = pandas_series10[-2:]
print(result4)
"""
h    80
i    90
dtype: int64"""


result5 = pandas_series10["a"]  # kendi oluşturduğumuz index değerlerle çağırabiliriz.
print(result5) # 10


result6 = pandas_series10[["a","c"]]
print(result6)
"""
a    10
c    30
dtype: int64
"""

result7 = pandas_series10.ndim
print(result7)  # 1


result8 = pandas_series10.dtype
print(result8)  # int64


result9 = pandas_series10.shape
print(result9)  # (9,)


result10 = pandas_series10.sum()
print(result10)  # 450


result11 = pandas_series10.max()
print(result11) # 90


result12 = pandas_series10.min()
print(result12) # 10


result13 = pandas_series10 + pandas_series10 
print(result13)
"""
a     20
b     40
c     60
d     80
e    100
f    120
g    140
h    160
i    180
dtype: int64
"""

result14 = pandas_series10 + 50
print(result14)
"""
a     60
b     70
c     80
d     90
e    100
f    110
g    120
h    130
i    140
dtype: int64
"""

result15 = np.sqrt(pandas_series10)
print(result15)
"""
a    3.162278
b    4.472136
c    5.477226
d    6.324555
e    7.071068
f    7.745967
g    8.366600
h    8.944272
i    9.486833
dtype: float64
"""


result16 = pandas_series10 >= 50
print(result16)
"""
a    False
b    False
c    False
d    False
e     True
f     True
g     True
h     True
i     True
dtype: bool
"""

result17 = pandas_series10[pandas_series10 >= 50]
print(result17)
"""
e    50
f    60
g    70
h    80
i    90
dtype: int64
"""


result18 = pandas_series10 % 2 == 0
print(result18)
"""
a    True
b    True
c    True
d    True
e    True
f    True
g    True
h    True
i    True
dtype: bool
"""




opel2018 = pd.Series([20,30,40,10],["Astra","Corsa","Mokka","Insignia"])
opel2019 = pd.Series([40,30,20,10],["Astra","Corsa","Grandland","Insignia"])

total = opel2018 + opel2019
print(total)
print(total["Corsa"])  # 60.0
# burda index kısım olan yer araba modelleri olna kısımdır.


"""
Astra        60.0
Corsa        60.0
Grandland     NaN
Insignia     20.0
Mokka         NaN   ->  bis sayı değil (NaN)
dtype: float64
"""

