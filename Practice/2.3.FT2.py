import numpy as np
import matplotlib.pyplot as plt

def DTFT(xn, T = 1000):
    X = np.fft.fftshift(np.fft.fft(xn, n=T))
    omega = np.linspace(-np.pi, np.pi, T)
    return X, omega

n = np.arange(30)
xn = np.power(0.5, n)

X, omega = DTFT(xn)
mag_X = np.abs(X)
phase_X = np.angle(X, deg="True")

plt.figure(figsize=(15,10))
plt.subplot(3, 1, 1)
plt.stem(n, xn)
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(omega, mag_X)
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(omega, phase_X)
plt.grid()
plt.show()