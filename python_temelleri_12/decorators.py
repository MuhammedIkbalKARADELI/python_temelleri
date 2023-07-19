# decorators fonksionlarını, fonksiyona özellik eklmek istediğimiz zaman kullanıyoruz.


####################1.1##################
# def my_decorator(func):
#     def wrapper():
#         print("Fonksiyondan önceki işlemler.")
#         func()
#         print("Fonksiyondan sonraki özellikler.")
#     return wrapper


# def sayHello():
#     print("Hello")


# sayHello = my_decorator(sayHello)
# sayHello()

'''
Fonksiyondan önceki işlemler.
Hello
Fonksiyondan sonraki özellikler.
olrak sonuç gelir.
'''


#####################1.2######################
# yukardaki ile aynı amaç ama yöntemleri farklı.

# def my_decorator(func):
#     def wrapper():
#         print("Fonksiyondan önceki işlemler.")
#         func()
#         print("Fonksiyondan sonraki özellikler.")
#     return wrapper

# sayHello = my_decorator(sayHello)  ile aynı göre görüyor ama '@' kullnım tanımlanan func un başında olmalı

# @my_decorator                   
# def sayHello():
#     print("Hello")

# sayHello()

'''
Fonksiyondan önceki işlemler.
Hello
Fonksiyondan sonraki özellikler.
aynı sonucu verir.
'''

##########################2.3############################
# burdaki kullanım dışarıdan alınan parametre olduğu zamanki kullanım şekli


# def my_decorator(func):
#     def wrapper(name):    
#         print("Fonksiyondan önceki işlemler.")
#         func(name)
#         print("Fonksiyondan sonraki özellikler.")
#     return wrapper


# @my_decorator                   
# def sayHello(name):
#     print("Hello",name)

# sayHello("Ali")

'''
Fonksiyondan önceki işlemler.
Hello Ali
Fonksiyondan sonraki özellikler.
olarak karşımıza gelir.
'''


#######################2.1#######################

import math
import time

def usalma(a,b):
    start = time.time()

    print(pow(a,b))

    time.sleep(1)
    finish = time.time()
    print("Fonksiyon "+ str(finish-start) + "saniye sürdü.")


def factorial(num):
    start = time.time()

    print(math.factorial(num))

    time.sleep(1)
    finish = time.time()
    print("Fonksiyon "+ str(finish-start) + " saniye sürdü.")

     
usalma(2,3)
factorial(8)


'''
cevabımız 
8
Fonksiyon 1.0085258483886719saniye sürdü.
40320
Fonksiyon 1.0109176635742188 saniye sürdü.
olur.

'''


#######################2.2###################
# burdaki kullanım yukardakş kullanımda her seferinde bşr başlangıç birde bitiş zamanı yaazdık onun yerine bir defa yazıcaz '@decorators' sayesinde

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        
        func(*args,**kwargs)
        
        time.sleep(1)
        finish = time.time()
        
        print("Fonksiyon "+ str(finish-start) + " saniye sürdü.")
    return inner
    

@calculate_time
def usalma(a,b):
    print(pow(a,b))

@calculate_time
def factorial(num):
    print(math.factorial(num))

     
usalma(5,3)
factorial(5)

'''
125
Fonksiyon 1.0094597339630127 saniye sürdü.
120
Fonksiyon 1.0100963115692139 saniye sürdü.
olarak burdan cevap alırız ve bu kullanımd 2.1 deki kullanımdan daha az kod yazdık.
'''
@calculate_time
def toplam(a,b):
    print(a+b)

toplam(5,9)

'''
14
Fonksiyon 1.0131685733795166 saniye sürdü.
olarak cevabımız alırız.
'''