
'''  bizim başatan oluşturduumuz bir dosyaya 'r+' ile güncelleme yapacağız

    İkbal KARADELİ 
    ümit KARADELİ 
    Ayşe KARADELİ 
    Esra KARADELİ 


bunlara sahip bir doyaya güncelleme yapıyoruz.

'''

#*************1****************


# with open("newfile4.txt","r+",encoding="utf-8") as file:
#       file.write("deneme")     # bunu yapınca külüsör nerdeyse ordaki indexelere bizim istediğim şeyi güncelliyor.

# with open("newfile4.txt","r+",encoding="utf-8") as file:
#      print(file.read())

'''
        yukaradki kod ile külüsörün olduğu yere güncelleme yaptı.
    deneme KARADELİ 
    ümit KARADELİ   
    Ayşe KARADELİ   
    Esra KARADELİ 

'''
#not #
# eğer 'r+' yerine 'w' ile yapsaydık bu sefer dosyadaki tü bilgileri siler istediğimiz şeyi yazardı yani eleme yapmzadı.





#****************2****************

# with open("newfile4.txt","r+",encoding="utf-8") as file:
#     file.seek(20)            # külüsörün konumunu değiştirdik.
#     file.write("deneme")     # bunu yapınca külüsör nerdeyse ordaki indexelere bizim istediğim şeyi güncelliyor.

# with open("newfile4.txt","r+",encoding="utf-8") as file:
#     print(file.read())

'''  
İkbal KARADELİ 
AdenemeRADELİ
Ayşe KARADELİ
Esra KARADELİ

olarak değişime uğruyor.
'''


#*****************3*************
# with open("newfile4.txt","a",encoding="utf-8") as file:    # "a" dosyadaki bilginin ensonuna ekleme yapar. Append eder.
#     file.write("\nArife GÜLER")

# with open("newfile4.txt","r",encoding="utf-8") as file:
#     print(file.read())


''' 

İkbal KARADELİ 
AdenemeRADELİ
Ayşe KARADELİ
Esra KARADELİ
Arife GÜLER

olarak değişime uğrar.
'''

#****************4********************
#**************Sayfa başına güncelleme***********


# with open("newfile4.txt","r+",encoding="utf-8") as file:
#     content = file.read()
#     content = "Ummuhan KARADELİ\n" + content  # burda biz bilgilerimizi derleyip toparlayıp content e atmış olduk
#     file.seek(0)     # külüsörü başa aldık.
#     file.write(content)    # content e atmış olduğumuz bilgileri de dosyanın içine atıcağız 

# with open("newfile4.txt","r",encoding="utf-8") as file:
#     print(file.read())


'''
Ummuhan KARADELİ
İkbal KARADELİ
AdenemeRADELİ
Ayşe KARADELİ
Esra KARADELİ
Arife GÜLER
olarak güncellemiş olduk.
not: arife güler  3. başlıkta yaptığımız code dan geldi.

'''

#******************5***************
#************sayfa ortasına güncelleme**********************

# with open("newfile4.txt","r+",encoding="utf-8") as file:       # külüsör nerdeyse istediğimiz verileri oraya aktarıyor eski verideki bilgiyi kaydır mıyor  bizim atığımız veri ile eski verinin indexleri çakışırsa  yeniyi yazıyor.
#     list = file.readlines()
#     list.insert(1,"Cemil KARADELİ\n")      # isediğimiz cümleyi listede 1. indxe yerleştirir.
#     file.seek(0)  # dosyadaki külüsörü başa alık 
#     for i in list:
#         file.write(i)

# with open("newfile4.txt","r",encoding="utf-8") as file:
#     print(file.read())


'''
Ummuhan KARADELİ
Cemil KARADELİ    <- eklenmiş oldu.
İkbal KARADELİ
AdenemeRADELİ
Ayşe KARADELİ
Esra KARADELİ
Arife GÜLER
olarak değişir.


'''


#***************6*******************



with open("newfile4.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(6,"Erol GÜLER\n")
    file.seek(0) 
    file.writelines(list)         # bu kullanım 5. başlık için bir kısay yol .
 

with open("newfile4.txt","r",encoding="utf-8") as file:
    print(file.read())

'''
Ummuhan KARADELİ
Cemil KARADELİ
İkbal KARADELİ
Ümit KARADELİ
Ayşe KARADELİ
Esra KARADELİ
Erol GÜLER       <- eklenir.
Arife GÜLER

'''


