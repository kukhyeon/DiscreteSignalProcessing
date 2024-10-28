import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches, rcParams
from scipy import signal

def zplane(b, a, filename=None):
    ax = plt.subplot(111)
    
    uc = patches.Circle((0,0), radius=1, fill=False, color='black', ls='dashed')
    ax.add_patch(uc)
    
    if np.max(b) > 1:
        kn = np.max(b)
        b = b/np.float(kn)
    else:
        kn = 1
        
    if np.max(a) > 1:
        kd = np.max(a)
        a = a/np.float(kd)
    else:
        kd = 1
    
    p = np.roots(a)
    z = np.roots(b)
    k = kn/float(kd)
    
    t1 = plt.plot(z.real, z.imag, 'go', ms=10)
    t2 = plt.plot(p.real, p.imag, 'rx', ms=10)
    
    ax.spines['bottom'].set_position('center')
    ax.spines['left'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    plt.show()
    
    return z, p, k

b = np.array([1, 0])
a = np.array([1, -0.5])
plt.figure(figsize=(10, 10))
plt.grid()
zplane(b, a)            