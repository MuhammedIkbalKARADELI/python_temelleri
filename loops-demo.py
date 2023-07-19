import random
sayi = random.randint(1,10)
can = int(input('hakkınızı belirtiniz: '))
hak = can  
sayac = 0

while 0 < hak:
    hak -= 1
    sayac += 1
    tahmin = int(input('bir sayı giriniz: '))
    
    if sayi == tahmin:
        print(f'Tebrikler {sayac}. defada bildiniz ve aldığınız puan:{100 - ((100/can)*(sayac-1))} ve bulduğunuz sayı doğru')
        break    
    elif sayi > tahmin:
        print('yukarı')
    else:
        print('aşağı')

    if hak == 0:
        print(f'hakkınız bitmiştir ve tutulan sayı {sayi} dir. ') 




