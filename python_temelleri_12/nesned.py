
##################1#####################
# def greeting(name):
#     print("Hello",name)

# print(greeting("Ali")) # Ali
# print(greeting)     # <function greeting at 0x0000021CAA1ECEE0>  (bir func olduğunu ve bellekte bir adreste kayıtlı olduğunu gösterir.)

# sayHello = greeting   # aynı adrese bağlantı kurar.
# print(sayHello)    # <function greeting at 0x0000013356C0CEE0>
# print(greeting)    # <function greeting at 0x0000013356C0CEE0>

# greeting("ali")    # Hello ali     
# sayHello("ali")    # Hello ali      # aynı func eşitleyince çalışma prensibide aynı olur.


# del sayHello       #burda sayHello yu silmemiz sadece sayHello kullanımını sileriz fakat greeting deki func adrsini silmez.
# print(sayHello)    # NameError: name 'sayHello' is not defined
# print(greeting)    # <function greeting at 0x000001D2282FCEE0>



########################2######################
#######2.1########
# def outer(num1):
#     def inner_increment(num1):
#         return num1 + 1

# outer(10) # istediğmiz sonucu vermez çünkü inner func outer func içinde sadece tanımladık çalıştırmadık.


########2.2##########
#encapsulation
# def outer(num1):
#     print("outer")
#     def inner_increment(num1):      # inner fonksiyonu outer ın içinde tanımladığımızdan yanlızca outer fonksiyonunda alışır dışında inner fonksiyonu tanımsız olur.
#         print("inner")
#         return num1 + 1
#     num2 = inner_increment(num1)    # inner func u, outer func un içinde çalıştırdık 
#     print(num1)
#     print(num2)

# outer(10)

########### 3 ##########

# def factorial(number):
#     if not isinstance(number,int):
#         raise TypeError("Number must be an intager.")
#     if not number >= 0:
#         raise ValueError("Number must be zero")
#     def inner_factorial(number):
#         if number<=1:
#             return 1
#         return number * inner_factorial(number-1)
#     return inner_factorial(number)


# print(factorial(8))

# print(factorial(5))
# print(factorial(0))
# print(factorial(-2))         # ValueError: Number must be zero
# print(factorial("dsg"))     # TypeError: Number must be an intager.


# try: 
#     print(factorial(-6))
# except Exception as ex:    # Number must be zero
#     print(ex)

