import os
import datetime

# result = dir(os)
# print(result)

result = os.name  # nt sonucunu verir. ve bu benim bigisiyarımın windows olduğun söyler.
print(result)

# etkin dizisini  verir.
result = os.getcwd()     # C:\Users\User\Desktop\python work space\python_temelleri\python_temelleri_15 
print(result)            # bu dosyanın hangi adrest olduğunu gösterir.



# dizin etkinleştirme.
# os.chdir("C:\Users\useer\Desktop")  bu da yeni adrese yönlendirme yapar.bu kullanımdan sonra oluşturulan dosylar her seferinde burda belirteceğimiz adrese gider.


# os.chdir('..')  bir geri adrese geçiş yapar. 


# klasör oluşturm
# os.mkdir("newdirectory") # klosör aynı dizinin içersinde yeni dosya oluşur.

# os.makedirs("newdirectory/yeniKlasör")  # klasörün içersine yeni klasör oluşturur.

# os.rename("newdirectory", "yeniklasör")   # klasörün ismini yenisiyle değiştirir.

# os.rmdir("newdirectory")  # kalsörü siler. alt klasörü olmadığı zaman kullanılack bir durumda 

# os.removedirs("yeniKlasör/yeniKlasör") # alt dosyayı böylelikle silebiliyoruz.



#listeleme                  
result = os.listdir()    # klasörün içersinde olan dosyaları listeer bize verir.
print(result)            # ['date.py', '_os.py']


for dosya in result:
    if dosya.endswith('.py'):
        print(dosya)



###################2#################

information_about_folder = os.stat("date.py")         # dosya bilgilerini verir
print(information_about_folder)

size_folder = information_about_folder.st_size   # byte cinsinden değer gelir. 
print(size_folder)         # 3547


# oluşturlma tarihi
second_info_created = information_about_folder.st_ctime  # saniye cinsinden biir bilgi bize verir.  
print(second_info_created)         # 1626555085.5191047

date_info_created = datetime.datetime.fromtimestamp(second_info_created)  # dosyanın oluşturulduğu zamanın saniye cinsincen tarih bilgisine datetime modülü ile çeviririz.
print(date_info_created)                     # 2021-07-17 23:51:25.519105

# son erişilme tarihi
second_info_lasttime = information_about_folder.st_atime    # saniye cinsinden verir.
print(second_info_lasttime)            #1626599708.8916154

date_info_lasttime = datetime.datetime.fromtimestamp(second_info_lasttime)   # saniye verisini tarih verisine değiştirme.
print(date_info_lasttime)                   # 2021-07-18 12:15:08.891615


# değiştirilme terihi
second_info_change = information_about_folder.st_mtime
print(second_info_change)            # 1626599708.8843708

date_info_change = datetime.datetime.fromtimestamp(second_info_change) # saniye verisini tarih verisine değiştirme.
print(date_info_change)              # 2021-07-18 12:15:08.884371


####################3########################
#************ önemli kullanım ****************

#os.system("notepad.exe")  # bunu çalıştırdığımızda bu uyggulama açılır.



#####################4###############


# path 
# dosyanın adını değiştirme uazntsını değiştirme gibi işlemlerde kullanılır.


result = os.path.abspath("_os.py") # dosyanıın tam konumunu verir.
print(result)            # C:\Users\User\Desktop\python work space\python_temelleri\python_temelleri_15\_os.py

result = os.path.dirname("C:/Users/User/Desktop/python work space/python_temelleri/python_temelleri_15/_os.py")      #  ta konumu verilen dosyanın dizin ismini verir.
print(result)        # C:/Users/User/Desktop/python work space/python_temelleri/python_temelleri_15
# yukarda kullanımın bir nevi kısa yolu

result =  os.path.dirname(os.path.abspath("_os.py"))
print(result)        # C:\Users\User\Desktop\python work space\python_temelleri\python_temelleri_15


result = os.path.exists("_os.py")  # aradığı konumda istenilen dosya var mı bakar.
print(result)            # True


result = os.path.exists("C:/Users/User/Desktop/python work space/python_temelleri/python_temelleri_15/_os.py")
print(result)            # True

 
result = os.path.isdir("C:/Users/User/Desktop/python work space/python_temelleri/python_temelleri_15")     # bu adres klasörmüdür  sorusuna cevap verir.
print(result)       # True


result = os.path.isdir("C:/Users/User/Desktop/python work space/python_temelleri/python_temelleri_15/_os.py")     # bu adres klasörmüdür  sorusuna cevap verir.
print(result)         # bu klasör değildir bu bir python adresidir. # False


result = os.path.isfile("C:/Users/User/Desktop/python work space/python_temelleri/python_temelleri_15")     # bu adres dosyamıdır  sorusuna cevap verir.
print(result)        # bu klasördür dosya değil  # False


result = os.path.isfile("C:/Users/User/Desktop/python work space/python_temelleri/python_temelleri_15/_os.py")     # bu adres dosyamıdır  sorusuna cevap verir.
print(result)      #True



# result = os.path.join("C:\\","Deneme","Deneme1")  # bir yol oluşturabiliriz.


# result = os.path.split("C:\\Deneme") # bölebiliriz.



####################4#################
# önemli
result = os.path.splitext("_os.py")
print(result)         # ('_os', '.py')

result1 = result[0]
print(result1)       #  _os       

result2 = result[1]
print(result2)       # .py





