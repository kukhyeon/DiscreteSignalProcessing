import numpy as np
import matplotlib.pyplot as plt

n1_start = 0
n1_end = 15
n2_start = -5
n2_end = 7

# Set the output range
n1 = np.arange(n1_start, n1_end+1)
x1 = np.array([0,0,0,1,2,3,4,5,6,7,6,5,4,3,2,1])
n2 = np.arange(n2_start, n2_end+1)
x2 = np.array([1,2,3,4,5,6,7,6,5,4,3,2,1])

n = np.arange(min(min(n1), min(n2)), max(max(n1), max(n2))+1)
print(f"n1: {n1}")
print(f"n2: {n2}")
print(f"n: {n}")

# Expand x1 and x2 to fit the range of the output
x1_end = np.zeros(len(n))
x2_end = np.zeros(len(n))

shift = abs(min(min(n1), min(n2)))

n1 = n1 + shift
n2 = n2 + shift

x1_end[int(min(n1)): int(max(n1)+1)] = x1
x2_end[int(min(n2)): int(max(n2)+1)] = x2

plt.figure(figsize = (10, 20))

plt.subplot(2,1,1); plt.stem(n1, x1, basefmt ="blue"); plt.grid()
plt.xlabel("n1"); plt.ylabel("x1[n]")

plt.subplot(2,1,2); plt.stem(n, x1_end, basefmt="blue"); plt.grid()
plt.xlabel("n"); plt.ylabel("x1_end[n]")

plt.show()

# Add two extended sequences & plot

x = x1_end + x2_end

plt.figure(figsize = (10, 10))

plt.subplot(3, 1, 1)
plt.stem(n, x1_end, basefmt="blue")
plt.grid()
plt.ylabel("x1_end[n]")

plt.subplot(3, 1, 2)
plt.stem(n, x2_end, basefmt="blue")
plt.grid()
plt.ylabel("x2_end[n]")

plt.subplot(3, 1, 3)
plt.stem(n, x, basefmt="blue")
plt.grid()
plt.xlabel("n")
plt.ylabel("x[n]")

plt.show()