import csv
from matplotlib import pyplot as plt

feq = []
mag = []

with open("fft_49.csv",'r', encoding='utf-8') as f:

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
plt.plot()
plt.plot(x, y)
plt.title('Test 1')
plt.xlabel('f THz')
plt.ylabel('Mag. dBv')
plt.grid()
plt.show()