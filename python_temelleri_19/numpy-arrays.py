import numpy as np

result1 = np.array([1,3,5,7,9])   # bir dizi oluşturduk
result2 = np.arange(1,10) # [1,2,3,4,5,6,7,8,9]
result3 = np.arange(10,100,4) # [10 14 18 22 26 30 34 38 42 46 50 54 58 62 66 70 74 78 82 86 90 94 98]
result4 = np.zeros(10) #[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] # 10*1 bir matris olr
result5 = np.ones(10) # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

result6 = np.linspace(0,100,5) # verdiğimiz değerleri 5 eşit parçaya böler

result7 = result2.reshape(3,3)

result8 = np.random.randint(0,10) # bu kod her programı çalıştırdığında tekraradan bir sayı seçer.
result9 = np.random.randint(20) # başlangıç noktasını vermediğimizde bize yinede rastgele 20 ye kadar bir sayı verir.
result10 = np.random.randint(0,20,3) # 0 ile 20 arasından 3 sayı rastgele seçer.

result11 = np.random.rand(5) # 0ile 1 arasında rastgele 5 tane sayı üretecektir.
result12 = np.random.randn(5) #  0 ile 1 arasında 5 tane rastgele pozitif ve negatif sayı üretir 



print(result1)
print(result2)
print(result3)
print(result4)
print(result4.shape) # (10,) olur
print(result5)
print(result5.shape) # (10,) olur 
print(result6)
print(result7)
print(result8)
print(result9)
print(result10)
print(result11)
print(result12)



np_array = np.arange(50)
np_multi_array = np_array.reshape(5,10)
print(np_multi_array)
result13 = np_multi_array.sum(axis=1) # sum of row array(satır sayılarının toplamı)
result14 = np_multi_array.sum(axis=0) # sum of columun array(sütün sayılarının toplamı)
print(result13) 
print(result14) 




rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)

result15 = rnd_numbers.max() # oluşturduğumuz rastgle sayılardan en büyük değeri verir
result16 = rnd_numbers.min() # oluşturduğumuz rastgle sayılardan en küçük değeri verir
result17 = rnd_numbers.mean()  # oluşturduğumuz rastgle sayıların ortalmasın verir.
result18 = rnd_numbers.argmax()  # oluşturduğumuz rastgele 10 sayıdan maximum değerin indexini verir.
result19 = rnd_numbers.argmin()  # oluşturduğumuz rastgele 10 sayıdan minimum değerin indexini verir.

print(result15)
print(result16)
print(result17)
print(result18)
print(result19)


