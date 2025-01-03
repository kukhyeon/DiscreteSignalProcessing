import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches, rcParams
from scipy import signal

np.set_printoptions(precision=3, suppress=True)

wp = 0.2*np.pi
ws = 0.3*np.pi
Rp = 1
As = 16

N, wc = signal.cheb1ord(wp, ws, Rp, As, analog=True)
b, a = signal.cheby1(N, Rp, wc, 'lowpass', analog=True)
z,p,k = signal.cheby1(N, Rp, wc, 'lowpass', analog=True, output='zpk')

plt.figure(figsize=(6,6))
plt.axvline(0, color='blue', lw=1)
plt.axhline(0, color='blue', lw=1)
plt.scatter(np.real(p), np.imag(p), s=50, marker='x', label='Poles')
plt.scatter(np.real(z), np.imag(z), s=50, marker='o', label='Zeros')
plt.grid('equal')
plt.legend
plt.show()

b, a = signal.cheby1(N, Rp, wc/np.pi, 'lowpass', analog=True)
w, H = signal.freqs(b, a)  # 아날로그 신호 변환
plt.figure(figsize=(6,6))
plt.plot(w, np.abs(H))
plt.show()