import numpy as np
import matplotlib.pyplot as plt

def DTFT(xn, T=1000):
    X = np.fft.fftshift(np.fft.fft(xn, n=T))
    omega = np.linspace(-np.pi, np.pi, T)
    return X, omega

start_t = -5
end_t = 5
Ts = 0.1

# sampling freq N
N = int(np.abs(end_t - start_t)/Ts)
# sampling해줌
t = np.linspace(start_t, end_t, N)
xc = np.exp(-np.abs(t))
n = np.arange(start_t/Ts, end_t/Ts)

plt.figure(figsize=(15,10))
plt.plot(t, xc)
markers, _, _ = plt.stem(t, xc)
plt.setp(markers, marker='^')
plt.xticks(range(-5, 6))
plt.grid()
plt.show()

