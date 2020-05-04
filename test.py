import numpy as np
import GA
from scipy.signal import find_peaks, peak_prominences
import CSV_einlesen
from matplotlib import pyplot as plt

x= CSV_einlesen.x
y= CSV_einlesen.y

fft= GA.fftFunction(x, y)
index = np.where((fft[0] > 1.7) & (fft[0] < 2.5))
#print("indexx", index)
index = index[0][:]
#print("index ",index)
signal = fft[1][index[0:-1]]
peak, _ = find_peaks(signal, prominence=(9, None))

print("peaks ", signal[peak])
print("peaks-max ", np.amax(signal[peak]))

prominences = peak_prominences(signal, peak)[0]
print("pro", prominences)
#print("max,", np.maximum(prominences))

contour_heights = signal[peak] - prominences

#plt.plot(fft[0][index[0:-1]], fft[1][index[0:-1]])
plt.plot(peak, signal[peak], 'x')
plt.plot(signal)
plt.vlines(x=peak, ymin=contour_heights, ymax=signal[peak])
plt.show()


# sinFunction_num = 8
# koeffizienten_num_per_sinFunction = 3
#
# sol_per_pop = 3
# num_parents_mating = 4
#
#
# pop_size = (sol_per_pop, sinFunction_num, koeffizienten_num_per_sinFunction)
# new_population = np.empty(pop_size)
# print("hallo",pop_size[1], pop_size[2])
# for i in range(sol_per_pop):
#     for j in range(sinFunction_num):
#         new_population[i][j] = GA.koeffizientenGenertieren(sinFunction_num)[j]
# print("pop", new_population[0,3:5])
#
# print("off",GA.mutation(new_population)[0][3:5])
#
# a = [2,2,3]
# b=[30,50,70]
# print(GA.averageFunction(a,b))
