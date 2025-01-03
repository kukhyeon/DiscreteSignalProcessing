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
    y[n] = input[n] - 16.0625 * input[n-2] + input[n-4]
    
FIR_direct_output = y.copy()

plt.figure(figsize=(15, 10))

plt.subplot(2,1,1)
plt.plot(x, "m")
plt.xlim(0, 5000)
plt.ylabel("Amplitude")
plt.title("Chirp signal")

plt.subplot(2,1,2)
plt.plot(FIR_direct_output, "b")
plt.xlim(0, 5000)
plt.xlabel("samples, frequency[0-5000Hz]")
plt.ylabel("Amplitude")
plt.grid()
plt.title("Frequency filtering result of FIR direct filter")

plt.show()