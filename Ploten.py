from matplotlib import pyplot as plt


plt.subplot(221)
plt.plot(x, y)
plt.title("Originale Messdaten")
plt.xlabel("t ps")
plt.ylabel("I nA")
plt.grid()

plt.subplot(222)
plt.plot(xNew[0], xNew[1])
plt.title("korrigierte Messdaten")
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