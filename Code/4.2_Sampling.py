import numpy as np
import matplotlib.pyplot as plt

# 그냥 cos 신호
t = np.linspace(0, 10, 100)
x = np.cos(2*t/3)

plt.plot(t, x)
plt.xlabel("t in sec."); plt.ylabel("x(t)")
plt.grid()
plt.show()

# 샘플링된 신호 x_c(nT)
t = np.linspace(0, 10, 21)
x = np.cos(2*t/3)

plt.stem(t, x)
plt.xlabel("t in sec."); plt.ylabel("x(t)")
plt.grid()
plt.show()


# 샘플링된 신호 x[n]
n = np.arange(0,21)

plt.stem(n, x)
plt.xlabel("n"); plt.ylabel("x[n]")
plt.grid()
plt.show()

# 샘플링된 신호를 xlabel 하나하나 맵핑
n = np.arange(0,21)

plt.figure(figsize=(15,10))
plt.stem(n, x)
plt.grid()

plt.xticks(range(21))
plt.xlabel("n"); plt.ylabel("x[n]")
plt.show()

t = np.linspace(0, 10, 21)
x = np.cos(2*t/3)

plt.figure(figsize=(15, 10))
markers, _, _ = plt.stem(t,x) # 언더 바 처리하면 markers 값만 받는다.
plt.grid()

plt.xticks(np.linspace(0, 10, 21))
plt.setp(markers, marker='^')

plt.xlabel("t in sec.")
plt.ylabel("x(t)")
plt.show()