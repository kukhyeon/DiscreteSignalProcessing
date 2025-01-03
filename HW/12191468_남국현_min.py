import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 영점 정의
z = np.array([0.9*np.exp(1j*0.6*np.pi), 0.9*np.exp(-1j*0.6*np.pi),
              0.8*np.exp(1j*0.8*np.pi), 0.8*np.exp(-1j*0.8*np.pi)])

# 극점 정의
p = [0, 0, 0, 0]

# 전달 함수의 gain 정의
k = (1.25)**2

# 영점, 극점, 이득 값을 이용하여 전달 함수의 다항식 계수(분자와 분모)를 계산.
b, a = signal.zpk2tf(z, p, k)


Omega, X = signal.freqz_zpk(z, p, k, whole=True) # 주파수 응답 계산
magnitude = np.abs(X) # 크기 계산
magnitude_db = 20*np.log10(magnitude) # 데시벨로 변환
phase = np.angle(X) # 위상 계산.
w, gd = signal.group_delay((b, a), whole=True) # 전달 함수의 group delay 계산.

plt.figure(figsize=(15,10))
plt.subplot(3,1,1)
plt.plot(Omega, magnitude_db)
plt.grid()
plt.title("Magnitude & Phase Response & Group delay")
plt.ylabel("Magnitude[dB] of X(z)")

plt.subplot(3,1,2)
plt.plot(Omega, phase)
plt.grid()
plt.ylabel("Phase of X(z)")

plt.subplot(3,1,3)
plt.plot(w, gd)
plt.grid()
plt.ylabel("Groud delay of X(z)")
plt.xlabel("Radian Frequency(w)")

plt.show()