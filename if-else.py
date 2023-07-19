

"""
if 3>2:
    print('Hoş Geldiniz')

if 3==3:
    print('Hoş Geldiniz')

if True:
    print('Hoş Geldiniz')  # yazdırın çünkü if in yanındaki bool değeri yanlız true olunca altındki ilk print yazısına izin verir.

haci = True
if haci:
    print('Hoş Geldiniz')   #  Hoş Geldiniz

if haci == True:
    print('Hoş Geldiniz') #  Hoş Geldiniz



username = 'ikbalkaradeli'
password = '12345'

isLoggedin = (username=='ikbalkaradeli') and (password=='1234')

if isLoggedin:
    print('Hoş Geldiniz')
else:
    print('Username ya da password yanlış')    

# Username ya da password yanlış  => password u yanlış yazdık ondan dolayı sonucumuz else kısmının altındaki printi yazdırdı.
"""
username = 'ikbalkaradeli'
password = '12345'

if  username==('ikbalkaradeli'):
    if password==('12345'):
        print('Hoş Geldiniz')
    else:
        print('password u yanlış girdiniz')    
else:
    print('username i yanlış girdiniz')    




