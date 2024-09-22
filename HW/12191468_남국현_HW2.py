import numpy as np
import matplotlib.pyplot as plt

n1_start = 0
n1_end = 7
n2_start = -8
n2_end = 2


# n1 = (0 ~ 7)
n1 = np.arange(n1_start, n1_end + 1)
x1 = 3 * np.cos(np.pi/2 * n1)

# n2 = (-8 ~ 2)
n2 = np.arange(n2_start, n2_end + 1)
x2 = 3 * np.sin(np.pi/2 * n2)

# n = [-8 ~ 7]
n = np.arange(min(min(n1), min(n2)), max(max(n1), max(n2)) + 1)

# x1_end, x2_end에 0으로 초기화된 배열 생성
x1_end = np.zeros(len(n))
x2_end = np.zeros(len(n))

# shift = 8 (최소값을 기준으로 이동)
shift = abs(min(min(n1), min(n2)))

# n1과 n2를 shift 시킴
n1_shifted = n1 + shift
n2_shifted = n2 + shift

# 해당 범위에 x1과 x2 값을 대입
x1_end[min(n1_shifted):max(n1_shifted) + 1] = x1
x2_end[min(n2_shifted):max(n2_shifted) + 1] = x2

x = x1_end * x2_end

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