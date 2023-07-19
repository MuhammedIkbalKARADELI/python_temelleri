numbers = [1, 10, 16, 4, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = min(numbers)  # 1
val = min(letters)  # a
val = max(numbers)  # 16
val = max(letters)  # y

val = numbers[3:4]  # [4, 10]
val = numbers[:3]   # [1, 10, 16]
val = numbers[4:]   # [10]
#print (val)

numbers[4] = 40   # [1, 10, 16, 40, 10]


numbers.append(59)  # [1, 10, 16, 40, 10, 59]


numbers.insert(3,8)  # [1, 10, 16, 8, 40, 10, 59]   3. indeks yerine yazılır sonrakiler bir sağa kaydırılır.
numbers.insert(5,78) # [1, 10, 8, 16, 40, 78, 10, 59]
numbers.insert(-1,52) # [1, 10, 8, 16, 78, 40, 10, 52, 59]  en yazılan list ifadesinde -1 inci indeksin tam olduğu yere yazıldı ve bir önceki list ifadesindeki -1 indeksi bir sağa kaydı.

#numbers.pop() # [1, 10, 8, 16, 78, 40, 10, 52]  en sondaki indeksi siler
#numbers.pop(-1) # [1, 10, 16, 8, 4, 78, 40, 10]
#numbers.pop(0)  # [10, 16, 8, 4, 78, 40, 10, 52]
# bu metodlarla işlem yaptıktan sonra terkrar işlem yapnıca enson yapılan işlemin üstüne deavm ediliyor. 

numbers.remove(59)  # [1, 10, 16, 8, 4, 78, 40, 52]  aradağımız karakteri list içinden bulur ve çıkartır.

numbers.sort() # [1, 4, 8, 10, 16, 40, 52, 78] sayıları numaralara sayısına göre sıraladı.
letters.sort() # ['a', 'a', 'b', 'g', 's', 's', 'y'] harfleri alfabeetik sıraladı.
numbers.reverse() # [78, 52, 40, 16, 10, 8, 4, 1] en son numbers a yaptığımız işlemin tam tersime çevidik sıralamayı. 
letters.reverse() # ['y', 's', 's', 'g', 'b', 'a', 'a']  en son letters yaptığımız işelemin tersine çevirdik.

print(numbers)  
print(letters)

print(len(numbers)) # 8
print(len(letters)) # 7


print(numbers.count(10))  # 1
print(letters.count('a')) # 2

numbers.clear()  # []  sonuç hepsini siler.
print(numbers)
