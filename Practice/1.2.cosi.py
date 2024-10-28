import numpy as np
import matplotlib.pyplot as plt

start = 0
end = 10

n = np.linspace(0, 12, 64)
amp = 3
omega = (3*np.pi)/8
phase = np.pi/2
xn = amp * np.cos(omega*n + phase)

plt.figure(figsize=(10,5))
plt.stem(n, xn)
plt.grid()
plt.show()