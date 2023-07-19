message = 'Hello There. My name is İkbal Karadeli'
message1 = '  Hello There. My name is İkbal Karadeli'

#1 message = message.upper()  -> Bütün karkterleri büyük yazdırır. 

#2 message = message.lower()  -> Bütün karakterleri küçük harfe döndürür.

#3 message = message.title()  -> Bütün kelimelerin ilk harfini büyük yapar. 

#4 message = message.capitalize() -> Verilen str ifadenim yanlızca baş harfini büyjk yapar.

#5 message1 = message1.strip()  -> Eger str ifademizin başında boşluk karakterleri varsa onları kaldırır.

#6 message = message.split()  -> str ifademizde boşluk karakterlerinde parçlara ayırır.
 #  print(message[5])  -> parçalra ayrılan kelimereden 5. indexini bulur.

#7 message = message.split('.') -> str ifademizde "." karakterinden parçaladı.
 # print(message[1]) -> parçaalnan str ifademizden en sondaki karakteri aldı.

#8 message = message.split()
 #message = ' '.join(message) -> boşluklardan parçalara ayrılmış ifademiz şimdi ' ' karakteri ile birleştirildi.
 #message = '**'.join(message) -> .split methodu ile boşluklardan parçalra ayılmış  ifademizzi '**' karakterleriyle birleştirdik.


#9 kk = message.find('İkbal') -> str ifademizde istediğimiz kelimenin kaçınca index ten başaldığını söyler 
 #print(kk) -> 24
 #kk1 = message.find('ö') -> ifadesi bulunmadığından sonucumuz -1.
 #print(kk1) -> -1


#10 message = message.startswith('H')  -> soruyoruz bizim str ifademiz H ile mi başlıyruz.

#11 message = message.endswith('i') -> soruyoruz bizim str ifademizin sonu i ile mi bitiyor.

#12 message = message.replace('İkbal','Çınar')  -> İkbal karakterinin yerine Çınar karakteri yazar.
#13 message = message.replace(' ','**') -> ' ' karakterleri yerine ** karakterlriyle yer değiştirdik.

#14 message = message.center(100) -> str ifademizi 100 karakterlik alanın tam ortasına yazar. 
#15 message = message.center(50,'*') -> str ifademizi 50 karakterimiz tam ortasına  alarız ve bu str ifademizin iki tarafındaki boşlukların yerine * ifadesini yerleştirir.



print(message)
