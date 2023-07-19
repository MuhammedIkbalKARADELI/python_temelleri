from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # burdan mousle yapaağımız olan işlemi yapabilmek için keyleri import ettik.
import time


driver = webdriver.Chrome()

url = "http://github.com"

driver.get(url)


searchInput = driver.find_element_by_name("q")  # araştırlıan websitesinde element adı "q" olanı arar. ve ordaki bilgi arama yeridir.
                        # burda bir elaman aradığımızdan element yazdık
time.sleep(1)

searchInput.send_keys("python")   # arama yerine "python yazar"

time.sleep(2)

searchInput.send_keys(Keys.ENTER) # yazılan bilgiyi enter yapar ve aratır.

time.sleep(2)

# result = driver.page_source     # bunu soup modülü ile kullanılabilir. burda sadece tüm kaynak kodu verir bize.
# print(result)


result = driver.find_elements_by_css_selector(".repo-list-item .text-normal a")  # class div vb ifadelerin bilgilerini bulmak için o ifadenin "str"sinin başına '.' konmalı ve bir onceki ifadenin altındaki ifade için arasına boşluk konulup istenilen ifdenin kendisi yazılmal örneğin a div h3 vb.

for element in result:  # burda aradığımız "python" karakteri altındaki tüm bilgileri bize aktarır. 
    print(element.text)

driver.close()


