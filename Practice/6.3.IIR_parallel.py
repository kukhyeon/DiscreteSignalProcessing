import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

tn = 5000
t = np.linspace(0, 1, tn)
x = chirp(t, f0=10, t1=0.2, f1=500, method='linear')

input = [0] * tn
v1 = [0] * tn
v2 = [0] * tn
y = [0] * tn

for n in range(0,len(x)):
    input[n] = x[n]
    v1[n] = 28.1125*input[n] - 13.3625*input[n-1] + 0.25*v1[n-1] + 0.125*v1[n-2]
    v2[n] = -10.05*input[n] - 3.95*input[n-1] - v2[n-1] - 0.5*v2[n-2]
    y[n] = -18*input[n] + v2[n] + v1[n]
    
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