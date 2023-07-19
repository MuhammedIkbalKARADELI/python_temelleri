import pandas as pd

df = pd.read_csv("imdbTop250.csv")
#print(df)



# 1- Dosyada hakkındaki bilgiler.
result1 = df.info()
#print(result1)
result4 = df.info
#print(result4)
result2 = df.columns # burdak ikullanımda columns bilgilerini bize verir. 
print(result2)


# 2- ilk 5 kaydı gösterin
result3 = df.head()
#print(result3)


# 3- ilk 10 kaydı gösterin
result5 = df.head(10)
#print(result5)


# 4- son 5 kaydı gösterin
result6 = df.tail()
#print(result6)



# 5- son 10 kaydı gösterin 
result7 = df.tail(10)
#print(result7)


# 6- sadece Movi_Title kolonunu alın
result8 = df["Title"]
#print(result8)



# 7- sadece Movie_Title kolonunu içeren ilk 5 kaydı alın
result9 = df["Title"].head()
#print(result9)


 
# 8- sadece Movie_Title ve Rating kolonunu içeren ilk 5 kaydı alın
result10 = df[["Title","Rating"]].head()
#print(result10)


 
# 9- sadece Movie_title ve Rating kolonunu içeren son 7 kaydı alın
result11 = df[["Title","Rating"]].tail(7)
#print(result11)



# 10- sadece Movie_title ve Rating kolonunu içeren ikinci 5 kaydı alın
result12 = df[5:][["Title","Rating"]].head()
#print(result12)



# 11- Sadece Movie_Title ve Rating kolonunu içeren ve imdb puanı 8.0 
# ve üstü olan kayıtlardan ilk 50 tanesini alınız.
result13 = df[df["Rating"]>=8.0][["Title","Rating"]].head(50)
#print(result13)



# 12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimleri getiriniz.
result14 = df[(df["Date"]<2015) & (df["Date"]>=2014)][["Title","Date"]]
#print(result14)



# 13- Değerlendirme sayısı (Num_Reviews) 1.000.000 den büyük ya da imdb puanı 
#     8 ile 9 arasında olan filmleri listeleyiniz.
result15 = df[(df["Votes"] >= 1000000) | ((df["Rating"] < 9.0) & (df["Rating"] >= 8.0 ))][["Title","Votes","Rating"]].head(50)
print(result15)