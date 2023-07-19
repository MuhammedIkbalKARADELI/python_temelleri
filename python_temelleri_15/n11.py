#### web scrabing #####

import requests
from bs4 import BeautifulSoup


url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"


html = requests.get(url).content

soup = BeautifulSoup(html,"html.parser")

# print(html) # tüm bilgileri verir.

# soup dan istenilen html bilgileri alınabilir.


list = soup.find_all("li",{"class":"column"},limit=10)   # aranan html bilgisinde li olan ve classı column olna bilginin hepsini bize aktarır.
#print(list)


for li in list:
    name = li.div.a.h3.text.strip()  # 
    link = li.div.a.get("href")  # link bilgisini verir.
    oldPrice = li.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip("TL")
    newPrice = li.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip().strip("TL")
    #print(name, link, oldPrice, newPrice,)
    print(f"Product name: {name} link: {link}  old price: {oldPrice}TL  and new price: {newPrice}")





