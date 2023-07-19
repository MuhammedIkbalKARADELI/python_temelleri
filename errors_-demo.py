liste = ["1","2","3","4","5a","10b","abc","10","50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

for x in liste:
    try:
        result = int(x)
        print(result)
    except Exception:
        continue



# 2: Kullanıcı 'q' değerini girmedikce aladığınız her inputun sayı
#   olduğundan emin olunuz aksi halde hata mesajı yazın.
# deneme1 #
while True:
    try:
        x = input('Bir sayı giriniz:')
       
        if x == 'q':
            print('Çıkış yaptınız.')
            break
       
        x = int(x)
        print(x)
    except Exception:
        print('Bir sayı giriniz veya çıkış için "q" yazınız.')
    else: 
        break


# deneme2 #

while True:
    sayi = input('Sayi: ')
    if sayi == 'q':
        break

    try:
        result = float(sayi)
        print('Girdiğiniz sayi: ', result)
        break
    except Exception:
        print('Geçersiz sayı.')
        continue



# 3: Girilen parola içinde türkçe karakter hatası veriniz.
# denem 1 #
def check_word(word):
    import re
    if re.search("[İçöüşı]",word):
        raise Exception('Türkçe karakter içermemeli.')

while True:
    
    word = input('Kelime yazınız:')
    
    try:
        check_word(word)
    except Exception as ex:
        print(ex)
        print('Hata')
    else:
        break

# deneme 2 #

def checkPassword(parola):

    turkce_karakterler = 'şçıİğüö'

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError('Parola türkçe karakter içeremez.')
        else:
            pass
    print('Geçerli parola')

parola = input('Parola: ')

try: 
    checkPassword(parola)
except TypeError as err:
    print(err)



# 4: Faktoriyel fonksiyonu oluşturup fonksiyona gelen değer için
# hata mesajı yazın.
# deneme 1 #
# def factorial(num):
#     if num < 0:
#         raise Exception('negatif ve sıfır sayı girmeyiniz.')

#     result = 1
    
#     for i in range(1,num+1):
#         result *= i
#     print(result)
    

# while True:
#     sayi = input('Bir sayı giriniz.')
#     sayi = int(sayi)
#     try: 
#         print('sonuc: ')
#         factorial(sayi)
#     except Exception as ex:
#         print(ex)
#     else:
#         break

# deneme 2 # 

def factoriyal(x):
    x = int(x)

    if x < 0:
        raise ValueError('Negatif değer')

    result = 1
    for i in range(1,x+1):
        result *= i

    return result

for x in [5,10,20,-3,'10a',6,8]:
    try:
        y = factoriyal(x)
    except Exception as err:
        print(err)
        continue
    print(y)

