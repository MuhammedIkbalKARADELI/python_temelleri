

# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu 
#    lise ya da üniversite olmalıdır.

"""
name = input('adınız: ')
age = int(input('yaşınız: '))
education = input('eğitim durumunuz: ')
education = education.strip().lower() 

'''
if (age >= 18 and (education == 'lise' or education == 'üniversite')):
    print(f'{name} eliyet alabilirsin.')
else:
    print(f'{name} ehliyet alamazsınız')
'''
'''
if (age >= 18):
    if (education == 'lise' or education == 'üniversite'):
        print(f'{name} ehliyet alabilirsiniz.')
    else:
        print(f'{name} eğitim durumunuz yetersiz.')
else:
    print(f'{name} yaşın ehliyet için uygun değildir.')
'''
"""

# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre 
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0 -24 => 0
#    25 -44 => 1
#    45 -54 => 2
#    55 -69 => 3
#    70 -84 => 4
#    85 -100 => 5

"""
name = input('adınız: ')
yazılı_not1 = float(input('1. yazılı notunuzu giriniz: '))
yazılı_not2 = float(input('2. yazılı notunuzu giriniz: '))
sözlü = float(input('sözlü notunuzu giriniz: '))

ortalama = (yazılı_not1 + yazılı_not2 + sözlü) / 3

if (ortalama >= 0) and (ortalama < 25):
    print(f'{name} aldığınız ortalama {ortalama} ve karşılık gelen notunuz 0 dır.')
elif (ortalama >= 25) and (ortalama <45): 
    print(f'{name} aldığınız ortalamaya {ortalama} ve karşılık gelen notunuz 1 dir.')
elif (ortalama >= 45) and (ortalama <55): 
    print(f'{name} aldığınız ortalamaya {ortalama} ve karşılık gelen notunuz 2 dir.')
elif (ortalama >= 55) and (ortalama <70): 
    print(f'{name} aldığınız ortalamaya {ortalama} ve karşılık gelen notunuz 3 dir.')
elif (ortalama >= 70) and (ortalama <85): 
    print(f'{name} aldığınız ortalamaya {ortalama} ve karşılık gelen notunuz 4 dir.')
elif (ortalama >= 85) and (ortalama <= 100): 
    print(f'{name} aldığınız ortalamaya {ortalama} ve karşılık gelen notunuz 5 dir.')
else:
    print('yanlış bilgi girdiniz.')
"""



# 3- Trafiğe çıkış tarihi alınan bir aracım servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl
#    2. Bakım => 2. yıl
#    3. Bakım => 3. yıl
#   ** Süre hesabını alınan gün, aay, yıl bilgisine göre gün bazlı hesaplayınız
#  *** datetime modülünü  kullanmanız gerekiyor.

# **
'''
days = int(input('aracınız kaç gündür trafikte: '))

if days <= 365:
    print('1. servis aralığı')
elif days <= (365*2) and days > 365:
    print('2. servis aralığı')  
elif days > (365*2) and days <= (365*3):
    print('3.servis aralığı')
else:
    print('hatalı süre')
'''

import datetime

date = input('aracınız hangi tarihte trafiğe çıktı (xxxx/xx/xx): ')
date = date.split('/')
#print(date)  # ['2019', '9', '11']

startTrafic = datetime.datetime(int(date[0]),int(date[1]),int(date[2]))

now = datetime.datetime.now()
#print(now)  # 2020-09-19

fark = (now - startTrafic)
#print(fark) # 291 days, 15:40:18.870533

#print(fark.days) # 291

days = fark.days

if days <= 365:
    print('1. servis aralığı')
elif days <= (365*2) and days > 365:
    print('2. servis aralığı')  
elif days > (365*2) and days <= (365*3):
    print('3.servis aralığı')
else:
    print('hatalı süre')










