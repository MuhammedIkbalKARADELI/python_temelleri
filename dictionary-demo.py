"""

ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '532 000 00 01'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '532 000 00 02'
    },
    '128': {
        'ad': 'Volkan',
        'soyad': 'Yükselen',
        'telefon': '532 000 00 03'
    }
}
    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız
        dictionary içinden saklayınız.

    2- Öğrenci numarası kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.      

"""

ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("öğrenci telefon: ")

#ogrenciler[number] = {
#    'ad': name,
#    'soyadı': surname,
#    'telefon': phone    
#}       # {'120': {'ad': 'ali', 'soyad': 'kar', 'telefon': '543 000 00 00'}}

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})


number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soadı: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})


number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soadı: ")
phone = input("öğrenci telefon: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})


#print(ogrenciler)   # {'120': {'ad': 'ali', 'soyad': 'kar', 'telefon': '543 000 0001'}, '140': {'ad': 'ahmet', 'soyad': 'sül', 'telefon': '543 000 0002'}, '160': {'ad': 'mehmet', 'soyad': 'ay', 'telefon': '543 000 0003'}}

print('*'*50)

ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[ogrNo]


print(f"Araığımız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']} ")
# yukarıda format boşluğuna "ogrenci['ad']" yazdık çünkü "ogrenci = ogrenciler[ogrNo]"
# ogrNo = bir str ifadedir ve istenen ifadeyi yazar ikisinide yapan şey ise input olması.
# bu da ihtiyacı karşılar
# ogrenci['ad'] = ogrenciler[ogrNo]['ad']