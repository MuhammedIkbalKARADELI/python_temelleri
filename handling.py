# # error handling

# try:
#     x = int(input('X: '))
#     y = int(input('y: '))
#     print(x/y)
# except ZeroDivisionError:
#     print('y must not be 0.')
# except ValueError:
#     print('enter a vale number for x and y') 


# try:
#     a = int(input('a: '))
#     b = int(input('b: '))
#     print(a/b)
# except (ZeroDivisionError, ValueError):
#     print('Wrong value was entered:')



# try: 
#     c = int(input('c: '))
#     d = int(input('d: '))
#     print(d/c)
# except ZeroDivisionError as z:
#     print('c ye Sıfır değere girmeyiniz.')
#     print(z)  # division by zero  



# try:
#     a = int(input('a: '))
#     b = int(input('b: '))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as e:
#     print('Wrong value was entered:')
#     print(e) # burda yukarda ilk hangi hata yapılırsa onun hata yazısını gönderiyor.


# try:
#     a = int(input('a: '))
#     b = int(input('b: '))
#     print(a/b)
# except:  # burda her hatada aşağıdaki yazıyı yazar ama hata türünü göremeyiz.
#     print('Wrong value was entered:')
    

# try:
#     z = int(input('z: '))
#     w = int(input('w: '))
#     print(z/w)
# except:
#     print('erong walue was entered')
# else:
#     print('Herşey yolunda.')  # eğer hata yoksa bu çalışır.



while True:
    try:
        z = int(input('z: '))
        w = int(input('w: '))
        print(z/w)
    except Exception as ex: #hataların toplandıgı başlık altı
        print('erong walue was entered')
        print(ex)
    else:  # burda else in amacı whli döngüsünü durdurmak için kullanıldı.
        print('Herşey yolunda.') 
        break
    finally:
        print('try except was ended') # bu blok her zman çalışır.

