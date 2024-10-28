import numpy as np
import matplotlib.pyplot as plt

n1_start = 0
n1_end = 7
n2_start = -8
n2_end = 2

n1 = np.arange(n1_start, n1_end + 1)
x1 = 3 * np.round(np.cos(np.pi/2 * n1),2)


n2 = np.arange(n2_start, n2_end + 1)
x2 = 3 * np.round(np.cos(np.pi/2 * n2),2)

n = np.arange(min(min(n1), min(n2)), max(max(n1), max(n2))+1)

x1_end = np.zeros(len(n))
x2_end = np.zeros(len(n))

shift = abs(min(min(n1), min(n2)))

n1_shifted = n1 + shift
n2_shifted = n2 + shift

# 해당 범위에 x1과 x2 값을 대입
x1_end[min(n1_shifted):max(n1_shifted) + 1] = x1
x2_end[min(n2_shifted):max(n2_shifted) + 1] = x2

x = x1_end * x2_end
print(x)

# 그래프 출력
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