import requests
from bs4 import BeautifulSoup
import json

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

response = requests.get(url)

print(response)  # <Response [200]>


html = requests.get(url).content
#print(html)   # url adresindeki tüm bilgileri yazdırır.


soup = BeautifulSoup(html,'html.parser')
# print(soup) # tüm html yazılım bilgilrini aktarır.


# list = soup.find_all('tbody') # burda bütün tbody leri yazdırır.
# list = soup.find("tbody") # tbody  birkaç tane olmasına rağmen ilk tbody  yi alır.
# list = soup.find("tbody", {"class":"lister-list"}) # tbody deki bu klasa sahip olanını yazdırır.

list1 = soup.find("tbody", {"class":"lister-list"}).find_all("tr") # tbody deki bu klasa sahip olanının tr kısımlarını yazdırır.  ve bu kullanımla isteğimiz veriyi en kısa şekilde alma şeklidir. ve en etkilisi gibi görünüyor.
list2 =  soup.find("tbody", {"class":"lister-list"}).find_all("tr",limit=1)  # 1 tane tr bilgisi yadırır yukardaki liste1 deki gibi 250 tane yani tüm tr bilgilerini yazdırmaz.

#print(list2)


for tr in list2: 
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    # print(title)    #  The Shawshank Redemption  yukardaki döngüde kullanılan liste deki limit=1 olduğundan birtane veri aldık
    year = tr.find("td",{"class":"titleColumn"}).find("span").text
    #print(year)     #  (1994)   
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    print(title, year, "imdb rating: ", rating)


count = 1
for tr in list1: 
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    #print(title)   # burda 250 tane tr dosyasındaki td deki class ı titleColumndan 'a' dan bilgileri alır. Bu bilgiler filim isimlerideri. 
    year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip('()')
    #print(year)    # burda 250 tane tr dosyasındaki td deki class ı titleColumndan 'span' dan bilgileri alır. Bu bilgiler yıl bilgileridir. 
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    #print(rating)   # burda 250 tane tr dosyasındaki td deki class ı ratingColumn imdbRating 'strong' dan bilgileri alır. Bu bilgiler imdb rating bilgileridir.. 
    #print(title, year, " imdb rating:"+rating)
    print(f"{count}- film: {title.ljust(52)} yıl: {year}  Değerlendirme: {rating}")
    count+=1





