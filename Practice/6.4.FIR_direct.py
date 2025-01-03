import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

tn = 5000
t = np.linspace(0, 1, tn)
x = chirp(t, f0=10, t1=0.2, f1=500, method='linear')

input = [0] * tn
y = [0] * tn

for n in range(0, len(x)):
    input[n] = x[n]
    y[n] = input[n] - 16.0625*input[n-2] + input[n-4]

result = y.copy()

plt.figure(figsize=(15,10))
plt.subplot(2,1,1)
plt.grid()
plt.xlim(0, 5000)
plt.plot(x, "m")

plt.subplot(2,1,2)
plt.grid()
plt.xlim(0,5000)
plt.plot(result, "b")

plt.show()