import numpy as np
import matplotlib.pyplot as plt

n1_start = 0
n1_end = 15
n2_start = -5
n2_end = 7

n1 = np.arange(n1_start, n1_end+1)
x1 = np.array([0,0,0,1,2,3,4,5,6,7,6,5,4,3,2,1])
n2 = np.arange(n2_start, n2_end+1)
x2 = np.array([1,2,3,4,5,6,7,6,5,4,3,2,1])

n_start = n1[0] + n2[0]
n_end = n1[-1] + n2[-1]
n = np.arange(n_start, n_end+1)

print(f"n1: {n1}")
print(f"n2: {n2}")
print(f"n: {n}")

x = np.convolve(x1, x2)

plt.figure(figsize = (10, 10))

plt.subplot(3, 1, 1)
plt.stem(n1, x1, basefmt="blue")
plt.grid()
plt.ylabel("x1[n]")

plt.subplot(3, 1, 2)
plt.stem(n2, n2, basefmt="blue")
plt.grid()
plt.ylabel("x2[n]")

plt.subplot(3, 1, 3)
plt.stem(n, x, basefmt="blue")
plt.grid()
plt.xlabel("n")
plt.ylabel("x1[n]")

plt.show()