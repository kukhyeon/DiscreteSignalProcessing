import numpy as np
import matplotlib.pyplot as plt

def DTFT(xk, k, T = 1000):
    omega = np.linspace(-np.pi, np.pi, T)
    X = np.zeros(T, dtype="complex64")
    for idx, val in enumerate(k):
        X += xk [idx] * np.exp(-1j * omega * val)
    return X, omega

def DTFT_fft(xn, T=1000):
    X = np.fft.fftshift(np.fft.fft(xn, n=T))
    omega = np.linspace(-np.pi, np.pi, T)
    return X, omega

n = np.arange(-2, 2)
xn = np.array([1,2,3,4])

X, omega = DTFT(xn, n)
mag_X = np.abs(X)
phase_X = np.angle(X, deg="True")

X1, omega1 = DTFT_fft(xn)
mag_X2 = np.abs(X)
phase_X2 = np.angle(X, deg="True")

plt.figure(figsize=(15, 10))
plt.subplot(2, 1, 1)
plt.stem(omega, mag_X)
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(omega, mag_X2)
plt.grid()
plt.show()