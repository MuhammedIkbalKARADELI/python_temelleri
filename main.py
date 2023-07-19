import mod # bizim oluşturduğumu mod dosyasını buraya açıyor bşr nevi ordaki her datayı burda kullanabiliyoruz.
           # başına sadece mod. koyup sanki mod.py dosyasındaymışız gibi herşeyi yapabiliyoru. 
#result = help(mod)
#print(result)

#result = help(mod.func)
#print(result)

result = mod.number
print(result)

result = mod.numbers
print(result)

result = mod.func(45)
print(result)

result = mod.person['name']
print(result)

result = mod.person['age'] # dictionary 
print(result)

p = mod.Person()   # class 
result = p.speak()  # class içindeki method
print(result)

e = mod.Person() # class içindeki method
e.eat()