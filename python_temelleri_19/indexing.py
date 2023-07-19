import numpy as np
from numpy.core.fromnumeric import reshape


numbers = np.array([0,5,10,15,20,25,50,75])

result1 = numbers[5] # oluşan diziden 5. indexteki karakter alınır.
result2 = numbers[-1] # oluşan diziden son indexteki karakter alınır.
result3 = numbers[0:3] # 0,1,2 indexe sahip karakterleri verir.
result4 = numbers[:3]
result5 = numbers[3:]
result6 = numbers[::]
result7 = numbers[::-1]
result8 = numbers[::-2]

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)



numbers2 = np.array([[0,5,10],[15,20,25],[50,75,95]])

result21 = numbers2[0]  # [0,5,10]
result22 = numbers2[2]  # [50,75,95]
result23 = numbers2[0,2] # [10]
result24 = numbers2[2,1] # [75]
result25 = numbers2[:,2] # [10,25,95]
result26 = numbers2[:,0] # [0,15,50]
result27 = numbers2[:,0:2] # [[ 0  5]
                           #  [15 20]
                           #  [50 75]]
result28 = numbers2[-1,:] # [50 75 95]      
result29 = numbers2[:2,:2]  # [[ 0  5]
                            #  [15 20]]

print(result21)
print(result22)
print(result23)
print(result24)
print(result25)
print(result26)
print(result27)
print(result28)
print(result29)




arr1 = np.arange(0,10)
arr2 = arr1  # referance copy  # burda arr2 ye yapıln her değişklikde arr1 de değişlik meydana gelecktir. 
arr3 = arr1.copy()  # burda sadece arr1 den kopyalanan değerler arr3 kopyalama işlemi yapılır

arr2[2] = 100  # burdaki bir dğişiklik arr1 de etkileyecktir. 

print(arr1)
print(arr2)
print(arr3)



