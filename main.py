import hullAlgo
import plotWil
import random
import time


#Inisiasi
hull =  hullAlgo.convexHull()
plotting = plotWil.memPlotHull()
#Masukan input
n = int (input("Masukan jumlah titik : "))
lbound = int(input("Masukan batas bawah acak : "))
ubound =  int(input("Masukan batas atas acak : "))
#Proses randomized
print("Titik-Titiknya {x,y} : ")
for i in range(0,n):
    x = random.randint(lbound,ubound)
    y = random.randint(lbound,ubound)
    print((x,y))
    hull.addPoint((x,y))
    plotting.addNotHull((x,y))

#Mulai algonya
msecawal = int(round(time.time() * 1000))
hull.mulaiHull()
msecakhir = int(round(time.time() * 1000))

#hasil hull nya
print("Hasilnya : ")
hasilHull = hull.Hull

#tampilkan hasil hullnya dan waktunya
print(hasilHull)
print(str (msecakhir-msecawal) + " millisecond")

#hasil plotting
for i in range(0,len(hasilHull)):
    plotting.addPairHull(hasilHull[i])
plotting.showHull()