name = 'İkbal'    
# ikbal 5 karakterli bir isim i = 0.karakter  k = 1. karakter ... l = 4, karakter saymaya 0 ile başlanıyor
surname = 'Karadeli' 
age = 19 
greeting = 'My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old'
#           123456789(10)...
length = len(greeting)
print(greeting)

print(greeting[0]) # (M) 
print(greeting[2]) # ( )
print(greeting[3]) # (n)

print(len(greeting)) # greeting ifadesinin kaç karakter olduğunu söyler

print(greeting[length-1]) # -1 yazdık çünkü 48 adet karakterimiz var sıfır da dahil yanı son karakter 47. oluyor

print(greeting[-1]) #  yukardeki ifadenin daha kısa hali

print(greeting[2:6])  # 2. indeksten başlar 6. indekse kadar gider ama 6. indeksi yazmaz

print(greeting[3:])  #3. indeksten başlar sonuna kadar gider
print(greeting[:16])  # baştan başlar son karkter 16. olur

print(greeting[2:40:2])  # 2 den 40. karaktere kadar git ama iki karakterde bir al 
print(greeting[13:40:3])  # 13 den başla 40. karaktere kadar git ama 3 karakterde bir al.
