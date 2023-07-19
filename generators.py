# def cube():
#     result = []

#     for i in range(5):
#         result.append(i**3)
#     return result

# print(cube())

# bzim burda kullandığımız code bellek üzerinde yer kaplıyor 
# generators ile bellekde yer kaplamayan bir code yazmayı sağlar.


###############  yield  #################
# bu kullanım bellekte yer kaplamaması için kullanılan yöntemdir. Burdaki amaç kodu ihityaç olmayıp sadece sonucu ihtiyaç olan kullanımlarda kullanılır.

# def cubes():
#     for i in range(5):
#         yield i**3

# for i in cubes():
#     print(i)

# print(cubes())   # <generator object cubes at 0x0000021E7414BC10>   verir.




#####kullsanım1######
# generator = cubes()
# iterators = iter(generator)

# while True:
#     try:
#         elemnts = next(iterators)
#         print(elemnts)
#     except StopIteration:
#         break




######kullanım2########
# print(next(iterators))
# print(next(iterators))
# print(next(iterators))
# print(next(iterators)) 
# print(next(iterators))
# print(next(iterators))  # StopIteration

####################comprhensivden generatorse çevirme #########################

listeler = [i**3 for i in range(5)]          # bu chomrhensive dir.
print(listeler)                         # [0, 3, 6, 9, 12]


listeler2 = (i**3 for i in range(5))       
print(listeler2)                        # <generator object <genexpr> at 0x000001ABBB4DBB30>

for i in listeler2:
    print(i)



