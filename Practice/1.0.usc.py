import numpy as np
import matplotlib.pyplot as plt

start = 0
end = 10
impulse = 3

n = np.arange(start, end+1)
x = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
unit_sample_seq = [1 if (start + i) == impulse else 0 for i in range(start, end+1)]
unit_sample_array = np.array(unit_sample_seq)
print(unit_sample_array)

plt.figure(figsize=(10, 5))
plt.stem(n, unit_sample_array)
plt.grid()
plt.title("title")
plt.xlabel("xlabel")
plt.ylabel("ylabel")

plt.show()