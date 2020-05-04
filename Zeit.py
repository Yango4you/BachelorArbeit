import csv
from pylab import *
import numpy as np
import random

from scipy.interpolate import interp1d
import time

localtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

zeit = []
strom = []

with open("trace_0_1.csv",'r', encoding='utf-8') as f:

    reader = csv.reader(f)
    #header = next(reader)
    #header = str(next(reader)).split(";")

    tabelle = []

    for zeile in reader:
        str1 = ''.join(zeile)
        spalten = str1.split(";")
        tabelle.append(spalten)


    for i in tabelle:
        zeit.append(float(i[0]))
        strom.append(complex(i[1]))

x = zeit
y = strom


# fft-funktion
Y = np.fft.fft(y)
N = int(len(Y)/2+1)
dt = x[1]-x[0]
fa = 1.0/dt
X = np.linspace(0,fa/2,N,endpoint=True)


#tcorr
k = [0]*12
for i in range(len(k)):
    k[i] = random.uniform(0.00000041, 0.01)
print("Koeffizienten:", k)

zufallF =[0]*3
for i in range(len(zufallF)):
    zufallF[i] = random.uniform(1.6, 2.8)
print("zufaellige Frequenz:", zufallF)
tneu = [0]*len(x)
for i in range(len(x)):
    tneu[i] =k[0]*np.sin(2*np.pi*(zufallF[0]+k[1])*x[i])+k[2]*np.cos(2*np.pi*(zufallF[0]+k[3])*x[i])+ k[4]*np.sin(2*np.pi*(zufallF[1]+k[5])*x[i])+k[6]*np.cos(2*np.pi*(zufallF[1]+k[7])*x[i])+k[8]*np.sin(2*np.pi*(zufallF[2]+k[9])*x[i])+k[10]*np.cos(2*np.pi*(zufallF[2]+k[11])*x[i])
print("tneu",tneu)

tcorr = [0]*len(x)
for i in range(len(x)):
    tcorr[i] = tneu[i] + x[i]
print("tcorr",tcorr)


# fft-funktion von tcorr
tLinear = np.linspace(tcorr[0],tcorr[-1],len(tcorr),endpoint=True)
#print("tLinear,",tLinear)
f = interp1d(tcorr, y, kind = 'cubic')
yneu = f(tLinear)
print("yneu,",yneu)

Yneu = np.fft.fft(yneu)
Nneu = int(len(Yneu)/2+1)
dtneu = tLinear[1]-tLinear[0]
faneu = 1.0/dtneu
Xneu = np.linspace(0,faneu/2,Nneu,endpoint=True)


#Hanning window
hann = np.hanning(len(y))
Yhann = np.fft.fft(hann*y)

hannCorr = np.hanning(len(yneu))
YhannCorr = np.fft.fft(hannCorr*yneu)


#plotten
plt.subplot(221)
plt.plot(x,y)
plt.title("Original Messdaten")
plt.xlabel("t ps")
plt.ylabel("I nA")
plt.grid()

plt.subplot(223)
plt.plot(X,20*np.log10(2.0*np.abs(Yhann[:N])/N))
plt.xlabel ("f THz")
plt.ylabel("Mag. in dB")
plt.grid()

plt.subplot(222)
plt.plot(tLinear,yneu)
plt.title("Korrigierte Messdaten")
plt.xlabel("tcorr ps")
plt.ylabel("I nA")
plt.grid()

plt.subplot(224)
plt.plot(Xneu,20*np.log10(2.0*np.abs(YhannCorr[:N])/N))
plt.xlabel ("fcorr THz")
plt.ylabel("Mag. in dB")
plt.grid()
plt.text(11.5,-310,localtime,rotation=0,wrap=False)
plt.tight_layout()
plt.show()

with open('test.csv','a',encoding='utf-8') as f:
    f.write(localtime + "\n")
    f.write("K: ")
    for i in range(len(k)):
        f.write(str(k[i])+"//")
    f.write("\n")
    f.write("zufaellige Frequenz: ")
    for i in range(len(zufallF)):
        f.write(str(zufallF[i])+"//")
    f.write("\n")
    f.write(("################################"+"\n"))
f.close()
#plt.plot(np.abs(y[:N]))
#plt.ylabel('I mA')
#plt.grid()
