# valu

x = 5 # 5
y = 25 # 25

x = y # 25
y = 10  # 10

print(x,y)  # 25 10

# reference type => list

a = ['apple','banana']
b = ['orange','banana']

#print(a,b) # ['apple', 'banana'] ['orange', 'banana']

a = b

b[1] = 'grape' 


print(a,b)   # ['orange', 'grape'] ['orange', 'grape']
# burada b nin bir karakterini değiştirdik ve a nın karakterleride b nin karakterleeriyle aynısı oldu
# ve b de hangi değişikliği yapsakta a nın karakterleirde hep b nin ki gibi olacak. 