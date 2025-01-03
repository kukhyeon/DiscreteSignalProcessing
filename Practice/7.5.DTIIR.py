import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy.signal import chirp

def FR_Signal_filtering(b, a):
    system = [b, a, 1]
    n, hn = signal.dimpulse(system)
    hn = np.asarray(hn).squeeze() # 까먹지 말 것
    
    t = np.linspace(0, 1, 5000)
    xn = chirp(t, f0=10, t1=0.2, f1=500, method='linear')
    yn = np.convolve(hn, xn)
    
    plt.plot(yn, 'blue')
    plt.grid()
    plt.show()
    
OmegaP = 0.2*np.pi
OmegaS = 0.3*np.pi
Rs = 7
As = 40
T = 1
F = 1/T

wp = 2*np.arctan(OmegaP*T/2)
ws = 2*np.arctan(OmegaS*T/2)

# 차수하고 차단 주파수 구하고, 아날로그 계수 구한 뒤에 디지털로 변환환
N, wc = signal.buttord(wp, ws, Rs, As, analog=True)
b, a = signal.butter(N, wc, 'lowpass', analog=True)
d, c = signal.bilinear(b, a, F) # 주파수가 들어간다다

Omega, H = signal.freqz(d, c)