import re

# result = dir(re)

# print(result) # kullanabileceğemiz metodları bize gösterir.


#### re mdule #######

ifade = "Python Kursu: Python Programlama Rehberrimiz | 40 saat"

# re.findall()

search = re.findall("Python",ifade)
print(search)          # ['Python', 'Python']

result = len(search)
print(result)    # 2


search1 = re.findall("40",ifade)
print(search1)         # ['40']


# re.split()


result = re.split(" ",ifade)  # her boşluk karakterinden ifademezi bölmüş olur.
print(result)    # ['Python', 'Kursu:', 'Python', 'Programlama', 'Rehberrimiz', '|', '40', 'saat']


result = re.split("R",ifade)   # "R" den öncesini ve sonrasını böler.
print(result)    # ['Python Kursu: Python Programlama ', 'ehberrimiz | 40 saat']  


# re.sub()

result = re.sub(" ","-",ifade)     #bir değiştirme işlemi yapar.
print(result)    # Python-Kursu:-Python-Programlama-Rehberrimiz-|-40-saat

result = re.sub("\s","-",ifade)  # "\s" ile " " kaarakterleri aynı anlma gelir.
print(result)   # Python-Kursu:-Python-Programlama-Rehberrimiz-|-40-saat


# re.search()

match_object = re.search("Python",ifade)
print(match_object)   # <re.Match object; span=(0, 6), match='Python'>   # 0 ile 6 karakterler arasında Python karakterini bulduğunu söyler.


span_object = match_object.span()
print(span_object)         # (0, 6)


start_caharcter = match_object.start()
print(start_caharcter)      # 0


end_caharacter = match_object.end()
print(end_caharacter)       # 6


phrase = match_object.group()
print(phrase)               # Python

result = match_object.string  # aramanın yapıldığı iadeyi belirtir.
print(result)               # Python Kursu: Python Programlama Rehberrimiz | 40 saat



#### regular expression  #############

"""

    [] - Köşeli parantezler arasına yazılan bütün karakterler
         aranır.

         [abc] => a      : 1 match
                  ac     : 2 match 
                  Python : No matches

         [a-e]  => [abcde]
         [1-5]  => [12345]
         [0-39] => [01239]   

         [^abc] => abc dışındaki karakterler.
         [^0-9] => rakam olmayan karakterler.

"""

result = re.findall("[abc]",ifade)
print(result)           # ['a', 'a', 'a', 'b', 'a', 'a']

result = re.findall("[sat]",ifade)
print(result)                 #  ['t', 's', 't', 'a', 'a', 'a', 's', 'a', 'a', 't']

result = re.findall("[a-e]",ifade)
print(result)                 #  ['a', 'a', 'a', 'e', 'b', 'e', 'a', 'a']

result = re.findall("[a-z]",ifade)
print(result)                 #  ['y', 't', 'h', 'o', 'n', 'u', 'r', 's', 'u', 'y', 't', 'h', 'o', 'n', 'r', 'o', 'g', 'r', 'a', 'm', 'l', 'a', 'm', 'a', 'e', 'h', 'b', 'e', 'r', 'r', 'i', 'm', 'i', 'z', 's', 'a', 'a', 't']

result = re.findall("[0-5]",ifade)
print(result)                 # ['4', '0']

result = re.findall("[^abc]",ifade)
print(result)                 #  ['P', 'y', 't', 'h', 'o', 'n', ' ', 'K', 'u', 'r', 's', 'u', ':', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'g', 'r', 'm', 'l', 'm', ' ', 'R', 'e', 'h', 'e', 'r', 'r', 'i', 'm', 'i', 'z', ' ', '|', ' ', '4', '0', ' ', 's', 't']

result = re.findall("[^0-9]",ifade)
print(result)                 # ['P', 'y', 't', 'h', 'o', 'n', ' ', 'K', 'u', 'r', 's', 'u', ':', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'l', 'a', 'm', 'a', ' ', 'R', 'e', 'h', 'b', 'e', 'r', 'r', 'i', 'm', 'i', 'z', ' ', '|', ' ', ' ', 's', 'a', 'a', 't']



