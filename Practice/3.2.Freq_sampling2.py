import numpy as np
import matplotlib.pyplot as plt

def DTFT(xn, n, T):
    omega = np.linspace(-np.pi, np.pi, T)
    X = np.zeros(T, dtype="complex64")
    for idx, val in enumerate(omega):
        X[idx] = np.sum(xn * np.exp(-1j*val*n))
    return X, omega

start_t = -5
end_t = 5
Ts = 0.1
N = int(np.abs(end_t-start_t)/Ts)
t = np.linspace(start_t, end_t, N)
xc = np.exp(-np.abs(t))
n = np.arange(start_t/Ts, end_t/Ts+1)

X, w = DTFT(xc,n, N)
X = np.real(X)

plt.figure(figsize=(15,15))
plt.subplot(2,1,1)
plt.stem(n, xc)
plt.grid()
plt.xticks(np.arange(start_t/Ts, end_t/Ts+1, 10))

plt.subplot(2,1,2)
plt.plot(w/np.pi, X)
plt.grid()
plt.xticks(np.arange(-1, 1.2, 0.2))
plt.show()