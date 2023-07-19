
class Persooon: 
    def __init__(self):
        print("person created")

class Studennt(Persooon):
    pass


a = Persooon()
b = Studennt()

#########################################


class Persoon:
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname
        print('Person created.')

    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print('i am eating')



class Studentt(Persoon):
    def __init__(self,fname,lname,number):
        Persoon.__init__(self,fname,lname)
        self.studentNumber = number
        print("Student created.")

    def who_am_i(self):
        print('I am a student')

    def sayHello(self):
        print('Hello I am a student.')


class Teacher(Persoon):
    def __init__(self,fname,lname,branch):
        Persoon.__init__(self,fname,lname) # altarnatif kullanım  ==  'super().__init__(fname,lname)'
        self.branch = branch
        print('Teacher cerated.')
    
    def who_am_i(self):
        print('I am a teacher')




p1 = Persoon('Ahmet','Kil')
s1 = Studentt('Ali','Pir',1231212412)        
t1 = Teacher('Çınar','Yılmaz','math')


print(p1.firstName +' '+p1.lastName)
print(s1.firstName +' '+s1.lastName+ ' '+str(s1.studentNumber))
print(t1.firstName +' '+t1.lastName+' '+t1.branch)

p1.who_am_i()
s1.who_am_i() # normalde (student içine 'who_am_i' tanımlamamış olsaydık 'I am a person' yazacaktı çünkü Student, Person dan inheritance aldı.)
t1.who_am_i()


p1.eat()
s1.eat()
t1.eat()

s1.sayHello() # bu method Student a ait bir özellik
