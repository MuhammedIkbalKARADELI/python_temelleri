
# 1- girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
'''
sayı = int(input('sayı: '))

if sayı>0 and sayı<100:
    print('girdiğiniz sayı 0-100 arsındadır.')
else:
    print('girdiğiniz sayı 0-100 arasında değildir.')
'''


# 2- Girilen bir syının pozitif çift sayı olup olmadığını kontrol ediniz.

'''
sayı = int(input('sayı: '))

if sayı>0:
    if sayı%2 == 0:
        print('girilrn sayı pozitif çift sayıdır.')
    else:
        print('girilen sayı pozitif tek sayıdır.')
else:
    if sayı%2 == 0:
        print('girilen sayı negatif çift sayıdır.')
    else:
        print('girilen sayı negatif tek sayıdır.')
'''


# 3- Email ve parola bilileri ile giriş kontrolü yapınız.
'''
email = 'email@sadikturan.com'
password = 'abc123'

girilenEmail = input('email: ')
girlenPassword = input('password: ')

if email==girilenEmail:
    if password==girlenPassword:
        print('Hoş Geldiniz.')
    else:
        print('Girilen şifre yanlış.')
else:
    print('Girdiğiniz email adresiniz yanlış.')
'''


# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

'''
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a>b and a>c:
    print('a en büyük sayıdır.')
elif b>a and b>c:
    print('b en büyük sayıdır.')
elif c>a and c>b:
    print('c en büyük sayıdır.')
'''


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) noyunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortalama50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 aldığında ortalmanın önemi olmasın.
'''
vize1 = int(input('1. vize notunuz: '))
vize2 = int(input('2. vize notunuz: '))
final = int(input('final: '))

ortalama = (((vize1 + vize2)/2) * 0.6)  + (final * 0.4)

**
if ortalama >= 50:
    if final >= 50:
        print(f'aldığınız not ortalamanız {ortalama} ve sınıfı geçmiş bulunmaktasınız.' )
    else:
        print(f'aldığınız ortlamanız {ortalama}dır ama finalden aldığınız {final} notundan dolayı kaldınız.')
else:
    print(f'aldığınız ortalamanız {ortalama}dır bu yüzden kaldınız.')

***
if ortalama >= 50:
    print(f'aldığınız not ortalmanız {ortalama} dır ve bölümü geçmiş bulunmaktasınız.')
else:
    if final >= 70:
        print(f'not ortalamanız {ortalama}dır fakat final notunuz sayesinde geçmiş bulunmaktasınız.')
    else:
        print('malesef bölümden kaldınız.')
'''


# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (kilo / boy uzunluğunun karesi)     
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4 => zayıf
#    18.5-24.9 => normal
#    25-29.9 => fazla kilolu
#    30-34.9 => şişman (obez)
'''
name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('booyunuz: '))

index = kg / (hg ** 2)

if (index>=0) and (index<=18.4):
    print('yaptığımız hesaplara göre vücut kütle indeksiniz {index} dir ve zayıf gurubuna girmektesiniz.')
elif (index>=18.5) and (index<=24.9):
    print('yaptığımız hesaplara göre vücut kütle indeksiniz {index} dir ve normal gurubuna girmektesiniz.')
elif (index>=25.0) and (index<=29.9):
    print('yaptığımız hesaplara göre vücut kütle indeksiniz {index} dir ve kilolu gurubuna girmektesiniz.')
elif (index>= 30.0) and (index<=34.9):
    print('yaptığımız hesaplara göre vücut kütle indeksiniz {index} dir ve şişman gurubuna girmektesiniz.')   
else:
    print('tanımlanmamış indeks aralığı')
'''




