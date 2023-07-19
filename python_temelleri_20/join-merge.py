import pandas as pd


customers = {
    "CustomerID" : [1,2,3,4] ,
    "FistName" : ["Ahmet","Ali","Hasan","Canan"],
    "LastName" : ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

orders = {
    "OrderID" : [10,11,12,13],
    "CustomerID" : [1,2,5,7],
    "OrderDate" : ["2010-07-04","2010-08-04","2010-07-07","2010-07-04"]
}


df_customers  = pd.DataFrame(customers, columns = ["CustomerID","FistName","LastName"])
df_orders  = pd.DataFrame(orders, columns = ["OrderID","CustomerID","OrderDate"])

print(df_customers)
"""
   CustomerID FistName LastName
0           1    Ahmet   Yılmaz
1           2      Ali  Korkmaz
2           3    Hasan    Çelik
3           4    Canan   Toprak
"""
print(df_orders)
"""
   OrderID  CustomerID   OrderDate
0       10           1  2010-07-04
1       11           2  2010-08-04
2       12           5  2010-07-07
3       13           7  2010-07-04
"""


# inner join
inner_join = pd.merge(df_customers,df_orders,how="inner")  # siparişi olan bütün müşterileri getirmiş oluyoruz.
print(inner_join)
"""
   CustomerID FistName LastName  OrderID   OrderDate
0           1    Ahmet   Yılmaz       10  2010-07-04
1           2      Ali  Korkmaz       11  2010-08-04
"""



# left join
left_join = pd.merge(df_customers,df_orders,how="left")  # df_customer a göre bir birleştirme yapılıyor.
print(left_join)
"""
   CustomerID FistName LastName  OrderID   OrderDate
0           1    Ahmet   Yılmaz     10.0  2010-07-04
1           2      Ali  Korkmaz     11.0  2010-08-04
2           3    Hasan    Çelik      NaN         NaN
3           4    Canan   Toprak      NaN         NaN
"""

# right join
right_join = pd.merge(df_customers,df_orders,how="right")  # df_customer a göre bir birleştirme yapılıyor.
print(right_join)
"""
   CustomerID FistName LastName  OrderID   OrderDate
0           1    Ahmet   Yılmaz       10  2010-07-04
1           2      Ali  Korkmaz       11  2010-08-04
2           5      NaN      NaN       12  2010-07-07
3           7      NaN      NaN       13  2010-07-04
"""


# outer join
outer_join = pd.merge(df_customers,df_orders,how="outer")  # tüm customerID ileri birleştirir.ve tüm colunları birleştirir.
print(outer_join)
"""
   CustomerID FistName LastName  OrderID   OrderDate
0           1    Ahmet   Yılmaz     10.0  2010-07-04
1           2      Ali  Korkmaz     11.0  2010-08-04
2           3    Hasan    Çelik      NaN         NaN
3           4    Canan   Toprak      NaN         NaN
4           5      NaN      NaN     12.0  2010-07-07
5           7      NaN      NaN     13.0  2010-07-04
"""



customersA = {
    "CustomerID" : [1,2,3,4] ,
    "FistName" : ["Ahmet","Ali","Hasan","Canan"],
    "LastName" : ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB = {
    "CustomerID" : [4,5,6,7] ,
    "FistName" : ["Yağmur","Çınar","Cengiz","Can"],
    "LastName" : ["Bilge","Turan","Yılmaz","Turan"]
}


df_customersA  = pd.DataFrame(customersA, columns = ["CustomerID","FistName","LastName"])
df_customersB  = pd.DataFrame(customersB, columns = ["CustomerID","FistName","LastName"])

result = pd.concat([df_customersA,df_customersB])  #row göre birleştirme yapar.
print(result)
"""
   CustomerID FistName LastName
0           1    Ahmet   Yılmaz
1           2      Ali  Korkmaz
2           3    Hasan    Çelik
3           4    Canan   Toprak
0           4   Yağmur    Bilge
1           5    Çınar    Turan
2           6   Cengiz   Yılmaz
3           7      Can    Turan
"""


result1 = pd.concat([df_customersA,df_customersB],axis=1)  #row göre birleştirme yapar.
print(result1)
"""
   CustomerID FistName LastName  CustomerID FistName LastName
0           1    Ahmet   Yılmaz           4   Yağmur    Bilge
1           2      Ali  Korkmaz           5    Çınar    Turan
2           3    Hasan    Çelik           6   Cengiz   Yılmaz
3           4    Canan   Toprak           7      Can    Turan
"""