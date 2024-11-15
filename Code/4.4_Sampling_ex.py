import numpy as np
import matplotlib.pyplot as plt

start_t = -5
end_t = 5
Ts = 0.1
N = int(np.abs(end_t-start_t)/Ts)

tp = np.arange(0, 5, 0.1)
tn = np.arange(-5, 0, 0.1)

t = np.zeros(N)
t[:50] = tn
t[50:] = tp

xc = np.exp(-np.abs(t))
n = np.arange(start_t/Ts, end_t/Ts)

plt.figure(figsize=(15, 10))

plt.plot(t, xc)
markers, _, _ = plt.stem(t, xc)
plt.setp(markers, marker='^')

plt.xticks(range(-5, 6))
plt.xlabel("t in sec.")
plt.ylabel("xc(t)")
plt.grid()
plt.show()