

# 1- Girilen 2 sayıdan  hangisi büyükür? 
"""
a = int(input('1. sayı: '))
b = int(input('2. sayı: '))
büyükmüdür = a > b
print(f"a saysı: {a} ve b saysı: {b} dir. a nın b den büyük olma durumu: {büyükmüdür}")
#our result is => a saysı: 10 ve b saysı: 2 dir. a nın b den büyük olma durumu: True
"""



# 2- Kullanıcıdan 2 vize (%60) ve final(%40) notunu alıp ortalama hesaplıyınız. 
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
"""
vize1 = float(input('1.vize: '))
vize2 = float(input('2. vize: '))
final = float(input('final: '))

ortalama = (((vize1 + vize2)/2) * 0.6) + (final * 0.4)
print(f'Aldığınız notlar üzere blümü geçme durumunuz: {ortalama >= 50}')
# my result is = Aldığınız notlar üzere bölümü geçme durumunuz: False
"""


# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
"""
tekçift = int(input('bir sayı yazınız: '))
isTekçift = (tekçift % 2) == 0 
print(f'Yazdığınız sayının çif olma durumu: {isTekçift}')
#  my result is = Yazdığınız sayının çif olma durumu: True
"""


# 4- Girilen bir negatif pozitif olma durumunu yazdırın.
"""
pozitifnegatif = int(input('bir sayı yazınız: '))
ispozitifnegatif = pozitifnegatif > 0
print(f'yazdığınız sayı pozitif olma durumu: {ispozitifnegatif}')
# my result is = yazdığınız sayı pozitif olma durumu: True
"""


# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: email@ikbalkaradeli.com  parola: abc123)
"""  
email = 'email@ikbalkaradeli.com'
password = 'abc123'

girilenEmail = input('email: ')
girilenParola = input('password: ')

print(f'girdiğiniz email doğru olama durumu: {email == girilenEmail.lower().strip()} parolanuzun doğru olma durumu: {password == girilenParola.lower()} ')
"""