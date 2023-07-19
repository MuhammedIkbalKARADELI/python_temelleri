"""
sayilar = [1,3,4,7,9,12,19,21]


# 1- sayılar listesini while ile ekrana yazdırın.
i = 0

while i < len(sayilar):
    print(sayilar[i])
    i += 1



# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki 
#     tüm tek sayıları ekrana yazdırın.

başlangıç = int(input('bir sayı giriniz: '))
bitis = int(input('bir sayı giriniz: '))

r = başlangıç

while r < bitis:
    r += 1       # bunu buraya yazdık çünkü istenen şey: belitilen rakamalrın arasındaki sayıları istediğinden.
    if r % 2 == 1:
        print(f'tek sayı {r}')


# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın.

z = 100 
while z > 0:
    print(z)
    z -= 1

# 4- Kullanıcıdan alacağınız 5 sayıyı ekrana sıralı bir şekilde yazdırın.

# benim yapış şeklim
'''
numbers = []

numbers.append(int(input('bir sayı giriniz: ')))
numbers.append(int(input('bir sayı giriniz: ')))
numbers.append(int(input('bir sayı giriniz: ')))
numbers.append(int(input('bir sayı giriniz: ')))
numbers.append(int(input('bir sayı giriniz: ')))

numbers.sort()

x = 0

while x < len(numbers):
    print(numbers[x])
    x += 1
'''

numbers = []

x = 0

while x < 5:
    sayı = int(input('bir sayı giriniz: '))
    numbers.append(sayı)
    numbers.sort()
    x += 1 

print(numbers)

for num in numbers:
    print(num)
"""

# 5- kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içerisnde saklayınız.
#    * Ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    *** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin

urunler = []

adet = int(input('kaç adet ürün var: '))

q = 0

while q < adet:
    name = input('ürününzün adı: ')
    price = input('ürünüzün fiyatı: ')
    urunler.append({
        'name': name,
        'price': price
    })
    q += 1

print(urunler)

for urun in urunler:
    print(f'ürün adı: {urun["name"]} ürün fiyatı: {urun["price"]}')


top = 0
for urun in urunler:
    fiyat = int(urun['price'])
    top += fiyat

print(f'toplam tutarınız {top} liradır.')