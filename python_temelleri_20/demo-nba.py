import pandas as pd

data = pd.read_csv("NBA_list_new.csv") # burdaki kullanımda df olarakgetirir bize
print(data)


# 1- ilk 10 kaydı getiriniz.
result1 = data.head(10)
print(result1)


# 2- Toplam kaçkayıt vardır?
result2 = data.apply(len)["PLAYER"]
print(result2)  # 530
"yada"
result2_1 = len(data.index)
print(result2_1) # 530

# 3- Tüm oyuncularınn toplam yaş ortalaması nedir.

data2 = data.dropna(subset=["AGE"])  # AGE columundaki nan olan rowlar atılır. 
sum = data2["AGE"].sum()
number =  data2.apply(len)["AGE"]
mean = sum/number

print(mean)
"yada"

mean_age = data["AGE"].mean() # böylebir kısa kullanım mevcut.
print(mean_age)

# 4- yaşı en büyük kimdir? 

older = data2["AGE"].max() # 42
print(older)

print(data2[data2["AGE"] == older]["PLAYER"])  # 507    Vince Carter
                                               # Name: PLAYER, dtype: object

print(data2[data2["AGE"] == older]["PLAYER"].iloc[0])  # Vince Carter


# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oyundakları takım nedir?

youngs = data2[(data2["AGE"] >= 20) & (data2["AGE"] < 25)].sort_values("AGE")
print(youngs[["PLAYER","TEAM"]])
"yada"
print(data2[(data2["AGE"] >= 20) & (data2["AGE"] < 25)].sort_values("AGE")[["PLAYER","TEAM"]])

# 7- "Zach Lofton" isimli oyuncunun oynadığı takım hangisidir.

index = data["PLAYER"].str.find("Zach Lofton")
data["Index"] = index
print(data)
print(data[data["Index"]>-1]["TEAM"])
"yada"
print(data[data["PLAYER"] == "Zach Lofton"][["PLAYER","TEAM"]] )  # 526  Zach Lofton  DET


# 8- Takımlara göre oyuncuların ortalama yaş bilgisi nedir?

teams = data.groupby("TEAM")
# for player in teams:
    # print(player)

mean_age = data.groupby("TEAM")["AGE"].mean()
print(mean_age)



# 9- Kaç farklı takım mevcut?

print(len(teams))
"yada"
print(data["TEAM"].nunique())
"yada"
print(data["TEAM"].unique())  # team deki verileri verir ama tekrar edeni vermez.
"""
['ORL' 'IND' 'OKC' 'BOS' 'POR' 'BKN' 'SAC' 'LAL' 'ATL' 'GSW' 'NYK' 'PHI'
 'DET' 'NOP' 'MIN' 'LAC' 'CLE' 'CHI' 'HOU' 'MEM' 'MIA' 'CHA' 'WAS' 'MIL'
 'DEN' 'SAS' 'TOR' 'DAL' 'UTA' 'PHX']
"""

# 10- Her takımda kaç oyuncu oynamaktadır?

count_players_in_team = data.groupby("TEAM")["PLAYER"].count()
print(count_players_in_team)
"yada"
playeer_count_team = data["TEAM"].value_counts()
print(playeer_count_team)


# 11- İsim içinde "and" geçen kayıtları bulunuz.

index_and = data["PLAYER"].str.find("and")
player_and = data[index_and>-1]["PLAYER"]
print(player_and)

"yada"

include_and = data[data["PLAYER"].str.contains("and")]["PLAYER"]
print(include_and)

"yada"

def str_find(name):
    if "and" in name.lower():
        return True
    return False
    
result = data[data["PLAYER"].apply(str_find)]["PLAYER"]
print(result)













