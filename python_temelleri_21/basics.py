from matplotlib import lines
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#1
"""
x = [1,2,3,4]

plt.plot(x) # x eksenini belirtmeden verilen değerler y ekseni üzerinde karşılık bulur
plt.show()
"""

#2
"""
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y)  # x değerleri x esenine yerleşir  y değerleri y ekseninde yer bulur.
plt.show()
"""

#3 
"""
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y)
plt.axis([0,6,0,20]) # burda grafiğimizin ölçeklerini veririz x ekseni 0 ile 6 arasında yap  y eksenin 0 ile 20 arasında yap 
plt.show()
"""

#4
"""
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y)
plt.axis([0,6,0,20]) 
plt.title("Grafik Başlığı")  # grafiğe başlık eklemiş olduk
plt.xlabel("x label")  # grafin x eksenine bir isim koyduk
plt.ylabel("y label")  # grafiğin y eksenine bir isim verdik

plt.show()
"""

#5 
"""
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y,color="red",linewidth="5") # burda grafiğimizdeki çizgiyi kırmızı yaptık ve kalınlığını artırdık.
plt.axis([0,6,0,20]) 
plt.title("Grafik Başlığı")  
plt.xlabel("x label")  
plt.ylabel("y label")  

plt.show()
"""

#6 
"""
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y,"--g") #burda grafiğimizdeki çizgi kesik çizgili olur ve rengi yeşil(green) olur.
plt.axis([0,6,0,20]) 
plt.title("Grafik Başlığı")  
plt.xlabel("x label")  
plt.ylabel("y label")  

plt.show()
"""

#7 
"""
x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y,"o--r") # marker(işaretleyici) ı o seçtik kesik çizgili red bir cizgi elde ediceğiz 
plt.axis([0,6,0,20]) 
plt.title("Grafik Başlığı")  
plt.xlabel("x label")  
plt.ylabel("y label")  

plt.show()
"""

#8 
"""
x = np.linspace(0,2,100) # 0 ile 2 arasını 100 değere böler.

plt.plot(x,x,label="linear")
plt.plot(x,x**2,label="quadratic")
plt.plot(x,x**3,label="cubic")

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("simple plot")

plt.legend() # grafiklerin label lerini gösteren bir tablo ekrana verir.

plt.show()
"""

#9 
"""
x = np.linspace(0,2,100)

fgr, axs = plt.subplots(2)  # ekranı ikiye böler

axs[0].plot(x, x, color="red")  # istediğin tarafa istediğin grafiği yazdırabiliriz.
axs[1].plot(x, x**2, color="blue") # alt satıra yazar.

plt.show()
"""

#10
"""
x = np.linspace(0,2,100)

fgr, axs = plt.subplots(3)  

axs[0].plot(x, x, color="red", label="linear")  
axs[1].plot(x, x**2, color="blue",label="quadratic") 
axs[2].plot(x, x**3, color="yellow",label="cubic")

axs[0].set_title("linear")
axs[1].set_title("quadratic")
axs[2].set_title("cubic")

plt.tight_layout() # olşan figuredeki karışıklığı giderecek 

axs[0].legend()
axs[1].legend()
axs[2].legend()

plt.show()
"""

#11
"""
x = np.linspace(0,2,100)

fig, axs = plt.subplots(2,2)
fig.suptitle("grafik başlığı")

axs[0,0].plot(x,x,color="red")
axs[0,1].plot(x,x**2,color="blue")
axs[1,0].plot(x,x**3,color="green")
axs[1,1].plot(x,x**4,color="yellow")

plt.show()
"""
########### *********  ***************  ****************  #################
"""
df = pd.read_csv("NBA_list_new.csv")

df = df.drop(["COLLEGE"], axis=1).groupby("TEAM").mean()

df.plot(subplots=True)
df.head().plot(subplots=True) # ilkk beş takımın grafiğini verir.

plt.legend()
plt.show()
"""






