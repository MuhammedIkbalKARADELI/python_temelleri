#  for da range() kullanımı


for x in range(10):
    print(x)
'''
0
1
2
3
4
5
6
7
8
9
'''

for x in range(2,12):
    print(x)
'''
2
3
4
5
6
7
8
9
10
11
'''

for x in range(40,100,15):
    print(x)
'''
40
55
70
85
'''

for x in range(20,100,10):  # 20 den başla 100e kadar 10 ara 10 ar yazdır.
    print(x)
'''
20
30
40
50
60
70
80
90
'''

# range() ifadesini list e çevirebiliriz.

print(list(range(20,100,10)))
# [20, 30, 40, 50, 60, 70, 80, 90]





# enumerate


index = 0
greeting = 'Hello There'

for letter in greeting:
    print(f'index: {index} letter: {letter}')
    index += 1

'''    
index: 0 letter: H
index: 1 letter: e
index: 2 letter: l
index: 3 letter: l
index: 4 letter: o
index: 5 letter:
index: 6 letter: T
index: 7 letter: h
index: 8 letter: e
index: 9 letter: r
index: 10 letter: e
'''
# yukardakiyle aynı sonucu verir
'''
for letter in greeting:
    print(f"index: {index} letter: {greeting[index]}")
    index += 1


index: 0 letter: H
index: 1 letter: e
index: 2 letter: l
index: 3 letter: l
index: 4 letter: o
index: 5 letter:
index: 6 letter: T
index: 7 letter: h
index: 8 letter: e
index: 9 letter: r
index: 10 letter: e
'''

# yukarda yapmış olduğumuz şeyin aynısını "anumerate" ile yapacağız.


selam = 'Merhaba'

for x in enumerate(selam): 
    print(x)
# burda x = item diyebilirix ve herşeyi diyebiliriz. ben x yazdım çünkü değişken olduğunu yani istediğimizi yazabildiğimizi göstermek için.
'''
(0, 'M')
(1, 'e')
(2, 'r')
(3, 'h')
(4, 'a')
(5, 'b')
(6, 'a')
'''

for a,b in enumerate(selam):
    print(f'index: {a} letter: {b}')

# a = index numarasını gösterir  b = str ifadesinde for döngüsünde yazdırır 

# burda 'a,b' yazmamın sebebi istediğim herşeyi yazavilirim demek için.
'''
index: 0 letter: M
index: 1 letter: e
index: 2 letter: r
index: 3 letter: h
index: 4 letter: a
index: 5 letter: b
index: 6 letter: a
'''

#  zip methodu

list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c', 'd', 'e']
list3 = [100, 200, 300, 400, 500]

print(list(zip(list1, list2)))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

print(list(zip(list1,list2,list3)))
# [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300), (4, 'd', 400), (5, 'e', 500)]


for item in zip(list1,list2,list3):
    print(item)
'''
(1, 'a', 100)
(2, 'b', 200)
(3, 'c', 300)
(4, 'd', 400)
(5, 'e', 500)
'''


for a,b,c in zip(list1,list2,list3):
    print(a)
'''
1
2
3
4
5
'''


for a,b,c in zip(list1,list2,list3):
    print(a,b)
'''
1 a
2 b
3 c
4 d
5 e
'''


for a,b,c in zip(list1,list2,list3):
    print(a,b,c)
'''
1 a 100
2 b 200
3 c 300
4 d 400
5 e 500
'''


for a,b,c in zip(list1,list2,list3):
    print(b)
'''
a
b
c
d
e
'''    