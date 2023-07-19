'''
x = 5

result = 5 < x < 10 
print(result)  # False 

result = 5 <= x < 10 
print(result)  # True
'''

x = 5 
hak = 5
devam = 'e'


# and


result =  x > 5 and x < 10 
print(result)  # False dır çünkü ilk ifade yanlış
# True, True  => True
# True, False  => False

result = (hak > 0 and (devam == 'e'))
print(result) # True

result = (hak > 10 and (devam == 'e'))
print(result) # False

# or

result = (x > 0) or (x % 2 == 0)
print(result) #True
# True, True  => True
# True, False  => True
# False, False => False


# not

result = (x > 0)  # True
result = not(x > 0)  #  False
print(result)


# x, 5-10 arasında olan bir çift sayı mı? 
x = 5
result = ((x>5) and (x<10)) and (x % 2 == 0)  # False
print(result)
