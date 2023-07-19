
'''
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
a = int(input('Bir sayı giriniz: '))
result = (a<=100) and (0<a)  # True
print(result)

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
b = int(input('Bir sayı tekrar giriniz: '))
result1 = (b>0) and (b%2==0)  # True
print(result1)  

# 3- Email ve parola bilgileri ile giriş kontrolü yapıız.
email = 'gmail@karadeli.com'
password = 'abc123'

girilenEmail = input('Email:')
girilenPassword = input('Pasword')

#email==girilenEmail.lower().strip()
#password==girilenPassword.lower().strip()

result2 = (email==girilenEmail.lower().strip()) and (password==girilenPassword.lower().strip())
print(f'gidiğiniz bilgilere göre hesabınıza girme durumuznuz:{result2} ')


# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

q = int(input('q: '))
w = int(input('w: '))
z = int(input('z: '))

result3 = (q>w) and (q>z)
print(f'q en büyük sayı mıdır?: {result3}')

result3 = (w>q) and (w>z)
print(f'w en büyük sayı mıdır?: {result3}')

result3 = (z>w) and (z>w)
print(f'z en büyük sayı mıdır?: {result3}')


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) ortalma 50 olsa bile final notu en az 59 olmalıdır.
#    b-) Finalden 70 aldığında ortalamanın önemli olmasın.
 
vize1 = float(input('1.vize: '))
vize2 = float(input('2. vize: '))
final = float(input('final: '))

ort = ((vize1 + vize2) / 2) * 0.6 + 0.4 * final

print(f'not ortalamanız {ort} dur ve bu sistemde geçme durumuznuz: {ort >= 50}  ')

# a-)
şart = (ort>=50) and (final>=59)
print(f'geçme notunuz {ort} dur ve yeni değerlendirme sistemine göre geçme durumunuz: {şart}')

# b-)
şart2 = (ort>=50) or (final>=70)
print(f'geçme notunuz {ort} dur ve ikinci yeni değerlendirme sistemine göre geçme durumunuz: {şart2}')
'''

# 6- Kişinin ad, sayad, kilo ve boy bilgilerini alıp kilo indexlerini hesplayınız. 
#    Formül . (kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gurub agirmektedir.
#    0-18.4       => Zayıf
#    18.5-24.9    => Normal
#    25.0-29.9    => Fazla Kilolu
#    30.0-34.9    => Şişman 

name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('booyunuz: '))

index = kg / (hg ** 2)

zayıf = (index>=0) and (index<=18.4)
normal = (index>=18.5) and (index<=24.9)
kilolu = (index>=25.0) and (index<=29.9)
şişman = (index>= 30.0) and (index<=34.9)


print(f'{name} kiloindexin: {index} ve kilo değerlendirmen zayıf: {zayıf}')
print(f'{name} kiloindexin: {index} ve kilo değerlendirmen normal: {normal}')
print(f'{name} kiloindexin: {index} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{name} kiloindexin: {index} ve kilo değerlendirmen şişman: {şişman}')

