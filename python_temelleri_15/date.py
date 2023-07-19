
#################1#################### 
# import datetime   # bu kullanımda herseferinde datetime modülünü kullanmak zorunda oluyoruz.

# result = dir(datetime)  # give us the class of datetime module
# print(result)

# result1 = dir(datetime.datetime)
# result2 = dir(datetime.date)
# result3 = dir(datetime.time)   # give us property of class

# print(result1)
# print(result2)
# print(result3)



################2###############
# bu kullanımda datetime ı her sefinde kullanmamız gerekmiyor.
# from datetime import datetime
# from datetime import date
# from datetime import time

# result1 = dir(datetime)
# result2 = dir(date)
# result3 = dir(time) 

# print(result1)
# print(result2)
# print(result3)


###############3#####################

from datetime import datetime


suan = datetime.today()  # 2021-07-18 11:35:22.137708   
suan = datetime.now()   # 2021-07-18 11:35:22.137708    şuanın tarihini verir.
print(suan)

suan1 = suan.year
suan2 = suan.month
suan3 = suan.day
suan4 = suan.hour
suan5 = suan.minute
suan6 = suan.second
print(suan1)
print(suan2)
print(suan3)
print(suan4)
print(suan5)
print(suan6)

##################4###################
# if you want more detail about now, you can use this 

result = datetime.ctime(suan)        # Sun Jul 18 11:45:46 2021
print(result)

################5################

simdi1 = datetime.strftime(suan,'%Y')          #2021 
simdi2 = datetime.strftime(suan,'%d')          #18  ->  day
simdi3 = datetime.strftime(suan,'%A')          #Sunday
simdi4 = datetime.strftime(suan,'%B')          #July
simdi5 = datetime.strftime(suan,'%X')          #11:49:29
simdi6 = datetime.strftime(suan,'%Y %B %A')    # 2021 July Sunday
print(simdi1)  
print(simdi2)  
print(simdi3)  
print(simdi4) 
print(simdi5) 
print(simdi6) 

##############6############

t = '21 April 2021 hour 12:34:23'
dt = datetime.strptime(t,'%d %B %Y hour %H:%M:%S')  # t oobjesinin formatını kendisi çevridi.
print(dt)                # 2021-04-21 12:34:23


###############7################
# kendimiz bir zaman objesi tanımlaya biliriz.
birhday = datetime(2001,4,7,10,12,30)
print(birhday)

second_information = datetime.timestamp(birhday) # bizim birthday objesinin saniye cinsinde ifadesine çeviri.
print(second_information)         # 986627550.0

date_information = datetime.fromtimestamp(second_information)  # saniye ifadesini tarih ifadesine çeviri.
print(date_information)          # 2001-04-07 10:12:30

referans_zaman = datetime.fromtimestamp(0)  #  tarihelri saniyeye çevirirken referans için kullanılan zaman
print(referans_zaman)          # 1970-01-01 03:00:00       # bilgisiyarler için  kullanılan milad bilgisi.



difference = suan - birhday
print(difference)   #7407 days, 1:52:16.232919    # timedelta

difference_day = difference.days
print(difference_day)   # 7407

difference_second = difference.seconds
print(difference_second)      # 6927



##################7#################
from datetime import timedelta

add_day = suan + timedelta(days=10)  # şuanki tarihdeki güne 10 gün ekler.
print(suan)      # 2021-07-18 12:10:24.753487
print(add_day)   # 2021-07-28 12:10:24.753487

add = suan + timedelta(days=20, minutes=32)
print(suan)    # 2021-07-18 12:12:18.465476
print(add)     # 2021-08-07 12:44:18.465476


take_out_day = suan - timedelta(days=10)
print(suan)         # 2021-07-18 12:14:39.146618
print(take_out_day) # 2021-07-08 12:14:39.146618



