import pandas as pd
from numpy.random import randn

rs = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10],[1,2,3,4,5],[6,7,8,9,10],[3,4,5,6,7]],index=[1,2,3,4,5],columns=[1,2,3,4,5])
print(rs)
"""
   1  2  3  4   5  <- column bilgileri
1  1  2  3  4   5
2  6  7  8  9  10
3  1  2  3  4   5    # geri kalan kısımda matrisimiz oluyor bir nevi
4  6  7  8  9  10
5  3  4  5  6   7
^
|
index bilgileri
"""



df = pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["Column1","Column2","Column3"])
print(df)
"""
    Column1   Column2   Column3
A  0.652717 -1.103341 -1.242787
B  0.468117  0.857099  1.089520
C  0.731250 -0.699035  0.449576
"""
#########################column bilgileri alma###################
result1 = df["Column1"]
print(result1)
"""
A   -0.812586
B   -0.443450
C   -0.761528
Name: Column1, dtype: float64
"""

result2 = df[["Column1","Column3"]] # bir den fazla column yazmak istersek eğeer bu yapıda yazıyoruz.
print(result2)
"""
    Column1   Column3
A  0.935455  1.413777
B -0.421175  0.744608
C -0.977285  0.725062
"""

result3 = type(df["Column1"])
print(result3)  # <class 'pandas.core.series.Series'>


result4 = type(df[["Column1","Column3"]])
print(result4)  # <class 'pandas.core.frame.DataFrame'>



####################### loc[]  kullanımı #################

# loc["row","column"]  ****    loc["row"]  ******  loc[["row1","row2"]]  *****  loc[:, "column"] (bu kullanım yukarıdaki gibi kullanıdğımız kullaanımlara benziyor.)
# ****** loc[["row1","row2"] ,["column1","Column2"]] 

result5 = df.loc["A"]
print(result5)  # A indexindeki satır(row) bilgilrini bize verir. 
"""
Column1    0.837690
Column2    1.020125
Column3    1.081768
Name: A, dtype: float64
"""

result6 = type(df.loc["A"])
print(result6)   # <class 'pandas.core.series.Series'>


result7 = df.loc[["A","C"]]
print(result7)
"""
    Column1   Column2   Column3
A  0.097977  0.378033  0.585300
C -0.474943 -1.160048  1.554317
"""

result8 = type(df.loc[["A","C"]])
print(result8)  # <class 'pandas.core.frame.DataFrame'>


result9 = df.loc["A","Column2"]
print(result9)  #  0.7806862613643982



result10 = df.loc[["A","C"],"Column3"]
print(result10)
"""
A   -0.062751
C    0.412378
Name: Column3, dtype: float64
"""

result11 = df.loc[["A","C"],["Column2","Column3"]]
print(result11)
"""
    Column2   Column3
A -0.096736 -1.340705
C -0.311765 -0.314481
"""


result12 = df.loc[:,"Column2"]
print(result12)
"""
A    1.276730
B    0.752784
C   -0.143804
Name: Column2, dtype: float64
"""


result13 = df.loc[:,["Column1", "Column2"]]
print(result13)
"""
    Column1   Column2
A  1.448809 -0.208583
B  0.673197 -0.102751
C -1.732890 -0.598243
"""

result14 = df.loc[:,"Column1":"Column3"]
print(result14)
"""
    Column1   Column2   Column3
A -0.850390  0.232947 -0.822144
B -0.400516 -1.273642 -1.608072
C  0.185524 -2.418827 -0.108078
"""

result15 = df.loc[:,:"Column2"]
print(result15)
"""
    Column1   Column2
A  0.281601  0.750752
B  1.288250 -0.430473
C -1.225340  0.305035
"""


result15 = df.loc["A":"B",:"Column2"]
print(result15)
"""
   Column1   Column2
A -0.16818 -1.195427
B -0.83255  0.090174
"""


