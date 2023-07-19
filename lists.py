#message = 'Hello There. My name is Sadık Turan'.split()
#print(message)  # sonucumuz = ['Hello', 'There.', 'My', 'name', 'is', 'Sadık', 'Turan
                 #                0        1        2      3      4      5        6       

#print(message[2])  # sonucumuz = My

my_list = [1,2,3]
my_list = ['bir',2,True,5.6]
print(my_list)   

list1 = ['one','two','three']
list2 = ['four','fife','six']

numbers = list1 + list2 # ['one', 'two', 'three', 'four', 'fife', 'six']
print(numbers)
print(len(numbers)) # 6


numbers1 = list1,list2
print(numbers1) # (['one', 'two', 'three'], ['four', 'fife', 'six'])
print(len(numbers1))  # 2


numbers2 = [list1,list2]
print(numbers2) #  ['one', 'two', 'three'], ['four', 'fife', 'six']]
print(len(numbers2))  # 2 

print(numbers1[1]) # ['four', 'fife', 'six']
print(numbers1[1][2]) # six


print(numbers2[0]) # ['one', 'two', 'three']
print(numbers2[0][1]) # two





userA = ['Sadık', 36]
userB = ['Çınar', 2]

users = userA + userB
print(users) # ['Sadık', 36, 'Çınar', 2]

users1 = [userA,userB]
print(users1) # [['Sadık', 36], ['Çınar', 2]]

print(users1[1][0]) # Çınar
