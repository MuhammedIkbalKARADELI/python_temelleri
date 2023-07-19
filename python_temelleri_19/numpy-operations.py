import numpy as np
from numpy.core.fromnumeric import reshape


numbers1 =np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)  #[39 69 81 84 73 65]
print(numbers2)  #[21 35 20 28 52 82]

result = numbers1 + numbers2
print(result)    #[ 60 104 101 112 125 147]
result1 = numbers1 + 10
print(result1) #[49 79 91 94 83 75]
result2 = numbers1 - 10
print(result2) #[29 59 71 74 63 55] 
result3 = numbers1 * 10
print(result3)  #[390 690 810 840 730 650]
result4 = numbers1 * numbers2
print(result4)  # [7742 1760 1672 5530 4947 5166]
result5 = numbers1 / 10
print(result5)  # [2.8 2.2 7.2 2.4 8.  4.3]
result6 = numbers1 / numbers2
print(result6)  # [0.65116279 0.37288136 1.30909091 0.31168831 5.71428571 1.02380952]


result7 = np.sin(numbers1) # [-0.83177474 -0.77946607 -0.15862267  0.76255845  0.01770193 -0.38778164]
result8 = np.cos(numbers1) # [ 0.5551133  -0.62644445 -0.98733928  0.64691932  0.99984331  0.92175127]
result9 = np.sqrt(numbers1) # [6.55743852 9.59166305 6.40312424 5.09901951 6.63324958 8.66025404]
result10 = np.log(numbers1) # [4.15888308 3.13549422 4.07753744 3.04452244 3.21887582 4.18965474]

print(result7)
print(result8)
print(result9)
print(result10)





multi_numbers1 = numbers1.reshape(2,3)
multi_numbers2 = numbers2.reshape(2,3)

print(multi_numbers1)
print(multi_numbers2)
"""
Ex:
[[16 14 83]
 [69 27 46]]
[[42 30 76]
 [10 75 27]]
 """

result11 = np.vstack((multi_numbers1,multi_numbers2)) #vertical stack # bu iki matrisi dikey olarak birliştirdi
print(result11)
"""
[[16 14 83]
 [69 27 46]
 [42 30 76]
 [10 75 27]] 
 """


result12 = np.hstack((multi_numbers1,multi_numbers2)) #horizontal stack # bu iki matrisi yatay olar birleştirdi
print(result12)
"""
[[16 14 83 42 30 76]
 [69 27 46 10 75 27]] 
 """



result13 = numbers1>=50 # burda matrisimizdeki sayıların 50 den büyk olanları bize söyler.
print(result13)   # [ True  True False  True  True  True]

result14 = multi_numbers1>=50
print(result14)
""" [[False  True False] 
     [ True  True False]]"""


result15 = numbers2 % 2 == 0
print(result15)  #[ True False  True  True False False]

result16 = numbers2[result15]  # burda istediğimiz şartı sağlayan ifadeleri yazdırıyoruz.
print(result16) # [12 72 20]




