import numpy as np
import matplotlib.pyplot as plt

start_t = -5
end_t = 5
Ts = 0.1
fs = 1 / Ts
N = int(np.abs(end_t - start_t) / Ts)

tp = np.arange(0, 5, Ts)
tn = np.arange(-5, 0, Ts)

t = np.zeros(N)
t[:int(N / 2)] = tn
t[int(N / 2):] = tp

xc = np.exp(-np.abs(t))

delta_t = 0.0005
recon_t = np.arange(start_t, end_t, delta_t)
Nt = len(recon_t)

sinc_out = np.zeros(Nt)

for i in range(Nt):
    sum = 0
    for j in range(N):
        sum += xc[j] * np.sinc((recon_t[i] - t[j]) / Ts)
    sinc_out[i] = sum
