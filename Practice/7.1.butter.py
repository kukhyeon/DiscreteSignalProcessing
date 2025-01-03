import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib import patches, rcParams

np.set_printoptions(precision=3, suppress=True)

wp = 0.2 * np.pi
ws = 0.3 * np.pi
Rp = 7
As = 16

N, wc = signal.buttord(wp, ws, Rp, As, analog=True)
b, a = signal. butter(N, wc, 'lowpass', analog=True)
z,p,k = signal.butter(N, wc, 'lowpass', analog=True, output='zpk')


plt.figure(figsize=(6,6))
plt.axvline(0, color='k', lw=1)
plt.axhline(0, color='k', lw=1)
plt.scatter(np.real(p), np.imag(p), s=50, marker='x', label='Poles')
plt.scatter(np.real(z), np.imag(z), s=50, marker='o', label='Zeros')
plt.grid('equal') ### 까먹지 말 것
plt.legend()
plt.show()

b, a = signal.butter(N, wc/np.pi, 'lowpass', analog=True)
w, H = signal.freqs(b, a) ### 까먹지 말 것 

plt.plot(w, np.abs(H))
plt.show()