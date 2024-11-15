import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

z = np.array([0.9*np.exp(1j*0.6*np.pi), 0.9*np.exp(-1j*0.6*np.pi),
              1.25*np.exp(1j*0.8*np.pi), 1.25*np.exp(-1j*0.8*np.pi)])

p = [0, 0, 0, 0]
k = 1

b, a = signal.zpk2tf(z, p, k)

Omega, X = signal.freqz_zpk(z, p, k, whole=True)
magnitude = np.abs(X)
magnitude_db = 20*np.log10(magnitude)
phase = np.angle(X)
w, gd = signal.group_delay((b, a), whole=True)

plt.figure(figsize=(15,10))
plt.subplot(3,1,1)
plt.plot(Omega, magnitude_db)
plt.grid()
plt.title("Magnitude & Phase Response & Groud delay")
plt.ylabel("Magnitude[dB] of X(z)")

plt.subplot(3,1,2)
plt.plot(Omega, phase)
plt.grid()
plt.ylabel("Phase of X(z)")

plt.subplot(3,1,3)
plt.plot(w, gd)
plt.grid()
plt.ylabel("Groud delay of X(z)")
plt.xlabel("Radian Frequency(w)")

plt.show()