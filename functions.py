
### 1 ###
print(' 1 '.center(50,'*'))
def sayHello():
    print('Hello')

sayHello()

### 2 ###
print(' 2 '.center(50,'*'))
def SayHello(name = 'user'):  # burdaki eşitlik name girilmediğinde 'user' yazdırır. 
    print(f'Hello {name} ')

SayHello('Ikbal')  # Hello Ikbal
SayHello()  # Hello user

### 3 ###
print(' 3 '.center(50,'*')) 
def meraba(name = 'kullanıcı'): 
    return 'Merhaba ' + name   # return kullanarak oluşturduğumuz fonksiyona
                              # değeri atamış oluruz.
 # ama yukardaki gibi print yazmış olsaydık değeri bir değişkene atamazdı

msg = meraba('Ali')
print(msg)


### 4 ### 
print(' 4 '.center(50,'*'))
def tot(num1, num2):
    return num1 + num2

result = tot(13, 115)
print(result)

### 6 ### 
print(' 6 '.center(50,'*'))
def top(a,b,c=0,d=0,e=0): # burda bazı değerler  eşittir 0 yaptık çünkü eksik elemanda değer girildiğinde hata vermesin ve fon çalışsın
    return sum((a,b,c,d,e))

result1 = top(2,3,43,5)
print(result1)

### 7 ###
print(' 7 '.center(50,'*'))
# yukrada ki gibi herseferinde eleman sayısını belirlemektense aşağıdaki gibi çoklu sayılar için uygulnabilir.
def total(*numbers):  # çoklu değerler için geçerli eski derslerde anlatılmıştı bir benzeri
    print(numbers)
    return sum((numbers))

sonuc = total(12,13,14,15,25,36,47,47,24,69) 
print(sonuc)   

### 8 ###
print(' 8 '.center(50,'*'))
def yasHesapla(dogumYılı):
    return 2021 - dogumYılı

ageAyse = yasHesapla(1976)
ageIkbal = yasHesapla(2001)
ageUmit = yasHesapla(1973)
ageEsra = yasHesapla(2002)    

print(ageAyse, ageEsra, ageIkbal, ageUmit)

### 9 ###
print(' 9 '.center(50,'*'))

def emekliligeKacYilKaldi(dogumYili, isim):
    '''  
    DOCSTRING: Dogum  yiliniza gore emekliliginize kac yil kaldi
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    '''
    # yukardaki kısım açıklma kısmı help fon. ile bulunur
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'emekliliğinize {emeklilik} yıl kaldı.')
    else:
        print('Zaten emeklisiniz. ')


emekliligeKacYilKaldi(2001,'ikbal')

print(help(emekliligeKacYilKaldi))

### 10 ###
print(' 10 '.center(50,'*'))
list= [1,2,3]
print(help(list.append))

