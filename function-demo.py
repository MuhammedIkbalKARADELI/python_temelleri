### 1 ###
# Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
print('Answer 1'.center(50,'*'))

def yazdir(kelime, adet):
    print(kelime * adet)
    print('\n')

yazdir('Hello\n', 10)
yazdir('Hello', 10)


### 2 ### 
# Kendine gönderilen sınırsız sayıdaki parametreyi bir lissteye çeviren fonksiyon yazın 
print('Answer 2'.center(50,'*'))

def listeCevir(*param):
    numbers =[]
    for x in param:
        numbers.append(x)
    print(numbers , '\n')

listeCevir(12,13,24,53,47,57,68,86,75,36)


### 3 ### 
# Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
print('Answer 3'.center(50,'*'))

def asalSayıBul(sayi1, sayi2):
    for num in range(sayi1, sayi2+1):
        if num >= 2:
            for x in range(2,num):
                if (num % x == 0):
                    break
            else:
                print(num)
                
sayi1 = int(input('Sayı 1: '))
sayi2 = int(input('Sayı 2: '))

asalSayıBul(sayi1, sayi2)


### 4 ### 
# Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.
print('Answer 4'.center(50,'*'))

def tamBolenBul(sayi):
    bolen = []
    for eleman in range(2,sayi):
        if (sayi % eleman == 0):
            bolen.append(eleman)
    print(bolen)
    return bolen

a = tamBolenBul(30) # return kullanarak 'a' ya  bu atamayı yapabildik.
print(a)
