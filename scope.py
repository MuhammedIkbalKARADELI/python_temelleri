### 1 ### 
print(' 1 '.center(50,'*'))
name = 'ikbal'

def changeName(new_name):
    name = new_name  # in this name is local value.
# in this function although we assigned the name 
# we can't take result is wanted

changeName('ali')  # we can't assign 'ali' to name.
print(name) # we take result 'ikbal' because in this name is global value


### 2 ### 
print(' 2 '.center(50,'*'))

isim = 'Ayse'
def isimDegis():
    isim = 'Ahmet'
    print(isim)

isimDegis()   
print(isim) # in this usage, we did not assigne a name and we take 'Ayse' because of defining of func


### 3 ### 
print(' 3 '.center(50,'*'))

x = 'global x'

def function():
    x = 'local x'
    print(x) # we can get 'local x' in this part

function()
print(x) # we take 'global x' because 'local x' is only assigned in func
# x in the function effects only inside the func 


### 4 ### 
print(' 4 '.center(50,'*'))

character = 'global string'

def greeting():
    character = 'Cınar'

    def hello():
        print('Hello ',character)
    
    hello()
# charachter usage on both side are not same 
greeting() 
print(character)


### 5 ### 
print(' 5 '.center(50,'*'))

character = 'global string'

def greeting():
    character = 'Cınar'

    def hello():
        character  = 'Ada' # if we  asigne again a new str to charachter, this str will be our new character.
        print('Hello ',character) # priorit is inside the func
    
    hello()

greeting() 
print(character)


### 6 ### 
print(' 6 '.center(50,'*'))

y = 50

def test(y):
    print('y is ', y)

    y = 100
    print('y is changed to 100 from 50 and y =', y)

test(y) 
print(y) # y is not changed globally 
# y outside of func is 50 but y outside of func is 100 
# y inside of func is only defining in func

### 7 ### 
print(' 7 '.center(50,'*'))
# we can define value inside of func like global value

k = 100

def deneme(): # we don't need to write thevalue inside of the braclet because we define vale inside of the func by using 'global' word
    global k
    print('k is ', k)
    k = 200
    print('k change to 200 and k = ',k)

deneme()
print(k) # k both side of func are same because we use 'global' word



### 8 ### 
print(' 8 '.center(50,'*'))

