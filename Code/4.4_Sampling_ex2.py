import numpy as np
import matplotlib.pyplot as plt

def DTFT(xk, k, T = 1000):
    omega = np.linspace(-np.pi, np.pi, T)
    X = np.zeros(T, dtype="complex64")
    for idx, val in enumerate(k):
        X += xk[idx] * np.exp(-1j * omega * val)
    return X, omega

start_t = -5
end_t = 5
Ts = 0.1
N = int(np.abs(end_t-start_t)/Ts)

t = np.linspace(start_t, end_t, N)
xc = np.exp(-np.abs(t))
n = np.arange(start_t/Ts, end_t/Ts)

X, w = DTFT(xc, n, N)
X = np.real(X)

plt.figure(figsize=(15, 10))

plt.subplot(2, 1, 1)
plt.stem(n, xc)
plt.grid()
plt.xticks(np.arange(start_t/Ts, end_t/Ts+1, 10))
plt.xlabel("n")
plt.ylabel("x[n]")

plt.subplot(2, 1, 2)
plt.plot(w/np.pi, X)
plt.grid()
plt.xticks(np.arange(-1, 1.2, 0.2))
plt.xlabel("Frequency in pi units")
plt.ylabel("X(w)")

plt.show()