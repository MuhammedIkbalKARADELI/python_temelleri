class Person: 
    address = 'adres girilmedi'

    def __init__(self,name,year):
        self.ad = name
        self.yil = year
        
    def intro(self):
        print('Hello There. I am ' + self.ad)

    def calculateAge(self):
        return 2021 - (self.yil)



c1 = Person('ahmet',1974)
c2 = Person('Ali',1990)

print(c1)
print(c2)

print(f"name: {c1.ad}  year:{c1.yil} and your adress is: {c1.address}")

c1.intro()
c2.intro()


print(f"My name is {c1.ad} and my age is {c1.calculateAge()}")
print(f"My name is {c2.ad} and my age is {c2.calculateAge()}")

################################################

class Circle:
    pi = 3.14

    def __init__(self,radious=1):
        self.yaricap = radious

    def cevre_hesapla(self):
        return 2*(self.pi)*(self.yaricap)

    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)

d1 = Circle(5)
d2 = Circle()
print(d1.yaricap)
print(d2.yaricap)
a = d1.cevre_hesapla()
b = d1.alan_hesapla()

print(a)
print(b)







