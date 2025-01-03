import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

tn = 5000
t = np.linspace(0, 1, tn)
x = chirp(t, f0=10, t1=0.2, f1=500, method='linear')

input = [0] * tn
v = [0] * tn
y = [0] *tn
v2 = [0] * tn

for n in range(0, len(x)):
    input[n] = x[n]
    v[n] = input[n] - 4*input[n-1] - input[n-2] - 0.5*v[n-1] - v[n-2]
    v2[n] = v[n] + 3*v[n-1] -2*v[n-2] + 0.125*v2[n-1] + 0.25*v2[n-2]
    y[n] = 1/16*v2[n]

output = y.copy()

# Plot results
plt.figure(figsize=(15, 10))

# Plot Chirp Signal
plt.subplot(2, 1, 1)
plt.plot(x, "m")
plt.xlim(0, 5000)
plt.grid()
plt.ylabel("Amplitude")
plt.title("Chirp signal")

# Plot Filtered Signal
plt.subplot(2, 1, 2)
plt.plot(output, "b")
plt.xlim(0, 5000)
plt.grid()
plt.xlabel("Samples, frequency [0-5000 Hz]")
plt.ylabel("Amplitude")
plt.title("Frequency filtering result of IIR direct-1 filter")

plt.show()