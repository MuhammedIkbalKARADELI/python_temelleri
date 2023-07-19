from selenium import webdriver
import time


driver = webdriver.Chrome()

url = "http://github.com"

driver.get(url)  # istediğimiz dosyayı açar 

time.sleep(2)   # iki saniye bekler

driver.maximize_window()  # aram yapılan pencere büyütülür.

# driver.save_screenshot("github.com-homepage.png")  # istenilen ad ile ekra fotosu kaydedilir.

url = "http://github.com/sadikturan"
driver.get(url)

print(driver.title) # aradığımız şeyin başlığını yazar.

if "sadikturan" in driver.title:
    driver.save_screenshot("github-sadikturan.png")


time.sleep(2)   # iki saniye daha bekler

driver.back()  # eski sayfaya geri döner.

# driver.forward()  # ileri sayfaya döner.
 
time.sleep(2) 

driver.close() # sürücüyü kapatır.


