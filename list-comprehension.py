
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

numbers = [x for x in range(10)]
print(numbers)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers1 = []
for y in range(10):
    numbers1.append(y)
print(numbers1)    
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




numbers = [x*x for x in range(10)]
print(numbers)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

numbers1 = []
for y in range(10):
    numbers1.append(y*y)
print(numbers1) 
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



numbers = [x**2 for x in range(10)]
print(numbers)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

numbers1 = []
for y in range(10):
    numbers1.append(y**2)
print(numbers1)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



numbers2 = []
for q in range(10):
    if q % 2==1:
        numbers2.append(q)
print(numbers2)
# [1, 3, 5, 7, 9]



numbers3 = []
for q in range(10):
    if q % 2==1:
        continue
    numbers3.append(q)
print(numbers3)
# [0, 2, 4, 6, 8]




numbers4 = [x**2 for x in range(10) if x%3==0]
print(numbers4)
# [0, 9, 36, 81]

numbers5 = []
for r in range(10):
    if r % 3 == 0:
        numbers5.append(r**2)
print(numbers5)
#[0, 9, 36, 81]


myString = 'Hello' 
myList = []

for word in myString:
    myList.append(word)
print(myList)
# ['H', 'e', 'l', 'l', 'o']

myList1 = [word1 for word1 in myString]
print(myList1)
# ['H', 'e', 'l', 'l', 'o']




years = [1997, 1956, 2000, 1979, 1983]
ages = [2020 - year for year in years]
print(ages)
#[23, 64, 20, 41, 37]



result = ['çift' if x%2==0 else 'tek' for x in range(1,10)]
print(result)
# ['tek', 'çift', 'tek', 'çift', 'tek', 'çift', 'tek', 'çift', 'tek']


result1 = [(f'tek sayı: {q}') if q%2==1 else (f'çift sayı: {q}') for q in range(2,15) ]
print(result1)


result2 = []
for t in range(3): 
    for k in range(4,7):
        result2.append((t,k))
print(result2)
# [(0, 4), (0, 5), (0, 6), (1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6)]

result3 = [(t,k) for t in range(3) for k in range(4,7)]
print(result3)
# [(0, 4), (0, 5), (0, 6), (1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6)]

