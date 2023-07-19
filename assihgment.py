"""
#x = 5
#y = 10
#z = 20
#  ||
#  \/

x, y, z = 5, 10, 20
print(x, y, z)  # 5, 10, 20

x, y = y, x 
print(x, y, z)  # 10, 5, 20


x += 5     #  (x = x + 5) 
print(x)   # 15

x -= 5     # (x = x - 5)
print(x)   # 10

x /= 3     # (x = x / 3)
print(x)   # 3.3333333333333335

x *= 5     # (x = x * 5)
print(x)   # 16.666666666666668

x %= 3     # (x = x % 3)   mod
print(x)   # 1.6666666666666679  

x //= 1    # (x = x // 1)  tam bölme
print(x)   # 1.0

y **= 4    # (y = y ** 4)
print(y)   # 625
"""



values = 1, 2, 3

print(values)  # (1, 2, 3)
print(type(values))  #<class 'tuple'>

x, y, z = values
print(x, y, z)  # 1 2 3

# values değerinde yeterli eleman yoksa bizim bu atamamız olamaz
# eğer values değerinde yerinden fazla değer varsa yine bzim x, y, z değerine bu yoldan atamayız.
  #  aşağıdaki yöntemle values değerindeki elemanları da atayabiliriz.
values = 1, 2, 3, 4, 5
x, *y, z = values
print(x, y, z) #  1 [2, 3, 4] 5
print(x, y[1], z)  # 1 3 5