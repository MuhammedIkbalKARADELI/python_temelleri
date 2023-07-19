myList = [1,2,3]
myString = 'my string'
print(len(myList))
print(len(myString))

print(type(myList))
print(type(myString))


class Movie:
    pass

m = Movie()

print(type(m)) # <class '__main__.Movie'>
#print(len(m)) # special methods kullanarak len i kullanabileceğiz.                                               
                                               
                                               
class film:                                               
    def __init__(self,title,director,duration):                                               
        self.title = title                                               
        self.director = director                                               
        self.duration = duration                                               
        print('film objesi oluşturuldu.')                                               
                                               
    def __str__(self):                                               
        return f"{self.title} by {self.director}"                                               
                                               
    def __len__(self):                                               
        return self.duration                                               
                                               
    def __del__(self):                                               
        print('film objesi silindi.')



f = film('film adı','film yönetmeni',120)

print(myString)
print(f) # bize adresini verir. <__main__.film object at 0x00B472B0> 

print(str(myList))
print(str(f)) # film class içersine 'str' method tanımlamadan önce yine adres bilgisini verir 

print(len(f))                   


