name = 'Çınar'
surname = 'Karadeli'
age = 19



print('My name is {} {}'.format(name, surname))
 # ilk '{}'sembolu ve name sıfırncı karkter   ikinci'{}'sembolu ve surname birinci karakter 
 # My name is Çınar Karadeli



print('My name is {1} {0}'.format(name, surname))
# My name is Karadeli Çınar



print('My name is {s} {n}'.format(n=name, s=surname))
# My name is Kardeli Çınar



print("My name is {} {} and I'm {} years old.".format(name, surname , age))
# My name is Çınar Karadeli and I'm 19 years old.



print("My name is {} {} and I'm {} years old.".format(name, name , name))
# My name is Çınar Çınar and I'm Çınar yers old. 



result = 200/700

print('the result is {}'.format(result))
# the result is 0.285714285714285714

print('the result is {r:1.4}'.format(r=result))
# the result is 0.2857

print('the result is {r:10.4}'.format(r=result))
# the result is       0.2857



print(f"My name is {name} {surname} and I'm {age} years old.")
# My name is Çınar Kardeli and I'am 19 years old.

