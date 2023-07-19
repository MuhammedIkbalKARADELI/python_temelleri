"""
meyve_list ={}

meyve = input('Aldığınız meyvenin adı: ')
meyve_fiyat = input('Aldığınız meyvenin fiyatı: ')
meyve_kilo = input('Aldığınız meyvenin kilosu: ')


meyve_list.update({
    meyve: {
        'fiyat': meyve_fiyat,
        'kilo': meyve_kilo,
        'tutar': (int(meyve_fiyat) * int(meyve_kilo))  
    }
})

meyve = input('Aldığınız meyvenin adı: ')
meyve_fiyat = input('Aldığınız meyvenin fiyatı: ')
meyve_kilo = input('Aldığınız meyvenin kilosu: ')


meyve_list.update({
    meyve: {
        'fiyat': meyve_fiyat,
        'kilo': meyve_kilo,
        'tutar': (int(meyve_fiyat) * int(meyve_kilo))  
    }
})

meyve = input('Aldığınız meyvenin adı: ')
meyve_fiyat = input('Aldığınız meyvenin fiyatı: ')
meyve_kilo = input('Aldığınız meyvenin kilosu: ')


meyve_list.update({
    meyve: {
        'fiyat': meyve_fiyat,
        'kilo': meyve_kilo,
        'tutar': (int(meyve_fiyat) * int(meyve_kilo))  
    }
})

print('*'*100)



aldğınız_meyve = input('aldığınız meyve adı: ')
meyveler = meyve_list[aldğınız_meyve]
indirim = meyveler['tutar'] * 0.10

print(f"Sizin almış olduğunuz {aldğınız_meyve} nın fiyatı {meyveler['fiyat']} liradır ve tutarınız {meyveler['tutar'] - indirim} liradır. İyi günle dileriz. Mağzamıza tekrardan bekleriz. ")
"""
'''
import random
sayi = random.randint(1,10)
hak = int(input('hakkınızı belirtiniz: '))
i = hak
sayac = 0

while 0 < i:
    i-=1
    sayac+=1
    num = int(input('bir sayı giriniz: '))
    if num == sayi:
        print(f'Tebrikler {sayac}. defada bildiniz ve aldığınız puan:{100 - ((hak-(i+1))*(100/hak))} ve bulduğunuz sayı doğru')
        break    
    elif num<sayi:
        print('yukarı')
    else:
        print('aşağı')

    if i == 0:
        print(f'hakkınız bitmiştir ve tutulan sayı {sayi} dir. ') 
'''


a = 3
b = 2
a = b 


print(a+b)