"""
    . - Her hangi bir tek karakteri belirtir.

        .. => a    : No match
              ab   : 1 match
              abc  : 1 match
              abcd : 2 matches

    
"""
result = re.findall("...", ifade)  # her üç basamklı gurubları ayırır.
print(result)

result = re.findall("..", ifade)   # her ikili karaktere ayırır.
print(result)

result = re.findall(".", ifade)    # her tekli karakterlere ayırır.
print(result)

result = re.findall("Py..on", ifade)  # istenilen ifadeyi bulur.
print(result)


"""
    ^ - Belirtilen string karakterlerle başlıyor mu ?

    ^a => a:    1 match
          abc:  1 match
          bac:  No match

"""
result = re.findall("^P",ifade)  # p ile başlıyan karakter var mı diye sorar.
print(result)     # ['P']

result = re.findall("^a",ifade)  # p ile başlıyan karakter var mı diye sorar.
print(result)     # []


"""
    $ - Belirtilen karakterle bitiyor mu ?

    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match 

"""

result = re.findall("a$",ifade)   # a ile biten bir karakter var mı diye sorar.
print(result)                  # []

result  =re.findall("n$",ifade)
print(result)                    # []
  
result  =re.findall("t$",ifade)   
print(result)                    #['t']


result  =re.findall("saat$",ifade)   
print(result)          #  ['saat']



"""
     * - Bir karakterin sıfır ya da daha fazla sayıda olmasını 
         kontrol eder.

         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""

result = re.findall("sa*t",ifade)    # burda a nın sınırı yo demesine getiriyor.
print(result)   # ['saat']

result = re.findall("py*hon",ifade)   
print(result)    # []

result = re.findall("Rehber*imiz",ifade)   
print(result)     # ['Rehberrimiz']


"""
     + - Bir karakterin bir ya da daha fazla sayıda olmasını 
         kontrol eder.

         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""
result = re.findall("sa+t",ifade)
print(result)          # ['saat']

result = re.findall("pyth+n",ifade)
print(result)          # []

result = re.findall("Rehber+imiz",ifade)
print(result)           # ['Rehberrimiz']



"""
    ? - Bir karakterin sıfır ya da bir kez olmasını 
        kontrol eder.

        ma+n => mn     : No match
                man    : 1 match
                maaan  : No match
                main   : No match (a' nın arkasına n gelmiyor.) 
"""

result = re.findall("sa?t",ifade)
print(result)        # []

result = re.findall("Pytho?n",ifade)
print(result)         # ['Python', 'Python']



"""
    {} - Karakter sayısını kontrol eder.

        al{2}   => a karakterinin arkasına l karakteri 2 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""

result = re.findall("a{2}",ifade) 
print(result)           # ['aa']

result = re.findall("[0-9]{2}",ifade)   # iki basamaklı bir sayı arar.
print(result)          #['40']

result = re.findall("x{2}",ifade) 
print(result)      # []



"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.

        a|b => a ya da b

            cde =>    no match
            ade =>    1 match
            acdbea => 3 match 
"""


"""
    () - gruplamak için kullanılır.

         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
"""






"""
    \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterinin arar. Yani
               $ regular exp. engine tarafından yorumlanmaz.

    \A - Belirtilen karakter string in başında mı ?
         \Athe => the string in başındamı

        result = re.findall("\APython", str)
        result = re.findall("saat\Z", str)

    \Z - Belirtilen karakter string in sonunda mı ?
         the\Z => the string in sonunda mı

    \b - Belirtilen karakter kelimenin in başında ya da sonunda mı ?
         \bthe => the kelimenin in başında mı?
         the\b => the kelimenin in sonunda mı?

    \B - Belirtilen karakter kelimenin in başında ya da sonunda değil mı ?
         \Bthe => the kelimenin in başında değil mi?
         the\B => the kelimenin in sonunda değil mi?
    
    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
         \d => 12abc34

    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
         \D => 1ab44_50

    \s - Boşluk karakterlerini arar.  
    \S - Boşluk karakterleri dışındakiler.
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W - \w nin tam tersi
    
"""
result = re.findall("\APython", ifade)        #  Belirtilen karakter string in başında mı ?
print(result)     # ['Python']

result = re.findall("saat\Z", ifade)          #  Belirtilen karakter string in sonunda mı ?
print(result)     # ['saat']



