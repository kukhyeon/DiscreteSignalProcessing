import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

theta = np.pi
b = np.array([1, -0.9*np.exp(1j*theta)])
a = np.array([1, 0])

Omega, X = signal.freqz(b, a, whole=True)
magnitude_db = 20*np.log10(np.abs(X))
phase = np.angle(X)

w, gd = signal.group_delay((b, a), whole=True)
# Magnitude (dB)
plt.figure(figsize=(15,10))
plt.subplot(3,1,1)
plt.plot(Omega, magnitude_db)
plt.grid()
plt.title("Magnitude & Phase Response & Group delay")
plt.ylabel("Magnitude[dB] of X(z)")

# Phase
plt.subplot(3,1,2)
plt.plot(Omega, phase)
plt.grid()
plt.ylabel("Phase of X(z)")

# Group Delay
plt.subplot(3,1,3)
plt.plot(w, gd)
plt.grid()
plt.xlabel("Radian Frequency (w)")
plt.ylabel("Group delay of X(z)")

plt.tight_layout()
plt.show()
