
# class

class Person:
    pass
    # class attributes

    # constructure (yapıcı method)

    # objects attributes

    # methods


# objects (instance)

p1 = Person() # <__main__.Person object at 0x01617160>
p2 = Person() # <__main__.Person object at 0x01617220>
# yukardaki gibi adreslerre atanır bu objeler.

print(p1)
print(p2)

print(type(p1)) # <class '__main__.Person'>
print(type(p2)) # <class '__main__.Person'>


#################################

class Persoon:
    pass

    def __init__(self,ad,yıl):
        self.name = ad # structuredaki gibi
        self.year = yıl # self. dan sonraki karakter yıl ı çağırmak için kullanılacaktır
        print('init methodu çalıştı.')


# k1 = Persoon() # that does not work because does not have any paramater 
# print(k1)

q1 = Persoon('Ali',1990)
q2 = Persoon('ahmet',1897)

print(q1)
print(q2)

print(f"name: {q1.name}  year:{q1.year}")


##########################

class Persooon: 
    address = 'adres girilmedi'

    def __init__(self,name,year):
        self.ad = name
        self.yıl = year
        print(f"Hoş geldin {self.ad} ")

c1 = Persooon('ahmet',1974)
c2 = Persooon('Ali',1990)

print(c1)   # <__main__.Persooon object at 0x00000235279C7D30>
print(c2)   # <__main__.Persooon object at 0x00000235279C7CD0>

print(f"name: {c1.ad}  year:{c1.yıl} and your adress is: {c1.address}")

#################################

class Arabaci:
    address = 'No information'

    def __init__(self,ad,yil,renk):
        self.name = ad
        self.year = yil
        self.colour = renk
        print(f"{self.name}'s year of car is {self.year} and colour is {self.colour}")


kisi1 = Arabaci('Ali',1990,'Blue')
kisi1.name = 'ahmet' # burdaki değişiklik yanlızca aşağıdaki yazıda değişiklik yaptı yukrdaki class da yapmadı

print(f"{kisi1.name}'s year of car is {kisi1.year} and colour is {kisi1.colour}")



