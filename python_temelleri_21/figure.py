import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



#1
"""
x = np.linspace(-10,9,20)
y = x**3

figure = plt.figure()

axes = figure.add_axes([0.2,0.2,0.8,0.8]) # figure olan sayfayı etkiliyor 

plt.show()
"""

#2
"""
x = np.linspace(-10,9,20)
y = x**3

figure = plt.figure()
axes = figure.add_axes([0.1,0.1,0.8,0.8]) # figure da boyutlarını oluşturduk

axes.plot(x,y,'b')
axes.set_xlabel("X axis")
axes.set_ylabel("Y axis")
axes.set_title("Cube")

plt.show()
"""



#2 
"""

x = np.linspace(-10,9,20)
y = x**3
z = x**2

figure = plt.figure()
axes_cube = figure.add_axes([0.1,0.1,0.8,0.8]) 

axes_cube.plot(x,y,'b')
axes_cube.set_xlabel("X axis")
axes_cube.set_ylabel("Y axis")
axes_cube.set_title("Cube")


axes_square = figure.add_axes([0.15,0.6,0.25,0.25])

axes_square.plot(x,z,"r")
axes_square.set_xlabel("x axis")
axes_square.set_ylabel("y axis")
axes_square.set_title("square")

plt.show()

# burda bir figure içne bir figure daha çizdik ve bu figürlerde de grafik çizdik

"""

#4
"""
x = np.linspace(-10,9,20)
y = x**3
z = x**2

figure = plt.figure()

axes = figure.add_axes([0,0,1,1])

axes.plot(x,z,label="square",color="red")
axes.plot(x,y,label="cub",color="blue")

#axes.legend(loc=1)  # legend sağ üst köşeye gelir.
#axes.legend(loc=2)   # legend sol üst köşeye gelir.
#axes.legend(loc=3)    # legend sol alt köşeye gelir.
axes.legend(loc=4)    # legend sağ alt köşeye gelir.

plt.show()
"""

#5

x = np.linspace(-10,9,20)
y = x**3
z = x**2

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(5,6)) # burda figurümüze boyut verdik (5,6) ve subplotumuzun yapısı söyleik 2 row 1 column olduğunu

axes[0].plot(x,z)
axes[0].set_title("square")

axes[1].plot(x,y)
axes[1].set_title("cube")

plt.tight_layout()

fig.savefig("figure1.png")  # png formatında figurümüzü kayıt etik
           # burda pdf formatında kayıt ettiğinde boyutları korunarak kayıt edilir.
plt.show()
