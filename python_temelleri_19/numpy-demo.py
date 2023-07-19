import numpy as np


# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturunuz.
result1 = np.array([10,15,30,45,60])
print(result1)
print(type(result1))

# 2- (5-15) arasındaki sayılara numpy dizisi oluşturunuz.
result2 = np.arange(5,15)
print(result2)

# 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.
result3 = np.arange(50,100,5)
print(result3)

# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.
result4 = np.zeros(10)
print(result4)

# 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz.
result5 = np.ones(10)
print(result5)

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.
result6 = np.linspace(0,100,5)
print(result6)

# 7- (10-30) arasında rastgele 5 tane tamsayı üretin.
result7 = np.random.randint(10,30,5)
print(result7)

# 8- [-1 ile 1] arasında 10 adet sayı üretin.
matris = np.random.randn(10)
print(matris)


# 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.
matris = np.random.randint(10,50,15).reshape(3,5)
print(matris)

# 10- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız.
rowSum = matris.sum(axis=1)
columnSum = matris.sum(axis=0)

print(rowSum)
print(columnSum)


# 11- Üretilen matrisin en büyük, en küçük ve ortalaması nedir?
min = matris.min()
max = matris.max()
mean = matris.mean()

print(min)
print(max)
print(mean)


# 12- Üretilen matrisin en büyük ve en küçük değerin indeksi kaçtır?

indexMin = matris.argmin()
indexMax = matris.argmax()

print(indexMin)
print(indexMax)


# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.

arr = np.arange(10,20)
print(arr)
print(arr[:3])


# 14- Üretilen dizinin elemanlarını tersten yazdırınız.

result9 = arr[::-1]
print(result9)


# 15- Üretilen matrisin ilk satırını seçiniz.
result10 = matris[0]
print(result10)

# 16- Üretilen matrisin 2.satırı 3.sütündak elemanı hangisidir.
result11 = matris[1,2]
print(result11)

# 17- Üretilen matrisin tüm satırdaki ilk elemanı seçiniz.
result12 = matris[:,0]
print(result12)

# 18- Üretilen matrisin her bir elemanın karesini alınız.
result13 = matris ** 2
print(result13)

# 19- Üretilen matris elemanlerının hangisi pozitif çift sayıdır? 
#     Aralığı (-50,50) arasında yazınız.

matris2 = np.random.randint(-50,50,15).reshape(3,5)
print(matris2)

result14 = matris2 % 2 == 0
print(result14)

result15 = matris2[result14]
print(result15)

result16 = result15 > 0
print(result16)

result17 = result15[result15 > 0]
print(result17)





