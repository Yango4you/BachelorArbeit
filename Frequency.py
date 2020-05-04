import csv
import math
import cmath
from matplotlib import pyplot as plt
import numpy as np


feq = []
mag = []

with open("trace_0_1.csv",'r', encoding='utf-8') as f:

    reader = csv.reader(f)
    header = next(reader)
    #header = str(next(reader)).split(";")

    tabelle = []

    for zeile in reader:
        str1 = ''.join(zeile)
        spalten = str1.split(";")
        tabelle.append(spalten)


    for i in tabelle:
        feq.append(float(i[0]))
        mag.append(float(i[1]))

x = feq
y = mag


def fft_funktion(a, b):
    N = int(len(b)/2+1)
    dt = a[1]-a[0]
    fa = 1/dt
    X = np.linspace(0, fa/2, N, endpoint=True)
    hann = np.hanning(len(b))
    Yhann = np.fft.fft(hann * b)
    Y = 20*np.log10(2.0*np.abs(Yhann[:N])/N)
    return X, Y

fft=fft_funktion(x,y)
print("Y",type(fft[0]))
#print("X",fft[1])
#print(fft[0][403:754])
idx = np.where((fft[0]>1.5)&(fft[0]<2.795))
#print("index11",idx)
idx = idx[0][:]
#for i in len(fft[0])
print("index", idx)
print("index", len(idx))
print(np.average(fft[1][idx[0]:idx[-1]]))

def tcorr(t):
    sin = []
    for i in range(0,4):
        k = np.random.uniform(0.00000041, 0.01)
        print("Koeffizienten:", k)
        f = np.random.uniform(1.5, 3)
        print("zufaellige Frequenz:", f)
        phi = np.random.uniform(0, 2*np.pi)
        sin.append(k*np.sin(2*np.pi*f*t+phi))
    print("sin",sin)

    cos = []
    for i in range(0, 4):
        k = np.random.uniform(0.00000041, 0.01)
        print("Koeffizienten:", k)
        f = np.random.uniform(1.5, 3)
        print("zufaellige Frequenz:", f)
        phi = np.random.uniform(0, 2 * np.pi)
        sin.append(k * np.cos(2 * np.pi * f * t + phi))
    print("cos", cos)
    return

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
# plt.plot()
# plt.plot(fft[0], fft[1])
# plt.title('Test 1')
# plt.xlabel('f THz')
# plt.ylabel('Mag. dBv')
# plt.grid()

#
# #plt.subplot(222)
# plt.plot(fft[2], fft[0])
# plt.title('Test 2')
# plt.xlabel('f THz')
# plt.ylabel('Mag. dBv')
# plt.grid()

# plt.subplot(223)
# plt.plot(x, y)
# plt.title('Test 3')
# plt.xlabel('f THz')
# plt.ylabel('Mag. dBv')
# plt.grid()
#
# plt.subplot(224)
# plt.plot(x, y)
# plt.title('Test 4')
# plt.xlabel('f THz')
# plt.ylabel('Mag. dBv')
# plt.grid()
plt.show()
