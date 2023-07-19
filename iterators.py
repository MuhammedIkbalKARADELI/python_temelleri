
# iterators  aslında bir döngü demektir   for döngüsünde vardır.


# liste = [1,2,3,4,5]

# iterator = iter(liste)   # <list_iterator object at 0x0000020BF7F7EFD0>   oluşturulduğunu görürüz.

# print(iterator)

# print(next(iterator)) #1  listenin ilk elemanını bize vermiş olucak.
# print(next(iterator)) #2
# print(next(iterator)) #3
# print(next(iterator)) #4
# print(next(iterator)) #5
#print(next(iterator)) # StopIteration  error  is given by system.
# bu yukarda yaptığımız şeyin aynısını for döngüsünde yapar.
# for i in liste:
#     print(i)    

# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break


class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration


list = MyNumbers(10,20)

myiter = iter(list)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
# bu kullanım ile de yazdırabiliriz.

# for x in list:   # 10 dan 20 ye kadar sayıları yazar.
#     print(x)   


while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break