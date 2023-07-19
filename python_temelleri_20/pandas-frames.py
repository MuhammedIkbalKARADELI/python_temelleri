import pandas as pd


df1 = pd.DataFrame()
print(df1)
"""
Empty DataFrame
Columns: []    
Index: [] 
"""
###################df with series#########################

s1 = pd.Series([1,2,3,4])
s2 = pd.Series([5,6,7,8])

data = dict(apples = s1, oranges = s2)

df2 = pd.DataFrame(data)

print(df2)
"""
   apples  oranges
0       1        5
1       2        6
2       3        7
3       4        8
"""


######################## normal ##############################

df3 = pd.DataFrame([1,2,3,4])
print(df3)
"""   burda row ve columun indexleri bilgisiyar tarafından verildi çünkü biz belirtmedik.
   0
0  1
1  2
2  3
3  4
"""

df4 = pd.DataFrame([["Ahmet",50],["Mehmet",70],["Veli",45],["Yasin",90]]) # burası matlabakine benziyor ; ile ikinci row u yazdırıyorduk ama burda [[a,b,c,d]] bir row 4 column olurken [[a,b,c,d],[x,y,z,q]] iki row 4 column oluyor 
print(df4)
"""
        0   1
0   Ahmet  50
1  Mehmet  70
2    Veli  45
3   Yasin  90
"""
################################List##############################

List = [["Ahmet",50],["Mehmet",70],["Veli",45],["Yasin",90]]



df5 = pd.DataFrame(List, columns=["Name","Grade"], index=[1,2,3,4])  # burda columun ve index  olark paramteleri belirttiğimizden istediğimiz sırada yazdık.
print(df5)
"""
     Name  Grade
1   Ahmet     50
2  Mehmet     70
3    Veli     45
4   Yasin     90
"""

df6 = pd.DataFrame(List,[1,2,3,4], ["Name","Grade"])  # burda columun ve index  olark paramteleri belirtmediğimizde ikinci sırada index bilgilerini yazdık üçüncğ sırada columun bilgilerini yazdık
print(df6)
"""
     Name  Grade
1   Ahmet     50
2  Mehmet     70
3    Veli     45
4   Yasin     90
"""


df7 = pd.DataFrame(List,[1,2,3,4], ["Name","Grade"], dtype = float) # burada ekstradan data türünüde vermiş olduk.
print(df7)
"""
     Name  Grade
1   Ahmet   50.0
2  Mehmet   70.0
3    Veli   45.0
4   Yasin   90.0
"""
#############################dict##########################

dict = {"Name": ["Ahmet","Ali","Yasin","Mehmet"], "Grade":[96,60,78,82] }


df8 = pd.DataFrame(dict)
print(df8)
"""
     Name  Grade
0   Ahmet     96
1     Ali     60
2   Yasin     78
3  Mehmet     82
"""


df9 = pd.DataFrame(dict,index=["212","475","964","274"])
print(df9)
"""
       Name  Grade
212   Ahmet     96
475     Ali     60
964   Yasin     78
274  Mehmet     82
"""



#############################dict_list#########################

dict_list = [   
                {"Name":"Ahmet","Grade":96},
                {"Name":"Ali","Grade":60},
                {"Name":"Yasin","Grade":78},
                {"Name":"Mehmet","Grade":92}
            ]


pd10 = pd.DataFrame(dict_list)
print(pd10)
"""
     Name  Grade
0   Ahmet     96
1     Ali     60
2   Yasin     78
3  Mehmet     82
"""


pd11 = pd.DataFrame(dict_list,index=["212","475","964","274"])
print(pd11)
"""
       Name  Grade
212   Ahmet     96
475     Ali     60
964   Yasin     78
274  Mehmet     92
"""

#######################################
print(pd11["Grade"])
"""
212    96
475    60
964    78
274    92
Name: Grade, dtype: int64
"""

print(pd11[["Grade","Name"]])
"""
     Grade    Name
212     96   Ahmet
475     60     Ali
964     78   Yasin
274     92  Mehmet
"""


