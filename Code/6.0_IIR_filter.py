import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

tn = 5000
t = np.linspace(0, 1, tn)
x = chirp(t, f0=10, t1=0.2, f1=500, method='linear')

input = [0] * tn
v = [0] * tn
y = [0] * tn

for n in range(0, len(x)):
    input[n] = x[n]
    v[n] = 1/16 * input[n] - 3/16*input[n-1] + 11/16 * input[n-2] - 27/16 * input[n-3] + 18/16 * input[n-4]
    y[n] = v[n] - 12/16 * y[n-1] - 2/16 * y[n-2] + 4/16 * y[n-3] + 1/16 * y[n-4]
    
IIR_direct_1_output = y.copy()

plt.figure(figsize=(15, 10))

plt.subplot(2,1,1)
plt.plot(x, "m"); plt.xlim(0,5000)
plt.ylabel("Amplitude"); plt.title("Chirp signal")

plt.subplot(2,1,2)
plt.plot(IIR_direct_1_output, "b"); plt.xlim(0, 5000)
plt.xlabel("samples, frequence(0-5000Hz)"); plt.ylabel("Amplitude"); plt.grid()
plt.title("Frequency filtering result of IIR direct-1 filter")

plt.show()