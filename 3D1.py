


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



print("3 Boyutlu yüzey görüntüleme grafiğini hoş geldiniz\n")
print("aşağıda renk paletlerinin isimleri ve özellikleri gösterilmiştir, lütfen kullanacağınız renk paletinin ismini yazınız\n\n")
print("Viridis: Güçlü ve göz yormayan, renk körlüğüne duyarlı bir palet.\n\nPlasma: Daha canlı, yüksek kontrastlı renkler.\n\nInferno: Sıcak renk tonları, parlak sarıdan kırmızıya.\n\nMagma: Daha yumuşak ve koyu renk tonları.\n\nCividis: Görme engelli kullanıcılar için optimize edilmiş bir palet\n\nRainbow: Renkli bir spektrum, ancak genellikle bilimsel görselleştirmelerde önerilmez.")
print("\n")

binary=str(input("lütfen renk paletinizin ismini yazınır "))


a=-1
b=-1
c=-1
d=-1
e=-1
f=-1


k= str(input("lütfen x eksenine koyacağınız ismi yazınız = "))
print("\n")
l= str(input("lütfen y eksenine koyacağınız ismi yazınız = " ))
print("\n")
m= str(input("lütfen z eksenine koyacağınız ismi yazınız = "))
print("\n")
o= input("lütfen X ve Y denklemlerini yazınız (Dikkat burada kullanılan fonksiyon bir güvenlik açığı bırakan bir fonksiyondur o yüzden X ve Y yi büyük yazmaya dikkat ediniz)")
print("\n")
w= int(input("lütfen grafiğin geniştlik değerini giriniz = "))
print("\n")
h= int(input("lütfen grafiğin yükseklik değerini giriniz = "))
print("\n")
a= int(input("lütfen x ekseninin başlangıç noktasını yazınız = "))
print("\n")
b=int(input("lütfen x ekseninin bitiş noktasını yazınız = "))
print("\n")
d= int(input("lütfen y ekseninin başlangıç noktasını yazınız = "))
print("\n")
e=int(input("lütfen y ekseninin bitiş noktasını yazınız = "))
while  c<0 or f<0:
    c= int(input("lütfen x eksenlerinin arasındaki mesafeyi giriniz noktasını giriniz = "))
   
    f= int(input("lütfen y eksenlerinin arasındaki mesafeyi giriniz noktasını giriniz = "))
    if c>0 and f>0 : 
        break 
    else: 
        print("lütfen 0 dan büyük sayılar giriniz") 
        continue



x = np.random.randn(10000)
y = np.random.randn(10000)

plt.hist2d(x, y, bins=50, cmap=binary)
plt.colorbar(label='Frequency')
plt.title(f"2D Histogram with {binary.capitalize()} Colormap")

x=np.linspace(a,b,c)
y=np.linspace(d,e,f)
X, Y = np.meshgrid(x,y)
Z = eval(o)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
fig = plt.figure(figsize=(w, h)) 
surface = ax.plot_surface(X, Y, Z, cmap=binary)
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=5) 
ax.set_xlabel(k)
ax.set_ylabel(l)
ax.set_zlabel(m)

plt.show()



