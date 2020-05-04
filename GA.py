import numpy as np
from scipy.interpolate import interp1d
from matplotlib import pyplot as plt
from scipy.signal import find_peaks, peak_prominences


def koeffizientenGenertieren(numSinfunction):
    k = [0]*numSinfunction
    for i in range(numSinfunction):
        amp = np.random.uniform(0.0066, 0.01)
        f = np.random.uniform(1.9, 2.5)
        phi = np.random.uniform(0, 2 * np.pi)
        k[i] = [amp, f, phi]
    return k


def tcorrFunction(t, y, k, numSinfunction):
    tNeu = np.empty((numSinfunction,len(t)))
    for i in range(numSinfunction):
        for j in range(len(t)):
            if i%2 == 0:
                function = k[i][0]*np.sin(2*np.pi*k[i][1]*t[j]+k[i][2])
            else:
                function = k[i][0]*np.cos(2*np.pi*k[i][1]*t[j]+k[i][2])
            tNeu[i][j] = function
    tcorr = t+tNeu.sum(axis=0)
    tLinear = np.linspace(tcorr[0], tcorr[-1], len(tcorr), endpoint=True)
    f = interp1d(tcorr, y, kind='cubic')
    yneu = f(tLinear)
    return tcorr, yneu


def fftFunction(t, y):
    N = int(len(y)/2+1)
    dt = t[1]-t[0]
    fa = 1/dt
    X = np.linspace(0, fa/2, N, endpoint=True)
    hann = np.hanning(len(y))
    Yhann = np.fft.fft(hann* y)
    Y = 20*np.log10(2.0*np.abs(Yhann[:N])/N)
    return X, Y


def averageFunction(x, y):
    index = np.where((x > 1.7) & (x < 2.5))
    index = index[0][:]
    avg = np.average(y[index[0]:index[-1]])
    return avg


def peaksFunction(x, y):
    index = np.where((x > 1.9) & (x < 2.5))
    index = index[0][:]
    signal = y[index[0:-1]]
    peak, _ = find_peaks(signal, prominence=(5, None))
    prominences = peak_prominences(signal, peak)[0]
    # contour_heights = signal[peak] - prominences
    a = np.amax(prominences)
    return a


def cal_pop_fitness(t, y, pop):
    fitness = [0]* pop.shape[0]
    for i in range(pop.shape[0]):
        tNeu = tcorrFunction(t, y, pop[i], pop.shape[1])
        fftNeu = fftFunction(tNeu[0],tNeu[1])
        fitness[i] = peaksFunction(fftNeu[0], fftNeu[1])
    return fitness


def select_mating_pool(pop, fitness, num_parents):
    parents = np.empty((num_parents,pop.shape[1],pop.shape[2]))
    for i in range(num_parents):
        min_fitness_idx = np.where(fitness == np.min(fitness))
        min_fitness_idx = min_fitness_idx[0][0]
        parents[i] = pop[min_fitness_idx]
        fitness[min_fitness_idx] = 999999999
    return parents


def crossover(parents, offspring_size):
    offspring = np.empty(offspring_size)
    crossover_point = np.uint8(offspring_size[1]/2)

    for k in range(offspring_size[0]):
        parent1_idx = k%parents.shape[0]
        parent2_idx = (k+1)%parents.shape[0]
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring


def mutation(offspring_crossover):
    for i in range(offspring_crossover.shape[0]):
        random_value = np.random.uniform(0, 0.01, 3)
        offspring_crossover[i, int(offspring_crossover.shape[1]/2)] = offspring_crossover[i, int(offspring_crossover.shape[1]/2)] + random_value
    return offspring_crossover


def ploten(x, y, xNew, yNew, a):
    fft = fftFunction(x, y)
    fftNew = fftFunction(xNew, yNew)
    plt.subplot(221)
    plt.plot(x, y)
    plt.title("Originale Messdaten")
    plt.xlabel("t ps")
    plt.ylabel("I nA")
    plt.grid()

    plt.subplot(222)
    plt.plot(xNew, yNew)
    plt.title("korrigierte Messdaten Gen.%d" % a)
    plt.xlabel("tcorr ps")
    plt.ylabel("I nA")
    plt.grid()

    plt.subplot(223)
    plt.plot(fft[0], fft[1])
    plt.xlabel("f THz")
    plt.ylabel("Mag. in dB")
    plt.grid()

    plt.subplot(224)
    plt.plot(fftNew[0], fftNew[1])
    plt.xlabel("f THz")
    plt.ylabel("Mag. in dB")
    plt.grid()
    plt.tight_layout()
    plt.show()
