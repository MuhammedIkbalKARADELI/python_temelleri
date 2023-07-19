
# Identity Operator: is

x = y = [1, 2, 3]
z = [1, 2, 3]

# '==' operatoru objelerin eşliğini sorar
print(x==y) # True
print(z==y) # True   bunların üçü doğru çünkü atadığımız objeleri aynı ama z nin adresleri dierğlerinin adreslerinden farklı
print(x==z) # True

# is operatoru adreslerin eşliğini sorar  
print(x is y) # True  çünkü atadığımız adresleri aynı 
print(x is z) # False çünkü atadığımız adresler farklı 
print(y is z) # False çünkü atadığımız adresler farklı 



a = [1, 2, 3]
b = [2, 4]

del a[2]
b.reverse()
b[0] = 1

print(a) # [1, 2]
print(b) # [1, 2]

print(a == b) # True  dur çünkü objeerli biribrine benzettik
print(a is b) # False dur çünkü adresleri biribirnin aynısı değil.




# Membership Operator: in 

x = ['apple', 'banana', 'orange']
print('banana' in x)  # True

name = 'Çınar'
print('ına' in name)  # True
