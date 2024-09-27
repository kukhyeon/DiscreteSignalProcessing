import numpy as np
import matplotlib.pyplot as plt

start = -3
end = 3

n = np.arange(start, end+1)

x = np.where(n==0, 1, 0)
h = np.array([2, 3, 4, -7, -2, 2, -4])

ny = np.arange(-6, 7)
y = np.convolve(x, h)

plt.figure(figsize=(10, 10))
plt.subplot(3, 1, 1)
plt.stem(n, x, basefmt="blue")
plt.grid()
plt.ylabel("x[n]")

plt.subplot(3, 1, 2)
plt.stem(n, h, basefmt="blue")
plt.grid()
plt.ylabel("h[n]")

plt.subplot(3, 1, 3)
plt.stem(ny, y, basefmt="blue")
plt.grid()
plt.xlabel("n")
plt.ylabel("y[n]")

plt.show()