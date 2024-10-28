import numpy as np
import matplotlib.pyplot as plt

start = 0
end = 5
n = np.arange(start, end+1)
seq = [1 if (start + i) > 3 else 0 for i in range(start, end+1)]
x = np.array(seq)
print(x)

plt.figure(figsize=(10, 5))
markers, stemlines, baseline = plt.stem(n, x)
markers.set_color("red")
stemlines.set_color("blue")
baseline.set_color("green")
plt.grid()
plt.show()
