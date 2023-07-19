import pandas as pd
import numpy as np


data = {
    'Çalışan': ["Ahmet Yılmaz","Can Ertürk","Hasan Korkmaz","Cenk Saymaz","Ali Turan","Rıza Ertürk","Mustafa Can"],
    'Departman' : ["İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları"],
    'Yaş' : [30,25,45,50,23,34,42],
    'Semt' : ["Kadıköy","Tuzla","Maltepe","Tuzla","Maltepe","Tuzla","Kadıköy"],
    'Maaş' : [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(data)
print(df)
"""
         Çalışan         Departman  Yaş     Semt  Maaş
0   Ahmet Yılmaz  İnsan Kaynakları   30  Kadıköy  5000
1     Can Ertürk       Bilgi İşlem   25    Tuzla  3000
2  Hasan Korkmaz          Muhasebe   45  Maltepe  4000
3    Cenk Saymaz  İnsan Kaynakları   50    Tuzla  3500
4      Ali Turan       Bilgi İşlem   23  Maltepe  2750
5    Rıza Ertürk          Muhasebe   34    Tuzla  6500
6    Mustafa Can  İnsan Kaynakları   42  Kadıköy  4500
"""


result1 = df["Maaş"].sum() # burda maaş columuns daki elemanları toplmaış oldu
print(result1)  #29250

result2 = df.groupby("Departman") # departmanı aynı olanlara göre gruplama yapar.
print(result2)  # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001753EED06A0>

result3 = df.groupby("Departman").groups
print(result3)   # {'Bilgi İşlem': [1, 4], 'Muhasebe': [2, 5], 'İnsan Kaynakları': [0, 3, 6]} 
  
result4 = df.groupby(["Departman", "Semt"]).groups  # ikili bilgilere göre gurplama yapar.
print(result4) # {('Bilgi İşlem', 'Maltepe'): [4], ('Bilgi İşlem', 'Tuzla'): [1], ('Muhasebe', 'Maltepe'): [2], ('Muhasebe', 'Tuzla'): [5], ('İnsan Kaynakları', 'Kadıköy'): [0, 6], ('İnsan Kaynakları', 'Tuzla'): [3]} 


semtler = df.groupby("Semt")
for name, group in semtler:  # name kısmı yukarda gruplama yaptığımız nesnenin adı.
    print(name)
    print(group)

"""
Kadıköy
        Çalışan         Departman  Yaş     Semt  Maaş
0  Ahmet Yılmaz  İnsan Kaynakları   30  Kadıköy  5000
6   Mustafa Can  İnsan Kaynakları   42  Kadıköy  4500
Maltepe
         Çalışan    Departman  Yaş     Semt  Maaş
2  Hasan Korkmaz     Muhasebe   45  Maltepe  4000
4      Ali Turan  Bilgi İşlem   23  Maltepe  2750
Tuzla
       Çalışan         Departman  Yaş   Semt  Maaş
1   Can Ertürk       Bilgi İşlem   25  Tuzla  3000
3  Cenk Saymaz  İnsan Kaynakları   50  Tuzla  3500
5  Rıza Ertürk          Muhasebe   34  Tuzla  6500
"""


departman = df.groupby("Departman")
for name, group in departman:  # name kısmı yukarda gruplama yaptığımız nesnenin adları.
    print(name)
    print(group)

"""
Bilgi İşlem
      Çalışan    Departman  Yaş     Semt  Maaş
1  Can Ertürk  Bilgi İşlem   25    Tuzla  3000
4   Ali Turan  Bilgi İşlem   23  Maltepe  2750
Muhasebe
         Çalışan Departman  Yaş     Semt  Maaş
2  Hasan Korkmaz  Muhasebe   45  Maltepe  4000
5    Rıza Ertürk  Muhasebe   34    Tuzla  6500
İnsan Kaynakları
        Çalışan         Departman  Yaş     Semt  Maaş
0  Ahmet Yılmaz  İnsan Kaynakları   30  Kadıköy  5000
3   Cenk Saymaz  İnsan Kaynakları   50    Tuzla  3500
6   Mustafa Can  İnsan Kaynakları   42  Kadıköy  4500
"""


result5 = df.groupby("Semt").get_group("Kadıköy")
print(result5)
"""
        Çalışan         Departman  Yaş     Semt  Maaş
0  Ahmet Yılmaz  İnsan Kaynakları   30  Kadıköy  5000
6   Mustafa Can  İnsan Kaynakları   42  Kadıköy  4500
"""

result6 = df.groupby("Departman").get_group("Muhasebe") # Departmana göre gruplanan yerden muhasebe grubunu alıyoruz.
print(result6)
"""
         Çalışan Departman  Yaş     Semt  Maaş
2  Hasan Korkmaz  Muhasebe   45  Maltepe  4000
5    Rıza Ertürk  Muhasebe   34    Tuzla  6500
"""

result7 = df.groupby("Departman").sum()
print(result7)  # burda tabi yaş ksımınıda toplamış bulunmakta.
"""
                  Yaş   Maaş
Departman
Bilgi İşlem        48   5750
Muhasebe           79  10500
İnsan Kaynakları  122  13000
"""

result8 = df.groupby("Departman").sum()["Maaş"]
print(result8)
"""
Departman
Bilgi İşlem          5750
Muhasebe            10500
İnsan Kaynakları    13000
Name: Maaş, dtype: int64
"""

result9 = df.groupby("Departman").mean()  # departman göre gurupladıktan sonra burdaki yaş ve maaş ortlamasını vermiş olduk.
print(result9) 
"""
                        Yaş         Maaş
Departman
Bilgi İşlem       24.000000  2875.000000
Muhasebe          39.500000  5250.000000
İnsan Kaynakları  40.666667  4333.333333
"""

result10 = df.groupby("Departman")["Maaş"].mean()  
print(result10)
"""
Departman
Bilgi İşlem         2875.000000
Muhasebe            5250.000000
İnsan Kaynakları    4333.333333
Name: Maaş, dtype: float64
"""

result11 = df.groupby("Semt")["Yaş"].mean()  
print(result11)
"""
Semt
Kadıköy    36.000000
Maltepe    34.000000
Tuzla      36.333333
Name: Yaş, dtype: float64
"""


result12 = df.groupby("Semt")["Çalışan"].count()  
print(result12)
"""
Semt
Kadıköy    2
Maltepe    2
Tuzla      3
Name: Çalışan, dtype: int64
"""

result13 = df.groupby("Departman")["Yaş"].max()  
print(result13)
"""
Departman
Bilgi İşlem         25
Muhasebe            45
İnsan Kaynakları    50
Name: Yaş, dtype: int64
"""


result14 = df.groupby("Departman")["Maaş"].min()  
print(result14)
"""
Departman
Bilgi İşlem         2750
Muhasebe            4000
İnsan Kaynakları    3500
Name: Maaş, dtype: int64
"""

result15 = df.groupby("Departman")["Maaş"].min()["Muhasebe"]  
print(result15)   # 4000


result16 = df.groupby("Departman").agg(np.mean)  #  result9 = df.groupby("Departman").mean()   ile aynı görevi görecektir.
print(result16)
"""
                        Yaş         Maaş
Departman
Bilgi İşlem       24.000000  2875.000000
Muhasebe          39.500000  5250.000000
İnsan Kaynakları  40.666667  4333.333333
"""

result17 = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min])  
print(result17)
"""
                    sum         mean  amax  amin
Departman
Bilgi İşlem        5750  2875.000000  3000  2750
Muhasebe          10500  5250.000000  6500  4000
İnsan Kaynakları  13000  4333.333333  5000  3500
"""

result18 = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["Muhasebe"]  
print(result18)
"""
sum     10500.0
mean     5250.0
amax     6500.0
amin     4000.0
Name: Muhasebe, dtype: float64
"""




