import numpy as np
import matplotlib.pyplot as plt

n1_start = 0
n1_end = 15
n2_start = -5
n2_end = 7

n1 = np.arange(n1_start, n1_end+1)
x1 = np.array([0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1])
n2 = np.arange(n2_start, n2_end+1)
x2 = np.array([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1])

n = np.arange(min(min(n1), min(n2)), max(max(n1), max(n2))+1)

x1_exn = np.zeros(len(n))
x2_exn = np.zeros(len(n))

shift = abs(min(min(n1), min(n2)))
n1 = n1 + shift
n2 = n2 + shift

x1_exn[int(min(n1)): int(max(n1)+1)] = x1
x2_exn[int(min(n2)): int(max(n2)+1)] = x2

x = x1_exn + x2_exn

plt.figure(figsize=(10, 5))
plt.stem(n, x)
plt.grid()
plt.show()