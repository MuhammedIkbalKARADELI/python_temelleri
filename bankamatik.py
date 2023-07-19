
IkbalAccount = {
    'name' : 'Ikbal Karadeli',
    'Account_NO' : '123456789',
    'Balance' : 3000,
    'Additional_Balance': 2000
    }

GulAccount = {
    'name' : 'Gul Aydın',
    'Account_NO' : '567891234',
    'Balance' : 1000,
    'Additional_Balance': 4000
    } 
    
RizaAccount = {
    'name' : 'Riza Pekmez',
    'Account_NO' : '987654321',
    'Balance' : 2000,
    'Additional_Balance': 2000
    }

def withdrawMoney(hesap,Cash):
    print(f"Merhaba {hesap['name']}.")

    if hesap['Balance'] >= Cash:
        hesap['Balance'] -= Cash 
        print(f"Paranızı alabilirsiniz. And you have {hesap['Balance']} liras left in the bank account ")
    else:
        tot = hesap['Balance'] + hesap['Additional_Balance']
        
        if tot >= Cash:
            answer = input('Do you want to withdraw money from Additional balance? (Yes / No): ')
            
            if answer == 'Yes':
                EkHespKullanimi = Cash - hesap['Balance']
                hesap['Balance'] = 0
                hesap['Additional_Balance'] -= EkHespKullanimi
                print(f"You can withdraw your money. And you have only {hesap['Additional_Balance']} liras left in the bank.")
            else: 
                print(f"At the no:{hesap['Account_NO']} account there are {hesap['Balance']} TL. ")
        else:
            print(f"You don't have enough money to withdraw. ")
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"Your account there are {hesap['Balance']} liras.")

withdrawMoney(GulAccount,2000)
withdrawMoney(GulAccount,2000)
withdrawMoney(GulAccount,2000)
bakiyeSorgula(GulAccount)





