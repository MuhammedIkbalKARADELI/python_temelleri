
# 1-100 e kadar


x = 0 

#while x < 100:
#    print(x)     # bu while döngüsünü yazdırırsam sonsuza kadar 0 yazılacak çünkü 0 herzaman 100 den büyüktür.


while  x < 100:
    print(x)     #bu while döngüsünde 0 dan 100 kadar yazdırır çünkü
    x += 1       # x += 1 yapınca x değeri her döngü sonunda 1 artıyor ve
                 # 100 olunca döngü durur çünkü while yanında değer false oluncadöngü durdurulur.

print('bitti...')


y = 1             
while y <= 100:  # bu while döngüsü 1 den başlar 101 kadar yazılır.
    print(y)
    y += 1


z = 1
while z <= 100:
    if z % 2 == 0:
        print(z)   # 1 den yüze kadar olan tüm çift sayıları yazdırır.
    z += 1         # while yanındaki ifade false olana kadar bu dögüyü devam eder.

print('bitti...')


q = 1
while q <= 100: 
    if q % 2 == 1:  # 1 den yüze kadar tüm tek sayıları yazdırır.
        print(q)
    q += 1


w = 0
while w < 100:   # true yeya false değerinin olamsı için w (belirlediğimiz ifadeyi) while değişkenindeki true false değer getircek ifadeye aktarıyoruz çünkü döngümüzün bir yerde son bulmasını ve istediğimiz değere kadar döngününü devam etmesi için kullanıyoruz ayrıca sayılarla bu işlemi yapmaya kaksak çok saçma işlemlere gireriz.
    if (w % 2) == 0:
        print(f'cift sayı: {w}')
    elif (w % 2) == 1:
        print(f'tek sayı:  {w}')   
    w += 1       # bu işlemi yapmaz sonsuza kadar hep ' çift  sayı : 0 ' yazdırır




name = ''

while not name:
    name = input('isminizi giriniz: ').strip()


print(f'Merhaba {name}')
#true olup yani (boş str ifadenin yazılmamasıdır)
# yukarıda "print(f'Merhaba {name}')"  döngünün dışında yazdık çünkü
# bunu yazdıra bilmek için döngü true olması durumunda dönünün sonlanması gerek.
# eğer  "print(f'Merhaba {name}')"  while döngüsünün içine yazılırsa print ifadesini herzaman yazdırır herzaman yazdırır ifade false olsada true olsada yazdırır.
# ama döngü bitince yani 'not name' true olunca printi bir defa yazdırır. but false olma durumunda hep bizim yazdığımız komut boyuncayazdırır. 

