import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches, rcParams
from scipy import signal

b = np.array([1,0])
a = np.array([1,-0.5])

Omega, X = signal.freqz(b, a)
magnitude = np.abs(X)
phase = np.angle(X, deg = True)

plt.figure(figsize = (15, 10))
plt.subplot(2, 1, 1)
plt.plot(Omega, magnitude)
plt.grid()
plt.ylabel("Magnitude of X(z)")
plt.title("Magnitude & Phase Response")

plt.subplot(2, 1, 2)
plt.plot(Omega, phase)
plt.grid()
plt.ylabel("Phase of X(z)")
plt.xlabel("Frequency in radian")

plt.show()