website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1-  ' Hello World ' karakter dizisinin baş ve sondaki karakterlerini silin. 

result = ' Hello World '.strip()  # -> 
result = ' Hello World '.lstrip()  # -> sol taraftan boşlukları siler
result = ' Hello World '.rstrip()  # -> sağ taraftan boşlukarı siler


result = website.lstrip('/:pth') # -> wbsite deki str ifademizden soltaraftan seçtiğimiz karakterleri siler. 

# 2- 'www.sadikturan.com'  içindeki sadikturan haricindeki her karakteri silin.
result = 'www.sadikturan.com'.lstrip('w.').rstrip('.moc')
result = 'www.sadikturan.com'.strip('w.moc')  # -> bu metodu kullanarakve seçtiğimiz karakterleri yazarak cümlenin içinden sildik

# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın 
result = course.lower()
result = course.upper()
result = course.title()

# 4- 'website' içinden kaç tane a karakteri vardır ?  (count('a'))
result = website.count('a')   # bu method bize istediğimiz karakter kaç tane olduğunu söyler.
result = website.count('www')
result = website.count('www',0,10)  # wbsite str ifadesinde burda 0 ile 10 karakter arasınd arama yapar. 


# 5- 'website' "www" ile başlayıp "com" ile bitiyor mu ?
result = website.startswith('www')  # False
result = website.startswith('http') # True
result = website.endswith('com')    # True

# 6- 'website' içersinde '.com' ifadesi var mı?
result = website.count('com')

result = website.find('com')    # sonuç 22 çünkü aradığımız ifaadenin ilk karakter numarasını verir
result = website.find('com',0,10)  # sonuç -1 dir çünkü com ifadesi 0 ile 10 karakteri arasında yok.
result = course.find('Python')  # 0
result = course.rfind('Python')  # sonuç 26 dır çünk sağdaki python u söyler 

result = website.index('com') # sonuç 22 
result = website.rindex('com') # sonuç 22
#result = website.index('comm')  # hata verir

# 7- 'course' içindeki karakterleri hapesi alfabetik mi ?  (isalpha, isdigit)
result = course.isalpha()  # burda course ifadesinin alfabetik olup olmadığını soruyor bütün karakterlerinin
result = 'Cınar'.isalpha()
result = course.isdigit() # burada course ifadesinin rakam olup olmadığını soruyor bütütn karakterlerinin
result = '1234'.isdigit()
 
# 8- 'contents' ifadesini satırda 50 karakter içinr yerleştirip sağ ve soluna * ekleyiniz 
result = 'contents'.center(50,'*')
result = 'contents'.rjust(50,'*')  # 50 karakterlik alnda contents ifadesini en sağa kaydırır
result = 'contents'.ljust(50,'*') # 50 karakterlik alnda contents ifadesini en sola kaydırır

# 9- 'course' karakter dizisindeki tğm boşluk karakterlerini '-' ile deiştirin 
result = course.replace(' ','-')
result = course.replace(' ','-',5) # yanlızca ilk beş boşluğa bu yer değiştirmeyi uygular 'replace' olduğundan sağdan ilk beş boşluk

# 10- 'Hello World' karakter dizisnin 'World' ifadesini 'There' olarak değiştirin
result = 'Hello World'.replace('World','There')

# 11- 'course' karakter dizisinin boşluk karakterlerinden ayırın
result = course.split()
result = result[2] # sonuçumuz 'Baştan' olur
result = course.split('.')

print(result)

