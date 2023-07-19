

# file = open("newfile3.txt","r",encoding="utf-8")
# content = file.read()
# print(content)
# file.close()



# yukardaki kullanım yerine  bir kullanımdaha var.

# with open("newfile3.txt","r",encoding="utf-8") as file :
#     content = file.read()
#     print(content)



# bu kullanımda close() metodhu kullamamıza gerek yok.

# with open("newfile3.txt","r",encoding="utf-8") as file :
#     content = file.read()
#     print(content)
#     print(file.tell())  # 43  # külüsörün en son nerde olduğuunu söyler.
#     content2 = file.read()  
#     print(content2)       # burda bize bir sonuç gelmez çünkü bir kaç satır yukarda okuma fonksiyonunda tüm karakterler okundu.



# with open("newfile3.txt","r",encoding="utf-8") as file :
#     content = file.read()
#     print(content)
#     print(file.tell())    # külüsörün en son nerde olduğuunu söyler.
#     file.seek(0)          # bu kullanımda külüsörün nereye gitmesi gerektiğini söyler.
#     content2 = file.read()  
#     print(content2)   


# with open("newfile3.txt","r",encoding="utf-8") as file :
#     content = file.read(12)  #külüsörden sonra 12 tane karakteri okur.
#     print(content)
#     print(file.tell())    # külüsörün en son nerde olduğuunu söyler.
#     file.seek(5)          # bu kullanımda külüsörün 5. karakterin sağ yanına gitmesi gerektiğini söyler.
#     content2 = file.read(26)   # külüsörün en son konumundan 26 karakter okur.
#     print(content2)   