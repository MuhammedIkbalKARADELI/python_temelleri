# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
cars =['Bmw','Mercedes','Opel','Mazda']

# 2-  Liste kaç elemanlıdır ?
result = len(cars)  # 4


# 3-  Listenin ilk ve son elemanı nedir ?
result = cars[0]
result = cars[-1]


# 4-  Mazda değerini Toyota ile değiştirin.
cars[-1] = 'Toyota' 
result = cars   #['Bmw', 'Mercedes', 'Opel', 'Toyota']


# 5-  Merceds listenin bir elemanı mıdır?
result = 'Mercedes' in cars  # True


# 6-  Listenin -2 indeksindeki değer nedir?
result = cars[-2]  #Opel


# 7-  Listenin ilk üç elemanını alın. 
result = cars[:3]
result = cars[-2:]


# 8-  listenin son 2 elemaın yerine "Toyota" ve "Renault" değerlerini ekleyin.
cars[-2:] = ['Toyota','Renault']
result = cars  #  ['Bmw', 'Mercedes', 'Toyota', 'Renault']


# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
result = cars + ['Audi','Nissan'] # ['Bmw', 'Mercedes', 'Toyota', 'Renault', 'Audi', 'Nissan']


# 10- Listenin son elemanını silin.
del cars[-1]
result = cars # ['Bmw', 'Mercedes', 'Toyota']
result = len(cars) # 3


# 11- Liste elemanlarını tersten yazdırınız.
result = cars[::-1] # ['Toyota', 'Mercedes', 'Bmw']

# 12- Aşağıdaki verileri bir liste içinde saklayız.

     # studentA: Yiğit Bilgi 2010, (70,60,70)     
     # studentB: Sena Turan 1999, (80,80,70)
     # studentC: Ahmet Turan 1998, (80,70,90)

studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]

# 13- Liste elemanlarını ekrana yazdırınız.
result = studentA[2]  # 2010
result = studentB[1]  # Turan
result = studentC[3]  # [80, 70, 90]

result = studentA[3][2]  # 70
result = studentB[3][1]  # 80
result = studentC[3][0]  # 80

# 14- 'Yiğit Bilgin 10 yaşında ve not ortalaması 66' yazdırın.
not_ort = (studentA[3][0] + studentA[3][1] + studentA[3][2])/3
result = f"{studentA[0]} {studentA[1]} {2020 - studentA[2]} yaşında ve not ortalaması {(not_ort):2.3}"




print(result)
