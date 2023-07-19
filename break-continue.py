
  # for - => break - countiue

name = 'ikbal karadeli'

for word in name:
  print(word)
'''
i
k
b
a
l

k
a
a
d
e
l
i
'''

for word in name:
    if word == 'a':
        break
    print(word)
# burada for döngüsünde a eşşit eşit word döngüsüne denk geldiğinde döngü orda durduruluyor.
# ve ifadenin döngüsü geri kalan karakterler için devam etmiyor
'''
i
k
b
'''

for word in name:
    if word == 'b':
        continue
    print(word)
 
# döngüde her b karakteri denk geldiğinde onu yazdırmaz ve dögüye devam eder. 
'''
i
k
a
l

k
a
r
a
d
e
l
i
'''

for word in name:
    if word == 'i':
        continue
    print(word)
'''
k
b
a
l

k
a
r
a
d
e
l
'''

fruits = ['apple', 'banana', 'orange']

for x in fruits:
    print(x)
    if x == 'banana':
        break
'''
apple
banana
'''

for x in fruits:
    if x == 'banana':
        break
    print(x)    
'''
apple
'''

#   while => break - countinue

x = 0

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1

'''
0
1
'''
while x < 5:
    print(x)
    if x == 2:
        break
    x += 1
'''   print() ifadesinin nereye yazılması gerektiğindeki önem
0
1
2     
'''   

'''
i = 0
while i < 20:
    if i == 3:
        continue
    print(i)
    i += 1
 
 # burda dura kalır çünkü artı birir countinue dan sonra yazdığımızdan kaynaklı
 # çünkü continue dan sonra döngüde komutlar atlanır ve başa tekrar başlar.
 ''
0
1
2  
burda break dan faklı olarak hep 012 yazar sonsuza kadar çünkü while döngüsü (i +=1 okunmadığından) hep true oluyor.    
ctrl + c ile sonlandırırsın terminalden 
'''


q = 0

while q < 6:
    q += 1
    if q == 3:
        continue
    print(q)
  
# not :  burda önemli olan   'q += 1' nereye yazdığın
'''
1
2
4
5
6
'''


#  1 - 100  arasındaki tek sayıların toplamı

top = 0
w = 0 
while w < 100:
    w += 1
    if w % 2 == 0:
        continue   # for ve while döngüler için döngünün başına dön ve yani geri kalan dögünün devamını getirme demek  
    print(w)        # eğer if ifadesi doğruysa   
    top += w 
# biz nezaman toplam işlemini yapmasını istiyoruz ?
# tek sayılar olunca o yüzden çift sayı gelince toplama yapmasın diye continuo yu w += 1 in öncesnde kullanıyoruz.

print(top)  # 2500

# not # 

# döngülerde continue dan a sonra gelen komutlar işleme alınmaz eğer 'if' ifadesindeki işlem gerçekleşirse 
#  ve döngüyü kaldığı öbür işlemden tekrar başlar.


 