import random

#result = dir(random)
#print(result)

#result = help(random)
#print(result)

result = random.random() # 0.0 - 1.0 arası bir sayı verirr.
print(result)

result = random.random() * 100
print(result)

result = int(random.uniform(1,10))
print(result)

result = int(random.uniform(10,100)) # 1 ile 100 arasında flooat bir sayı verir ondan başına int e çeviriyoruz.
print(result)

result = random.randint(1,100) # int olarak bize sayı verir 1 ile 100 arasında.
print(result)


names = ['Ali', 'Yağmur', 'Deniz', 'Cenk']

result1 = names[random.randint(0,len(names)-1)]
print(result1)

result2 = random.choice(names)  # result1 ile kullanım aynıdır.
print(result2) 


greeting = 'Hello there.'

result1 = greeting[random.randint(0,len(names)-1)]
print(result1)

result2 = random.choice(greeting)  # result1 ile kullanım aynıdır.
print(result2)


liste = list(range(10))
print(liste)

random.shuffle(liste) # liste içindeki tüm elemanların yerleri değişti ve listemize yeni bir değer oluşturmuş olduk. 
print(liste)  #burdan sonra liste orjinaline ulaşamayız. yani yeni bir değer atamış oluruz.


liste2 = range(100)

result = random.sample(liste2,3) # yukarda oluşturduğumuz lste2 den üç tane rastgele sayı seçti.
print(result)

result = random.sample(names,2)  # names içersinden rastgele iki karakter seçti.
print(result)


