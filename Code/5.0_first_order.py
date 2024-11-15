import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

theta = np.pi
b = np.array([1, -0.9*np.exp(1j*theta)]) 
a = np.array([1, 0])

Omega, X = signal.freqz(b, a, whole=True)
magnitude = np.abs(X)
magnitude_db = 20*np.log10(magnitude)
phase = np.angle(X)
w, gd = signal.group_delay((b, a), whole=True)

plt.figure(figsize=(15,10))
plt.subplot(3,1,1)
plt.plot(Omega, magnitude_db)
plt.grid()
plt.title("Magnitude & Phase Response & Group delay")
plt.ylabel("Magnitude[dB] of X(z)")

plt.subplot(3,1,2)
plt.plot(Omega, phase)
plt.grid()
plt.ylabel("Phase of X(z)")

plt.subplot(3,1,3)
plt.plot(w, gd)
plt.grid()
plt.ylabel("Groud delay of X(z)")
plt.xlabel("Randian Frequency(w)")

plt.show()