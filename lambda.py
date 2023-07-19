### 1 ### another way of using func

def square(num):    return num**2

result = square(3)
print(result)


### 2 ###  if we have list for using this func,
#            we can use map func 

numbers = [1,2,3,4,5,6,7]

print(list(map(square,numbers)))  # by using this func, we have square number of this list

### 3 ###  also we can write the answer is wanted like above

for item in map(square,numbers):
    print(item)

### 4 ###  we also can use lambda which is more easy usage instead of defining a function

kare = lambda n: n **2 

result2 = list(map(kare,numbers))  # we take result withot any differents 
result3 = list(map(lambda x: x**2,numbers)) # in this usage we don't have func name so that we can't use func name 
print(' ')
sonuc = kare(4)
print(sonuc,'is result of kare func')
print(result2)
print(result3)


### 5 ###  we can define in the map func by using lamda

reslt4 = list(map(lambda y: y+2, numbers))
print(reslt4)

### 6 ### 

def chechk_even(num): return num%2==0 # our result come from return which is true

result5 = list(filter(chechk_even,numbers))
print(result5)

### 7 ### also we can use lambda 

chechk_square_even = lambda num: (num+1)%2==0 # this fuc give us 'true','false' result
result6 = list(filter(chechk_square_even,numbers))
result8 = chechk_square_even(numbers[2])
result9 = chechk_square_even(numbers[1])

print(result8)
print(result9)
print(result6)


### 8 ### another usage

result7 = list(filter(lambda x: ((x*3)/2)%2==0,numbers)) # filter write the true results in the func we cereate
print(result7)
