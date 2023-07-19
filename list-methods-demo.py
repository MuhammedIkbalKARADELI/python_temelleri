names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna elkleyiniz. 
 #names.append('Cenk')
 #print(names)  # ['Ali', 'Yağmur', 'Hakan', 'Deniz', 'Cenk']

# 2- "Sena" değerini listenin başına ekleyiniz.
 #names.insert(0,'Sena')  # ['Sena', 'Ali', 'Yağmur', 'Hakan', 'Deniz']
 #names.insert(-1,'Sena')  # ['Ali', 'Yağmur', 'Hakan', 'Sena', 'Deniz']  en sona 'Sena' ifadesi gelmez çünkü biz en yukardaki names de -1 değerinin yerine yazdık.
 #names.insert(len(names),'Sena')  # ['Ali', 'Yağmur', 'Hakan', 'Deniz', 'Sena']  'Sena' ifadesini böyle yazarak en sona koyabiliriz.
 #print(names)  

# 3- "Deniz" ismini listeden siliniz.
 #names.remove('Deniz') # ['Ali', 'Yağmur', 'Hakan']
 #print(names)

 #names.pop() # listenin en sonundaki karakteri siler ['Ali', 'Yağmur', 'Hakan']
 #print(names)

 #names.pop(1) # belirnen indexteki karakteri kaldırır ['Ali', 'Hakan', 'Deniz']
 #print(names)

# 4- "Deniz" isminin ideksi nedir?
 #result = names.index('Deniz')  # 3
 #print(result)

 #index = names.index('Deniz')
 #names.pop(index)   # indexini belireldiğimiz karakteri kaldırır  ['Ali', 'Yağmur', 'Hakan']
 #print(names)

# 5- "Ali" listenin bir elemanı mı?
 #result = 'Ali' in names  # True
 #result = names.index('Ali') # 0  #sonuç -1 ise list de yoktur.
 #print(result)

# 6- Liste elemanlarını ters çeviriniz.
 #names.reverse() # ['Deniz', 'Hakan', 'Yağmur', 'Ali']
 #print(names)

 #years.reverse() # [1987, 1998, 2000, 1998]
 #print(years)

# 7- Liste elemanlarını alfabetik olarak sıralayınız. 
 #names.sort() # ['Ali', 'Deniz', 'Hakan', 'Yağmur']
 #print(names)

# 8- years listesini rakamsal büyüklüğe göre sıralayınız.
 #years.sort() # [1987, 1998, 1998, 2000]
 #print(years)

# 9- str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
 #str = "Chevrolet,Dacia" 
 #result = str.split(',')
 #print(result)  # ['Chevrolet', 'Dacia']

# 10- years dizisinin en büyük ve en küçük elamını nedir.
 #min = min(years)
 #max = max(years)
 #print(min,max)  # 1987 2000

# 11- years diizisinde kaç tane 1998 depğeri vardır?
 #result = years.count(1998)
 #print(result) # 2

# 12- years dizidsinin tüm elemanları siliniz.
 #years.clear()
 #print(years)  # []

# 13- kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []

araba_markası = input("Araba markası: ")
markalar.append(araba_markası)

araba_markası = input("Araba markası: ")
markalar.append(araba_markası)

araba_markası = input("Araba markası: ")
markalar.append(araba_markası)

print(markalar)

