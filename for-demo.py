
sayilar =[1,3,5,7,9,12,19,21]

# 1- Sayılar listesindeki hangi sayılar 3'ün katıdır?

for x in sayilar:
    if x % 3 == 0:
        print(x)
'''
3
9
12
21
'''

# 2- Sayılar listesinden sayıların toplamı kaçtır?

toplam = 0

for y in sayilar:
    toplam = toplam + y  # =>  toplam += y 
    print(toplam)
'''
1
4
9
16
25
37
56
77
'''
#  print yazısını döngünün içine almayınca döngülerdeki tüm karakter için toplamı yazmaz

toplam2 =  0
for y in sayilar:
    toplam2 = toplam2 + y  # =>  toplam2 += y 
print(toplam)
'''
77
'''

# 3- Saylar listesindeki tek sayıların karesini alınız.
  
for z in sayilar:
    if z % 2 == 1:
        print(z**2)
'''
1
9
25
49
81
361
441
'''


sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# 4- Şehirlerden hangileri en fazla 5 karakterdir?

for w in sehirler:
    if len(w) <= 5:
        print(w)
'''
izmir
rize
'''



urunler = [
    {'name':'samsung S6','price':'3000'},
    {'name':'samsung S7','price':'4000'},
    {'name':'samsung S8','price':'5000'},
    {'name':'samsung S9','price':'6000'},
    {'name':'samsung S10','price':'7000'}
]

print(urunler)

# 5- Ürünlerin fiyatları toplamı nedir?

top = 0 

for urun in urunler:
    print(urun['price'])
'''
3000
4000
5000
6000
7000
'''

for urun in urunler:
    fiyat = int(urun['price'])
    top += fiyat
    print(top)
'''  
3000
7000
12000
18000
25000
'''
top2 = 0
for urun1 in urunler:
    fiyat = int(urun1['price'])
    top2 += fiyat
print(top)
'''  
25000
'''

# 6- Ürünlerin fiyatı en fazla 5000 olan ürünleri gösteriniz.

for urun2 in urunler:
    fiyat = int(urun2['price']) 
    if fiyat <= 5000:
        print(fiyat)
        print(urun2)
        print(urun2['name'])
'''
3000
{'name': 'samsung S6', 'price': '3000'}
samsung S6
4000
{'name': 'samsung S7', 'price': '4000'}
samsung S7
5000
{'name': 'samsung S8', 'price': '5000'}
samsung S8
'''



