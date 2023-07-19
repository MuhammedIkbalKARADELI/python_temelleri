website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1- 'course karakter dizisinde kaç karakter bulunmaktadır ?

result = len(course)

# 2- 'website' içinden www karakterlerini alın
 
result = website[7:10]


# 3- 'website' içinden com karakterlerini alın

length = len(website)
result = website[-3:]
print(result)

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın 

result = course[:15]  
result = course[-15:]

# 5- 'course' ifadesindeki karakterleri tersten alın 

result = course[::]  # -> course'u aynen yazdırır 
result = course[::2] # -> course'u aynen ama iki karakterde bir yazdırır
result = course[::-1] # -> course'u tam ters bir şekilde yazdırır


name, surname, age, job = 'Bora', 'Yılmaz', 32, 'mühendis'

# 6- Yukarıdaki verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın
#     'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis' 

result = 'Benmim adım ' + name + ' ' + surname +', Yaşım ' + str(age) + ' ve mesleğim ' + job
result = "Benim adım {} {}, Yaşım {} ve mesleğim {}.".format(name, surname, age, job)
result = f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}"

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin. 
s = 'Hello world' 
s = s[:6] + 'W' + s[-4:]
print(s)

print(s.replace('w','W'))

# 8- 'abc' ifadesini yan yana 3 defa yazdırın

result = 'abc' * 3
result = 'abc ' * 3




print(result)
