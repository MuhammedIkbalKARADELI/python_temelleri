import math

#value = dir(math)  # bu bize math ile kullanabileceğimiz func ları gösterir
#value = help(math) # burda bu func ların kullanımını ve ne işe yaradaklarını gösteriyor.
value = help(math.factorial) 
print(value)

deger = math.sqrt(49)
print(deger)

deger1 = math.factorial(5)
print(deger1)

deger2 = math.floor(5.9)
print(deger2)

deger3 = math.ceil(4.1)
print(deger3)


print('Kullanım 2'.center(60,'*'))

import math as islem  # burda yaptığımız şey math a takma ad tanımladık.

value1 = islem.factorial(8)
print(value1)

value2 = islem.ceil(8.1)
print(value2)

value3 = islem.sqrt(36)
print(value3)

print('Kullanım 3'.center(60,'*'))

from math import *  # math kütüphanesindeki hepsini import et demek.

sonuc = factorial(5)
print(sonuc)

sonuc1 = ceil(6.2)
print(sonuc1)

sonuc2 = sqrt(64)
print(sonuc2)


from math import factorial,sqrt  # burda ikitane func import ettik.

result1 = sqrt(64)
print(result1)

result2 = factorial(5)
print(result2) 


print('Ozellik'.center(60,'*'))

def sqrt(x):
    print(f'x : {x}')

from math import sqrt   # buda kendimiz sqrt func tanımamıza rağmen math daki import edilen sqrt kullanıldı çünkü en son o tanımlandığı için 
urun1 = sqrt(64)
print(urun1)


from math import factorial  # burda kend tanımladığımız func en sonda olduğundan en sondaki func kabul ediyor.
def factorial(x):
    print('x: ', x)

factorial(8)


