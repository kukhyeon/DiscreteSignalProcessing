import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

tn = 5000  # 총 샘플 수
t = np.linspace(0, 1, tn)  # 시간 벡터 생성
x = chirp(t, f0=10, t1=0.2, f1=500, method='linear')  # Chirp 신호 생성

input = x.copy()  # 입력 신호 복사
y1 = np.zeros(tn)  # 첫 번째 섹션의 출력을 저장할 배열
y2 = np.zeros(tn)  # 두 번째 섹션의 출력을 저장할 배열

# 섹션 1의 계수 (b: 분자, a: 분모)
b1 = [1/8, -3/8, 1/4]
a1 = [1, -1/4, -1/8]

# 섹션 2의 계수
b2 = [1/2, 0, 9/2]
a2 = [1, 1, 1/2]

# 이전 입력 및 출력 값을 저장할 변수 초기화
x1 = [0, 0]  # 섹션 1의 이전 입력값들
y1_past = [0, 0]  # 섹션 1의 이전 출력값들

x2 = [0, 0]  # 섹션 2의 이전 입력값들
y2_past = [0, 0]  # 섹션 2의 이전 출력값들

for n in range(tn):
    # 섹션 1 처리
    x_n = input[n]
    y1[n] = b1[0]*x_n + b1[1]*x1[0] + b1[2]*x1[1] - a1[1]*y1_past[0] - a1[2]*y1_past[1]

    # 이전 값 업데이트 (섹션 1)
    x1[1] = x1[0]
    x1[0] = x_n
    y1_past[1] = y1_past[0]
    y1_past[0] = y1[n]

    # 섹션 2 처리
    x_n2 = y1[n]
    y2[n] = b2[0]*x_n2 + b2[1]*x2[0] + b2[2]*x2[1] - a2[1]*y2_past[0] - a2[2]*y2_past[1]

    # 이전 값 업데이트 (섹션 2)
    x2[1] = x2[0]
    x2[0] = x_n2
    y2_past[1] = y2_past[0]
    y2_past[0] = y2[n]

IIR_cascade_output = y2.copy()  # 최종 출력 저장

# 결과를 시각화
plt.figure(figsize=(15, 10))

plt.subplot(2,1,1)
plt.plot(x, "m"); plt.xlim(0, tn)
plt.ylabel("Amplitude"); plt.title("Chirp signal")

plt.subplot(2,1,2)
plt.plot(IIR_cascade_output, "b"); plt.xlim(0, tn)
plt.xlabel("Samples"); plt.ylabel("Amplitude"); plt.grid()
plt.title("Frequency filtering result of IIR cascade filter")

plt.show()
