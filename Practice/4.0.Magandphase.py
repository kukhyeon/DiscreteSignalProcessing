import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams, patches
from scipy import signal

b = np.array([1, 0])
a = np.array([1, -0.5])

Omega, X = signal.freqz(b, a)
mag = abs(X)
phase = np.angle(X, deg="True")