result16 = df.loc[:"B",:"Column2"]
print(result16)
"""
    Column1   Column2
A  0.230350  1.208011
B -0.775674 -0.950232
"""

################## iloc[] ##################
# burdaki kullanım loc[] ile aynı am iloc[] row bilgisini int sayılarla almak için kullanılır loc["A"] yerine iloc[0] gibi , "A" 
# loc["A":"B"] yerine iloc[0:1] gibi

result17 = df.iloc[2]  # loc["C"] ile aynı kullanım ama 
print(result17)
"""
Column1    1.870715
Column2    0.152633
Column3   -0.572221
Name: C, dtype: float64
"""

result18 = df.iloc[0,1]   # "A" row u  "Column2" Column u
print(result18)    # -1.660365020988603


# result19 = df.iloc[0,"Column2"]   böyle bir kullanımbize hata verir iloc[] içindeki tüm veiler int olmalı.
# print(result19)




########################### row ve column eklme ve çıkarma ###################

df["Column4"] = pd.Series(randn(3), ["A","B","C"])  # burda yeni bir series oluşturdu ve df imimize ekledik.
print(df)
"""
    Column1   Column2   Column3   Column4
A  0.238118  0.035100 -0.303810  0.020650
B -0.655976 -0.876009 -1.583761 -2.074341
C -1.255689 -0.078234 -0.308673 -1.145387
"""


df["Column5"] = df["Column1"] + df["Column2"]  # Column1 ile Column2  yi toplayarak yeni bir series oluşturduk ve Column5 e eiştliyip yeni bir colummn ekledik.
print(df)
"""
    Column1   Column2   Column3   Column4   Column5
A  1.303227  1.731890  1.111715  0.793844  3.035117
B  1.387473 -1.761359 -1.500597 -1.375595 -0.373886
C -1.071239  0.802860  1.171439 -0.428985 -0.268379
"""


df["Column6"] = pd.Series(randn(3),["A","B","C"])
print(df)
"""
    Column1   Column2   Column3   Column4   Column5   Column6
A -0.301234 -0.160087 -0.538322  0.708845 -0.461321 -2.691493
B -0.996502  0.433835  0.846352  0.438109 -0.562667 -0.962958
C  0.272531  0.743593  1.018570  0.155955  1.016125  0.944193
"""


############# column silme

result19 = df.drop("Column6",axis=1)  # burda axis=1 diyerek yukardan aşağıya bir silme olduğunu belirityoruz.
print(result19)      # burda ki kullanımda df üzerinde bir değişikliğe sebep olmaz burda df den Columun6 nın çıkmış halşne aldı.
"""
    Column1   Column2   Column3   Column4   Column5
A  0.433021  0.491640  0.120664  0.015709  0.924662
B -0.197456 -0.094504  0.331264 -0.568447 -0.291960
C  0.600766  1.037869  0.225747  0.130628  1.638635
"""

print(df)  # burda herhangi bir değişiklik olmadı 
"""
    Column1   Column2   Column3   Column4   Column5   Column6
A  0.433021  0.491640  0.120664  0.015709  0.924662  0.579041
B -0.197456 -0.094504  0.331264 -0.568447 -0.291960  0.122643
C  0.600766  1.037869  0.225747  0.130628  1.638635  1.208820
"""
print("asdsasf")


result20 = df.drop("Column6",axis=1,inplace=True) # burda inplace=True  kullanımı df üzrinde değişikliğ neden olur.
#                              eğer inplace=False olduğunda result19 daki gibi bir kullanım olur ve yapılan işlemn df ye etkilemez.
print(df)  
"""
    Column1   Column2   Column3   Column4   Column5
A -1.504992  2.868114 -0.786264  0.926810  1.363122
B -0.202822 -0.461097 -0.506936  0.091379 -0.663919
C  2.409821  1.209949 -0.648258  2.112008  3.619770
"""


