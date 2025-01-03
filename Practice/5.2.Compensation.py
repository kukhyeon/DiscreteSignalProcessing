import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

zero1 = 0.9*np.exp(1j*0.6*np.pi)
zero2 = 1.25*np.exp(1j*0.8*np.pi)
z = np.array([0.9*np.exp(1j*0.6*np.pi), 0.9*np.exp(-1j*0.6*np.pi), 0.8*np.exp(1j*0.8*np.pi), 0.8*np.exp(-1j*0.8*np.pi)])
p = np.array([0,0,0,0])
k = (1.25)**2 # 헷갈리는 부분
b, a = signal.zpk2tf(z, p, k) # z, p, k를 통해 계수 변환환

Omega, X = signal.freqz_zpk(z, p, k, whole=True)
mag_dB = 20*np.log10(np.abs(X))
phase = np.angle(X)
w, gd = signal.group_delay((b, a), whole=True)
# Plotting
plt.figure(figsize=(15, 10))

# Magnitude Response
plt.subplot(3, 1, 1)
plt.plot(Omega, mag_dB)
plt.grid()
plt.title("Magnitude Response [dB]")
plt.ylabel("Magnitude [dB]")

# Phase Response
plt.subplot(3, 1, 2)
plt.plot(Omega, phase)
plt.grid()
plt.title("Phase Response")
plt.ylabel("Phase [radians]")

# Group Delay
plt.subplot(3, 1, 3)
plt.plot(w, gd)
plt.grid()
plt.title("Group Delay")
plt.xlabel("Normalized Frequency (x π rad/sample)")
plt.ylabel("Group Delay")

plt.show()