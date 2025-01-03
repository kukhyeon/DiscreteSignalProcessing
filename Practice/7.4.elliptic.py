import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches, rcParams
from scipy import signal

np.set_printoptions(precision=3, suppress=True)

wp = 0.2*np.pi
ws = 0.3*np.pi
Rp = 1
As = 16

# 차수하고 차단주파수로 계수 구한 후, zpk도 구할 수 있음.
N, wc = signal.ellipord(wp, ws, Rp, As, analog=True)
b, a = signal.ellip(N, Rp, As, wc, 'lowpass', analog=True)
z, p, k = signal.ellip(N, Rp, As, wc, 'lowpass', analog=True, output='zpk')

plt.figure(figsize=(6,6))
plt.axvline(0, color='k', lw=1)
plt.axhline(0, color='k', lw=1)
plt.scatter(np.real(p), np.imag(p), s=50, marker='x', label='Poles')
plt.scatter(np.real(z), np.imag(z), s=50, marker='o', label='Zeros')
plt.grid('equal')
plt.legend()
plt.show()

b, a = signal.ellip(N, Rp, As, wc/np.pi, 'lowpass', analog=True)
w, H = signal.freqs(b, a)

plt.figure(figsize=(6,6))
plt.plot(w, np.abs(H))
plt.xlim(0,1)
plt.grid()
plt.show()