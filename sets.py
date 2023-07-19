
fruits = {'orange', 'banana', 'apple'}
print(fruits)  # {'banana', 'apple', 'orange'}
#print(fruits[0]) #  indexlenemez

"""
for x in fruits:
     print(x)             aşağıdaki gibi karışık bir şekilde yazdırır.
                 # apple  
                 #banana
                 #orange
"""

fruits.add('cherry') # beliftiğimiz karkateri ekler sets'e
print(fruits)   # {'cherry', 'apple', 'banana', 'orange'}

fruits.update(['grapes'])  # belirttiğimiz karkakteri ekler. 
print(fruits)   # {'cherry', 'banana', 'apple', 'grapes', 'orange'}

fruits.update(['grapes','mango'])    # aynı karakteri tekrar atrsan bile bir defa yazar.
print(fruits)  # {'apple', 'banana', 'orange', 'cherry', 'mango', 'grapes'}

fruits.remove('apple') # belirtiğimiz karakteri kaldırır.
print(fruits)  #{'orange', 'cherry', 'mango', 'banana', 'grapes'}

fruits.discard('orange')  # belirtitğimiz karakteri sets den kaldırır.
print(fruits)  # {'banana', 'cherry', 'mango', 'grapes'}

fruits.pop()  # pop() normalde index ile kullanılır bu yüzden pop() setsin içinden herhangi bir karakteri kaldırır.
print(fruits)  #{'banana', 'grapes', 'cherry'}

fruits.clear()   # bütün elemanları siler.
print(fruits)  # set()

MyList = [1,2,3,4,4,45,5,5,6]
print(MyList)  # [1, 2, 3, 4, 4, 45, 5, 5, 6]
print(set(MyList))  # {1, 2, 3, 4, 5, 6, 45}  aynı sayıları bir defa içerir sets in içinde.





