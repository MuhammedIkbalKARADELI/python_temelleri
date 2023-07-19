# Dosya Açmak için ve oluşturmak için open() fonksiyonu kullanılır
# Kullanımı: open(dosya_adi,dosya_erişim_modu)
# Dosya_erişim_modu => Dosyayı hangi amaçla açtığımızı belirtir.



# "w": (Write) yazma modu. Dosyayı konumda oluşturur.
#    ** Dosayayı konumda oluşturur.
#    ** Dosya içeriğini siler ve yeniden ekleme yapar.

# file = open("newfile.txt","w")
# print(file)    # <_io.TextIOWrapper name='newfile.txt' mode='w' encoding='cp1254'>
# file.close()

#file = open("C:/Users/User/Desktop/newFile.txt","w")   ((bu komutla ilgili adrese bir .txt uzantılı bir dosya açmış olduk.))
#file.close()

#file = open("newfile.txt","w",encoding="utf-8")  # bu komut "w" her çalıştığı zaman ilgili dosya içindeki veriler silinir ve bu komuttan sonra istenilen bilgileri aktarır.
#                               yukardaki encoding="utf-8" tanımlı olmayan karakterleri tanımlı hale getirir. (öçüğıİ)gibi.
#file.write("İkbal KARADELİ\n")  # "\n" bundan sonra gelen karakter yeni satıra yazar.
#file.write("Muhamme İKbal KARADELİ")
#file.close()



# "a": (Append) ekleme. Dosya konumda yoksa oluşturlur.

#file = open("newfile.txt","a",encoding="utf-8") # burdaki kullanım "a" istenilen veriyi ilgili dosyaya eklme yapar.
#file.write("\nAyşe Fatma Veli")
#file.close()



# "x": (Create) oluşturm. Dosya zaten varsa hata verir.

#file = open("newfile2.txt","x",encoding="utf-8") # yeni bir dosya oluşturur.
#file.close()




# "r": (Read) okuma. Varsayılan. dosya konumda yoksa hata verir.








# file = open("newfile3.txt","w",encoding="utf-8")
# file.write("1234567890abcdefgğhıijklmnoprsştuüqxwyz\n")
# file.close()




file = open("newfile4.txt","a",encoding="utf-8")
file.write("İkbal KARADELİ \n")
file.write("ümit KARADELİ \n")
file.write("Ayşe KARADELİ \n")
file.write("Esra KARADELİ \n")
file.close()

files = open("newfie4.txt","r",encoding="utf-8")
names = files.read()
print(names)
files.close()