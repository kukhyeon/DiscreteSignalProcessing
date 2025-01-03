import numpy as np
from scipy.signal import chirp
import matplotlib.pyplot as plt

tn = 5000
t = np.linspace(0, 1, tn)
x = chirp(t, f0=10, t1=0.2, f1=500, method='linear')

input = [0] * tn
v = [0] * tn
y = [0] * tn

for n in range(0, len(x)):
    input[n] = x[n]
    v[n] = input[n] - 3*input[n-1] + 2*input[n-2] + 0.25*v[n-1] + 0.125*v[n-2]
    y[n] = 1/16*v[n] + 9/16*v[n-2] - y[n-1] - 0.5*y[n-2]
    
output = y.copy()

plt.figure(figsize=(10,10))
plt.subplot(2,1,1)
plt.plot(x, 'm')
plt.grid()
plt.xlim(0,5000)
plt.subplot(2,1,2)
plt.plot(output, "b")
plt.grid()
plt.xlim(0,5000)
plt.show()