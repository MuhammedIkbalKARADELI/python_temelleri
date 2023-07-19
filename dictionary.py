#sehirler = ['kocaeli','istanbul']
#plakalar = [41, 34]

#print(plakalar[sehirler.index('kocaeli')])
#print(plakalar[sehirler.index('istanbul')])






# şimdi amacımız yukarıdaki kadar işlem yapmadan sonuca varmak.
# amaç print(plakalar['kocaeli']) =>  41


#plakalar = {'kocaeli': 41, 'istanbul': 34}

#print(plakalar['kocaeli'])  # belirttiğimiz karakterin eşleştirdiğimiz karakteri verir.

#plakalar['ankara'] = 6   # sülü paratenze yazdığımız bilgiyi aktarır. {'kocaeli': 41, 'istanbul': 34, 'ankara': 6}
#print(plakalar) 

#plakalar['kocaeli'] = 'new value'  # kocaeli karşılığını değiştiririz.   {'kocaeli': 'new value', 'istanbul': 34, 'ankara': 6} 
#print(plakalar)  


"""
users = {
    'ikbalkaradeli': 19,
    'esrakaradeli':18
}

print(users['ikbalkaradeli'])  # 19
print(users['esrakaradeli'])   # 18
"""

users = {
    'ikbalkaradeli': {
        'age': 37,
        'roles': ['admin','user'],
        'email': 'ikbal@gmail.com',
        'address': 'aydın',
        'phone': '24323523523'
    }, 
    'esrakaradeli': {
        'age': 18,
        'roles': ['user'],
        'email': 'esra@gmail.com',
        'address': 'aydın',
        'phone': '43634634664'    }
}

print(users['ikbalkaradeli']) # {'age': 37, 'email': 'ikbal@gmail.com', 'address': 'aydın', 'phone': '24323523523'}
print(users['ikbalkaradeli']['age'])  # 37
print(users['ikbalkaradeli']['email']) # ikbal@gmail.com
print(users['ikbalkaradeli']['address']) # aydın
print(users['ikbalkaradeli']['phone'])   # 24323523523

print(users['esrakaradeli']) # {'age': 18, 'email': 'esra@gmail.com', 'address': 'aydın', 'phone': '43634634664'}
print(users['esrakaradeli']['age'])   # 18
print(users['esrakaradeli']['email'])  # esra@gmail.com
print(users['esrakaradeli']['address']) # aydın
print(users['esrakaradeli']['phone'])  # 43634634664

print(users['ikbalkaradeli']['roles'][0]) # admin
print(users['ikbalkaradeli']['roles'][1]) # user
print(users['esrakaradeli']['roles'][0])  # user


print(users) #{'ikbalkaradeli': {'age': 37, 'email': 'ikbal@gmail.com', 'address': 'aydın', 'phone': '24323523523'}, 'esrakaradeli': {'age': 18, 'email': 'esra@gmail.com', 'address': 'aydın', 'phone': '43634634664'}}


