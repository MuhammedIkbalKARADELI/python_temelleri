x = 10

#if x > 5:
#    raise Exception('x 5 den büyk değer alamaz.')

# 'raise Exception()' yaparak kendimiz bir hata codu yazmış olduk raise ile olmayan hata kodu belirledik.
def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception('Parola en az 8 karakter olmalıdır.')
    elif not re.search("[a-z]", psw):
        raise Exception('Parola küçük harf içermelidir.')
    elif not re.search("[A-Z]", psw):
        raise Exception('Parola büyük harf içermelidir.')
    elif not re.search("[0-9]", psw):
        raise Exception("Parola rakam içermelidir.")
    elif not re.search("[_@$]", psw):
        raise Exception("Parola alpha numeric karakter içermelidir.")
    elif re.search("\s",psw):
        raise Exception("Parola boşluk içermemelidir.")


pasword = '12345Ba@'

try:
    check_password(pasword)
except Exception as ex:
    print(ex)
else: 
    print('Hoş geldiniz.')
finally:
    print('Validation tanımlandı.')


class Person: 
    def __init__(self,name,year):
        if len(name) > 10:
            raise Exception('Name alanı fazla karakter içeriyor. ')
        else: 
            self.name = name


p1 = Person('ALLi',1990)
print(p1.name)

p2 = Person('asfasfafadfafa',123131)
print(p2.name)