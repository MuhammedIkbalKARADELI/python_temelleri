### 1 ###
# name = input('Adınız: ').title()
# age = int(input('Yaşınız: '))
# grade = input('Eğitim durumuznuz: ').title().strip()

# if age >= 18:
#     if grade == 'Üniversite' or grade == 'Lise':
#         print(f'{name} ehliyet almaya hak kazandı.')
#     else:
#         print(f'{name} eğitim durmunuz yetersiz.')
# else:
#     print(f'{name} yaşınız ehliyet almaya uygun değildir.')



### 2 ###
# import datetime 

# tarih = input('Trafiğe çıkış tarihini giriniz (2020/8/9): ')
# tarih = tarih.split('/')
# trafik = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

# simdi = datetime.datetime.now()

# fark = simdi - trafik

# days = fark.days
# print(days)



### 3 ###
# urunler  = []

# adet = int(input('Kaç adet ürün gireceksiniz: '))

# i = 0
# while i < adet:
#     name = input('Ürün adı: ')
#     price = input('Ürün fiyat: ')
#     urunler.append({
#         'name': name,
#         'price': price
#     })
#     i += 1

# for urun in urunler:
#     print(f'Ürün adı {urun["name"]} fiyatı {urun["price"]}')   


### 4 ###
# import random
# sayi = random.randint(1,10)
# hak = 5
# i = 0

# while i < hak:
#     i += 1
#     num = int(input('Enter a number from 1 to 10: '))
   
#     if num == sayi:
#         print('You win.')
#         break
#     elif num > sayi:
#         print('down')
#     else:
#         print('up')
    
#     if i == 5:
#         print('You do not have any right to countinuo') 


### 5 ###
# sayi = int(input('Enter a number to find out if number is prime or not: '))
# isprime = True

# if sayi == 1:
#     isprime = False

# for num in range(2,sayi):
#     if sayi % num == 0:
#         isprime = False
#         break

# if isprime:
#     print(f'{sayi} is prime number.')
# else: 
#     print(f'{sayi} is not a prime number.')
    


### 6 ###

# def selam(isim = 'user'):
#     print('Hello',isim)

# selam('ikbal')  # buradaki kullanımda bu fonksiyona çıkan sonuç aktarılmaz sadece sonucu yazdırır.


# def merhaba(name = 'user'):
#     return 'hello ' + name 

# a = merhaba('berk')  # burdaki 'return' lü kulanımda bizim oluşturduğumuz fon. na değer atar ve ordan o değeri kullana biliriz.
# b = merhaba('berk')[2:]

# print(a)
# print(b)


### 7 ###

# def changey(n):
#     n[0] = 'ada'

# name = ['Ali','mehmet','ahmet']
# k = name[:]
# y = name # burda adresi ortak yapa y ile name in adresini
# changey(k)
# print(name,'name ')
# print(k, 'k')
# changey(y)  # burda y'e yaptığımız işlemle name'i de etkilemiş oldu çünkü adreslerini eşitlemiştik.
# print(y,'y')
# print(name, 'name2')


### 8 ###

# a = sum((14,25)) # sum fon. içinde tuple şeklinde sayılar yazılmalı.  
# print(a)


### 9 ###

# def add(*params):
#     print(params)
#     return sum((params))

# print(add(12,13,13,15,16,51))


### 10 ###

#def user(**args):
#    print(args)
#    print(type(args))
#
#    for key, value in args.items():
#        print(f'{key} is {value}')
#
#user(name='ikbal',age=20,city='aydın')










