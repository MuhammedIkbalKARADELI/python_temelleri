from githubUserInfo import username, password
from selenium import webdriver
import time


class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)   # burda istenilen html bilgi kısmının üstüne mousun asağ kısmına basıp ordan copy segmentinden copy xpath kısmını seçerek aldık ve bu yöntem çok daha kolay bir yöntemdir. 
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)  # bu aldığımı şeyler github sitesinin password ve username kısmıdır ve buraya biz kendi bilgilerimizi "send_keys()" ile bilgilerimizi aktarabiliriz. 
        
        time.sleep(1)

        self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]").click() #burda aynı yukardaki gibi copy xpath ile sign in tuşuna basmamız için .click() komutu kı-ullanılıyor.
        

    def loadFollowers(self):
        items = self.browser.find_elements_by_css_selector(".d-table.table-fixed")

        for i in items:
            self.followers.append(i.find_element_by_css_selector(".link-gray.pl-1").text)


    def getFollower(self):
        self.browser.get("https://github.com/MuhammedIkbalKARADELI?tab=followers")
        time.sleep(2)

        while True:
            links = self.browser.find_element_by_class_name("BtnGroup").find_elements_by_tag_name("a")

            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(1)
                    self.loadFollowers()
                else: 
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(1)
                        self.loadFollowers()
                    else:
                        continue



github = Github(username, password)

github.signIn()

github.getFollower()
print(len(github.followers))
print(github.followers)






