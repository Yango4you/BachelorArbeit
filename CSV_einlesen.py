import csv


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
