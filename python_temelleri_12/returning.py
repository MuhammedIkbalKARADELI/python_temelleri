def usalma(number):
    
    def inner(power):
        return number ** power

    return inner                  #burda sadece fonksiyonun adını yazdık çalıştırmadık.

two = usalma(2)      
three = usalma(3)    

print(two(3))        # 8
print(three(3))      # 27 
print(three(4))      # 81


def yetki_sorgula(page):
    def inner(role):
        if role == "Admin":
            return "{0} rolünü {1} sayfasına ulaşabilir.".format(role,page)
        else: 
            return "{0} rolünü {1} sayfasına ulaşamaz.".format(role,page)
    return inner

user1 = yetki_sorgula("Product Edit")
print(user1("Admin"))              # Admin rolünü Product Edit sayfasına ulaşabilir.

user2 = yetki_sorgula("Product Edit")
print(user2("Çalışan"))            # Çalışan rolünü Product Edit sayfasına ulaşamaz.





def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam+= i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim*= i
        print(carpim)

    if islem_adi == "carpma":
        return carpma 
    elif islem_adi == "toplama":
        return toplam


top = islem("toplama")
print(top(3,5))       #8
    

carp = islem("carpma")
carp(6,9)      #54    # carpma func da sonuda return yerine print yazdığımızdan burda karaktere eşitlememiz gerekmedi
