import numpy as np
import matplotlib.pyplot as plt

start = -3
end = 3

n = np.arange(start, end+1)
x = np.where(n==0, 1, 0)
h = np.array([2, 3, 4, -7, -2, 2, -4])

ny = np.arange(-6, 7)
y = np.convolve(x, h)

print(y)

plt.figure(figsize=(10, 10))
plt.grid()
plt.stem(ny, y)
plt.show()