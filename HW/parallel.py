import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

tn = 5000  # 총 샘플 수
t = np.linspace(0, 1, tn)  # 시간 벡터 생성
x = chirp(t, f0=10, t1=0.2, f1=500, method='linear')  # Chirp 신호 생성

input = x.copy()  # 입력 신호 복사

# 각 필터의 출력을 저장할 배열 초기화
y0 = np.full(tn, 1/16)  # 상수 항
y1 = np.zeros(tn)  # 첫 번째 1차 필터 출력
y2 = np.zeros(tn)  # 두 번째 1차 필터 출력
y3 = np.zeros(tn)  # 2차 필터 출력

# 첫 번째 1차 필터 계수
b1 = [37/80]
a1 = [1, -0.5]

# 두 번째 1차 필터 계수
b2 = [-435/64]
a2 = [1, 0.25]

# 2차 필터 계수
b3 = [61/10, 201/40]
a3 = [1, 1, 0.5]

# 이전 입력 및 출력 값 저장을 위한 변수 초기화
x1_past = 0  # 첫 번째 1차 필터 이전 입력값
y1_past = 0  # 첫 번째 1차 필터 이전 출력값

x2_past = 0  # 두 번째 1차 필터 이전 입력값
y2_past = 0  # 두 번째 1차 필터 이전 출력값

x3_past = [0, 0]  # 2차 필터 이전 입력값들
y3_past = [0, 0]  # 2차 필터 이전 출력값들

for n in range(tn):
    x_n = input[n]

    # 상수 항 처리
    y0[n] = y0[n] * x_n

    # 첫 번째 1차 필터 처리
    y1[n] = b1[0]*x_n - a1[1]*y1_past
    y1_past = y1[n]

    # 두 번째 1차 필터 처리
    y2[n] = b2[0]*x_n - a2[1]*y2_past
    y2_past = y2[n]

    # 2차 필터 처리
    y3[n] = (b3[0]*x_n + b3[1]*x3_past[0]
             - a3[1]*y3_past[0] - a3[2]*y3_past[1])

    # 이전 값 업데이트 (2차 필터)
    x3_past[1] = x3_past[0]
    x3_past[0] = x_n
    y3_past[1] = y3_past[0]
    y3_past[0] = y3[n]

# 전체 출력은 각 필터의 출력의 합
y_total = y0 + y1 + y2 + y3

# 결과를 시각화
plt.figure(figsize=(15, 10))

plt.subplot(2,1,1)
plt.plot(x, "m")
plt.xlim(0, tn)
plt.ylabel("Amplitude")
plt.title("Chirp signal")

plt.subplot(2,1,2)
plt.plot(y_total, "b")
plt.xlim(0, tn)
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid()
plt.title("Frequency filtering result of IIR parallel filter")

plt.show()
