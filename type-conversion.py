"""
#1 input() = string bir yapı
  x = input("1.sayı: ") 
  y = input("2.sayı: ")

#2 aşağıdakini yaparak hangi yapı olduğunu öğreniyoruz
  print(type(x))   => str
  print(type(y))   => str


#3 asagıdaki 'x' ve 'y' yi inputtaki str yapıdan int yapısına geçirdik  
   x = int(x)   
   y = int(y) 
  
#4 aşığadiyle yeni çevirdiğim yapıyı teyit ettiriyoruz bir nevi  
   print(type(x))  => int
   print(type(y))  => int

#5 aşağıdaki iki sonuçta doğrdur ssağdakini yaparsak eğer #3 yapmamıza gerek kalmaz
   toplam = x + y   <=>  toplam = int(x) + int(y)

print(toplam)
"""

"""
  x = 5             #int
  y = 2.5           #float
  name = 'Çınar'    #str
  isOnline = True   #bool

  print(type(x))        =>int
  print(type(y))        =>float
  print(type(name))     =>str
  print(type(isOnline)) =>bool

"""

#  Type conversion    

x = 5             #int
y = 2.5           #float
name = "Çınar"    #str
isOnline = True   #bool

'''
# int -> float 
 
  x = float(x)
  print(x)
  print(type(x))
'''

'''
# float -> int

  y = int(y)
  print(y)
  print(type(y))
'''
'''
result = x + y  #5 + 2.5 = 7.5
print(result )  
print(type(result))  #float
'''

'''
# bool -> str  

isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))
'''


'''
# bool -> int
  # eğer 'bool' True 'ise'' int değeri 1
  isOnline = True
  isOnline = int(isOnline) 
  print(isOnline)  # 1
  print(type(isOnline)) # int  

 # eğer 'bool' False ise 'int' değer 0
  isOnline = False
  isOnline = int(isOnline)
  print(isOnline)  # 0
  print(type(isOnline)) # int  
'''

