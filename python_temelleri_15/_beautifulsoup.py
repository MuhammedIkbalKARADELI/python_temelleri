html_doc = """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>İlk web sayfam</title>
</head>
<body>

    <h1 id="header">
        Python Kursu
    </h1>

    <div class="grup1">
        <h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup2">
        <h2>
            Modüller
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup3">
        <h2>
            Django
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <img src="fred.jpg" alt="">

    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>

</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

result = soup.prettify()  # html_doc dosyasında düzensizliği düzeltir.

result = soup.title   # <title>İlk web sayfam</title>

result = soup.head    # <head>
                      # <meta charset="utf-8"/>
                      # <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
                      # <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
                      # <title>İlk web sayfam</title>
                      # </head>

result = soup.body    # html_docs daki <body> kısmını verir.

result = soup.title.name #  title
result = soup.title.string  # İlk web sayfam

result = soup.h1          # html_docs daki <h1> kısmını verir.
result = soup.h1.name     # h1
result = soup.h1.string   # Python Kursu


result = soup.h2          # html_docs daki <h2> kısmını verir.
result = soup.h2.name     # h2
result = soup.h2.string   # Programlama

result = soup.find_all('h2')  # bütün <h2> bilgilerini verir.
result = soup.find_all('h2')[0] # <h2>  Programlama  </h2>
result = soup.find_all('h2')[1] #  <h2>  Modüller  </h2>

result = soup.div
result = soup.find_all('div')   # bütün <div> bilgilerini verir.
result = soup.find_all('div')[1]
result = soup.find_all('div')[1].ul  # 2.<div> içindeki <ul> sini verir.
result = soup.find_all('div')[1].ul.find_all('li')  # [<li>Menü 1</li>, <li>Menü 2</li>, <li>Menü 3</li>]

result = soup.div.findChildren()  # <div> in tüm alt elemanlarını B[<li>Menü 1</li>, <li>Menü 2</li>, <li>Menü 3</li>]

result = soup.findNextSibling()

result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()

result = soup.find_all('a')

print(result)


for link in result:
    print(link.get('href'))
'''
http://example1.com/elsie
http://example2.com/elsie
http://example3.com/elsie
'''
