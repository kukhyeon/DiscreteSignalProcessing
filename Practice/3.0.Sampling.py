import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)
x = np.cos(2*t/3)

# versus
n = np.arange(0, 21)

plt.stem(n, x)
plt.xticks(range(21))
plt.xlabel("n"); plt.ylabel("x[n]")
plt.grid()
plt.show()