"""
    1- Bir Müşterinin aşağıdaki bilgileri için değişken oluşturunuz

    Müşteri adı
    Müşteri soyadı
    Müşteri adı + soyadı
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müşteri doğum yılı
    Müşteri adres bilgisi
    Müşteri yaşı
"""
musteriAdi = 'Ali'
musteriSoyad = 'Yılmaz'
musteriAdSoyad = musteriAdi + ' ' + musteriSoyad
musteriCinsiyet = True # Erkek
musteriTcKimlk = '12345678910'
musteriDogumYili = 1989
musteriAdresi = 'İstanbul Kadıköy'
musteriYaşi = 2020 - musteriDogumYili



"""
    2- Aşağıdaki siparişlerin toplam bilgisi

    Sipariş 1 => 100    TL
    Sipariş 2 => 1100.5 TL
    Sipariş 3 => 356.95 TL
"""   


order1 = 110
order2 = 1100.5
order3 = 356.95

total = order1 + order2 + order3

print("total:" ,  total)
# buradaki "total:" yazısı bir kod degil, py ile yazdırınca total(beyaz yazılı olan) ın önünde yazı olarak sonuç veriyor (zaten string bir yapı)


a = '110'
b = '1100.5'
c = '356.95'       
 
kko = a + b + c
  
print('sacma bir sayı: ', kko)  
  