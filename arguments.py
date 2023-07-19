### 1 ###
print(' 1 '.center(25,'*'))
def changeName(n):
    n = 'ada'

name = 'yigit'  # burda name deki karakter değişmez çünkü adresi
                # 'n' ile eş olmaz fakat list lerde hariç.
changeName(name)
print(name)

### 2 ###
print(' 2 '.center(25,'*'))

def changeCity(city):   # burda city ile aşağıda yzdığımız cities değerleri adres eşitlemesi oluyor
    city[0] = 'Istanbul' # ardından bu eşitlikten değeri değiştirebiliyoruz.

cities = ['Ankara', 'Izmir']

changeCity(cities)
print(cities)

### 3 ###
print(' 3 '.center(25,'*'))

def isimchange(i):
    i[0] = 'ada'

names = ['Ali','Fatma','Jale']
n = names # burda adres eştilemesi yaparız bu yüzden
          # n  ye yapacağımız her değişiklik 'names'de de görülür.
k = names[:] # slicing # burda adres eşitlemesi yapılmaz sadece değerler kopyalanır

isimchange(names)
print(names)
print(n) # n de isimchange fon kullanılmamasına rağmen n de değişiklik var çünkü 'names' ve 'n' nin adresleri bir
# onun yerine 'k' değerler kopyalanıp yapılan değişiklerle 'names' i etkilemeden sonuç elde edebiliriz.
 
### 4 ###
print(' 4 '.center(25,'*'))

def add(*param):
    print(' ')
    print(param[0])
    return sum(param)
print(add(10, 13, 41, 52, 87, 24))
print(add(12, 23, 144 ))

### 5 ### 
print(' 5 '.center(25,'*'))

def toplam(*paramss):
    sum = 0
    for x in paramss:
        sum += x
    return sum

print(toplam(1, 43, 41, 32, 56, 97))
print(toplam(12, 23, 144 ))


### 6 ### 
print(' 6 '.center(25,'*'))

def displayUser(**arg): #bu kullnım '**' dictionary formatına cevrir.
    print(type(arg))
    print(arg)
    for key, value in arg.items():
        print(f'{key} is {value}')

displayUser(name='Ikbal', age=19, city='Aydın')
print(' ')
displayUser(name='Ada',age=12,city='kocaeli',phone='214124124' )

### 7 ### 
print(' 7 '.center(25,'*'))

def myFunc(a,b, *args , **kwargs):
    print(a)  # int
    print(b) # int
    print(args) # tuple
    print(kwargs) # dic

myFunc(10, 20, 30, 40, 50, 60, 70, 80, key1='value 1', key2='value 2')


