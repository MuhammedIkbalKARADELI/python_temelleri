from matplotlib import colors
import matplotlib.pyplot as plt


yil = [2011,2012,2013,2014,2015]

oyuncu1 = [8,10,12,7,9]
oyuncu2 = [7,12,5,15,21]
oyuncu3 = [18,20,22,25,19]


# Stack Plot
"""
plt.plot([],[],color="y",label="oyuncu1")
plt.plot([],[],color="r",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3")

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=["y","r","b"])

plt.title("yıllara göre atılan goller")
plt.xlabel("yil")
plt.ylabel("Gol sayısı")

plt.legend()
plt.show()
"""


# Pie Plot
"""
goal_types = "Penaltı", "Kaleye Atılan Şut", "Serbest Vuruş"

goals = [12,35,7]

colors = ["y","r","b"]

plt.pie(goals,labels=goal_types,colors=colors, shadow=True, explode=(0.05,0.05,0.05), autopct="%1.1f%%" )
plt.show()
"""

# Bar Plot
"""
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5,color="r")
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi",width=.5,color="y")

plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe (km)")
plt.title("Araç bilgileri")

plt.show()
"""

# Histogram Plot

from numpy import random

x = random.randint(100, size=(50))

yaslar = x
yas_grupları = [0,10,20,30,40,50,60,70,80,90,100]


plt.hist(yaslar,yas_grupları,histtype="bar",rwidth=0.8)

plt.xlabel("yaş grupları")
plt.ylabel("kişi sayısı")
plt.title("Histogram graiği")

plt.show()




