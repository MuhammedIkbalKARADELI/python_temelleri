

numbers = [1,2,3,4,5]
'''
for num in numbers:
    print(num)

1
2
3
4
5
'''
'''
for num in numbers:
    print('Hello')

Hello
Hello
Hello
Hello
Hello
'''

names = ['çınar','sadık','sena']
'''
for name in names:
    print(name)

çınar
sadık
sena
'''

# str için for kullanımı
name = 'Ibal Karadeli'
'''
for n in name:
    print(n)
               str ifademizde herbir indexi teker teker yazdırır.
I
b
a
l

K
a
r
a
d
e
l
i
'''


# tuple için for kullanımı
tuple = (1,2,3,4,5)
'''
for t in tuple:
    print(t)

1
2
3
4
5
'''


tuple2 = [(1,2),(8,3),(9,5),(4,7)]
'''
for t2 in tuple2:
    print(t2)
 
(1, 2)
(8, 3)
(9, 5)
(4, 7)
'''
'''
for a,b in tuple2:
    print(a)

1
8
9
4
'''
'''
for a,b in tuple2:
    print(b)

2
3
5
7
'''

'''
for a,b in tuple2:
    print(a,b)

1 2
8 3
9 5
4 7
'''

# dictionary için for kullanımı


dict = {'k1':1, 'k2':2, 'k3':3}
'''
for d in dict:
    print(d)

k1
k2
k3
'''
'''
for d in dict.items():
    print(d)
                 eleman bilgilerini getitrir.
('k1', 1)
('k2', 2)
('k3', 3)
'''
'''
a = key, b = value dur.
for a,b in dict.items():
    print(a)
                dict dan key değelrini yazdırdık
k1
k2
k3
'''
'''
for a,b in dict.items():
    print(b)
                 dict dan value değerini yazdırdık.
1
2
3
'''
'''
for a,b in dict.items():
    print(a,b)
                 dict dan key,value değerlerini yazdırmış olduk.
k1 1
k2 2
k3 3
'''

adj = ['red', 'blue', 'green']
cars = ['BMW', 'Mercedes', 'Audi']

for x in adj:
    for y in cars:
        print(x,y)
        
'''
red BMW
red Mercedes
red Audi
blue BMW
blue Mercedes
blue Audi
green BMW
green Mercedes
green Audi
'''