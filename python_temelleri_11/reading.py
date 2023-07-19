# try:
#     file = open("newfile.txt","r",encoding="utf-8") # Burda dosya adını yazdığımızda FileNotFoundError hatası vericektir ve biz bunu yönettik try exception ile.
#     print(file)
# except FileNotFoundError :
#     print("Dosya okuma hatası")
# finally:
#     print("Dosya kapandı.")
#     file.close()




# file = open("newfile.txt","r",encoding="utf-8")

# for i in file:  # burda dosyamızdaki bilgiler bize hep bir boşluk ile aktarılacaktı.
#      print(i)




# file = open("newfile.txt","r",encoding="utf-8")

# for i in file:
#     print(i,end="") # burdaki kullanımla boşlukları kaldırmış olacağız




# file = open("newfile.txt","r",encoding="utf-8")

# for i in file:
#     print(i,end="")  
                     
# for k in file:
#     print(k,end="")
# eğer burdaki gibi aynı kodu iki defa uygularsam .txt deki imleç nerdeyse ordan deva eder.




# file = open("newfile.txt","r",encoding="utf-8")

# content = file.read()
# print(content)            # istediğimiz dosyayı yazdırabiiyoruzz böylelikle.
# file.close()


#************** read()    *****************

# file = open("newfile.txt","r",encoding="utf-8")

# contenn1 = file.read()
# print("içerik 1")
# print(contenn1)

# contenn2 = file.read()
# print("içerik 2")
# print(contenn2)                  # burda içerik 2 den sonra harhangi bir bilgi gelmez çünkü tüm bilgiler doyadan conyenn1 de alındı ilmeç 
#                                  # dosyada sonda kalınca contenn2 ye herhangi bir bilgi kalamadı


# file = open("newfile.txt","r",encoding="utf-8")
# content = file.read(3)     # imleç dosyada işlem yapıldı yerde kaldığından sonraki işlemlerde kaldığı yerden devam eder.
# print(content) 
# content = file.read(4)
# print(content)
# content = file.read(5)
# print(content)
# content = file.read(6)
# print(content)
# content = file.read(9)
# print(content)
# content = file.read(8)
# print(content)
# content = file.read(11)
# print(content)
# content = file.read(17)
# print(content)
# content = file.read(7)
# print(content)

# file.close()


#************** readline()    *****************

# file = open("newfile.txt","r",encoding="utf-8")
# content = file.readline()    # dosyamızdaki satırı seçer ve print ile ayzdırırız. 
# print(content)
# content = file.readline()
# print(content)
# content = file.readline()
# print(content,end="")        # readline() metodu kendinden sonra bir satır boşluk bırakır. o yüzden end="" kullanırız.
# content = file.readline()
# print(content,end="")
# content = file.readline()
# print(content)
# content = file.readline()
# print(content)
# file.close()




#************** readlines()    *****************

# file = open("newfile.txt","r",encoding="utf-8")
# liste = file.readlines()

# print(liste) #['files.py konumundaki koddan geliyor.\n', 'İkbal KARADELİ\n', 'Muhamme İKbal KARADELİ\n', 'Ayşe Fatma Veli\n', 'Ayşe Fatma Veli']
# print(liste[1])  # İkbal KARADELİ
# print(liste[0])  # files.py konumundaki koddan geliyor.
# print(liste[4])  # Ayşe Fatma Veli
# file.close()