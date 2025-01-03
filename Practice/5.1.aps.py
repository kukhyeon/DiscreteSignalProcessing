import numpy as np 
import matplotlib.pyplot as plt  
from scipy import signal  

# 주어진 theta 값 설정
theta = 0.8 * np.pi  # theta = 0.8 * pi

# 영점 정의, 역수로 하는 것을 조심하라
z = 1 / np.array([0.8 * np.exp(-1j * theta), 
                  0.8 * np.exp(1j * theta)])
p = np.array([0.8 * np.exp(-1j * theta), 
              0.8 * np.exp(1j * theta)])

# DC 이득을 직접 계산하여 정규화
dc_gain = 1/1.5625  # DC 이득 계산
b, a = signal.zpk2tf(z, p, dc_gain) # 영점, 극점, 이득 값을 이용하여 전달 함수의 다항식 계수(분자와 분모)를 계산.

Omega, X = signal.freqz(b, a, whole=True)  # 주파수 응답 계산
magnitude = np.abs(X)  # 크기 계산
magnitude_db = 20 * np.log10(magnitude)  # 크기를 데시벨로 변환
phase = np.angle(X)  # 위상 계산
w, gd = signal.group_delay((b, a), whole=True)  # 그룹 딜레이 계산


plt.figure(figsize=(15, 15))  
plt.subplot(3, 1, 1) 
plt.plot(Omega, magnitude_db)  # 크기 응답 그래프 그리기  
plt.grid() 
plt.title("Magnitude & Phase Response & Group delay")  
plt.ylabel("Magnitude[dB] of X(z)") 
plt.ylim(-1, 1)  # 범위 제한

plt.subplot(3, 1, 2) 
plt.plot(Omega, phase)  # 위상 응답 그래프 그리기
plt.grid() 
plt.ylabel("Phase of X(z)")

plt.subplot(3, 1, 3)  
plt.plot(w, gd)  # 그룹 딜레이 그래프 그리기
plt.grid()
plt.ylabel("Groud delay of X(z)")  
plt.xlabel("Randian Frequence(w)") 

plt.show()

  
