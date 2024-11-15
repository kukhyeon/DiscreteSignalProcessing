import numpy as np  
import matplotlib.pyplot as plt 

start_t = -5  
end_t = 5  
Ts = 0.5  # 샘플링 주기 설정
fs = 1 / Ts  # 샘플링 주파수 계산
N = int(np.abs(end_t - start_t) / Ts)  # 샘플 개수 계산

tp = np.arange(0, 5, Ts)  # 양의 시간 샘플 생성
tn = np.arange(-5, 0, Ts)  # 음의 시간 샘플 생성

t = np.zeros(N)  # 시간 축 초기화
t[:int(N / 2)] = tn  # 음의 시간 샘플 할당
t[int(N / 2):] = tp  # 양의 시간 샘플 할당

xc = np.exp(-np.abs(t))  # 샘플링된 신호 계산
n = np.arange(start_t / Ts, end_t / Ts)  # 이산 신호의 인덱스 생성

delta_t = 0.0005  # 재구성 시간 간격 설정
recon_t = np.arange(start_t, end_t, delta_t)  # 재구성 시간 축 생성
Nt = len(recon_t)  # 재구성 시간 샘플 수 계산

sinc_out = np.zeros(Nt)  # 재구성된 신호 초기화

# 신호 재구성을 위한 sinc 보간 수행
for i in range(Nt):
    sum = 0  # 합계 초기화
    for j in range(N):
        sum += xc[j] * np.sinc(fs * (i * delta_t - j * Ts))  # sinc 함수와 샘플 신호 곱하여 합산
    sinc_out[i] = sum  # 재구성된 신호에 저장
        
plt.figure(figsize=(10, 10))

# 첫 번째 서브플롯: 샘플링된 신호
plt.subplot(3, 1, 1)
plt.plot(t, xc)
markers, _, _ = plt.stem(t, xc)
plt.setp(markers, marker = '^')
plt.grid()
plt.xticks(range(-5, 6))
plt.xlabel("t in sec")
plt.ylabel("xc(t)")
plt.legend()

# 두 번째 서브플롯: 이산 신호 x[n]
plt.subplot(3, 1, 2)
plt.stem(n, xc, basefmt=" ")
plt.grid()
plt.xticks(np.arange(start_t / Ts, end_t / Ts + 1, 10))
plt.xlabel("n")
plt.ylabel("x[n]")
plt.title('x(n), Reconstructed signal using sinc function')

# 세 번째 서브플롯: 재구성된 신호
plt.subplot(3, 1, 3)
plt.plot(recon_t, sinc_out)
plt.plot(recon_t, np.exp(-np.abs(recon_t))) 
plt.grid()
plt.xlabel("t in sec")
plt.ylabel("x(t)")
plt.legend()

plt.tight_layout()
plt.show()

"""
 Reconstruction이 잘 수행되지 않는 이유
 이상적인 reconstruction을 위해선 샘플링된 신호를 무한한 길이의 sinc function으로 합성해야 한다. 
 하지만, 현실에서는 다음과 같은 이유들로 재구성이 어렵다.
 
 1. 무한한 지원 범위의 sinc function 사용 불가능
  - 이상적인 sinc function은 무한한 대역폭, 즉, 모든 주파수를 포함해야 함을 의미한다.
    하지만 실제 시스템에서는 무한한 대역폭을 구현할 수 없기에 sinc function을 정확히 구현할 수 없다.
    
 2. 필터의 실질적 구현 한계
  - 이상적인 필터는 시간과 주파수 영역에서 무한한 응답을 가지지만, 실제 필터는 유한한 시간과 주파수 응답을 가진다.
    이는 sinc function의 무한한 길이를 실제로 구현할 수 없음을 의미하며, 따라서 재구성 신호에 오차가 발생한다.
    
 3 수치적 오차와 정밀도 한계
  - 파이썬과 같은 프로그래밍 언어는 부동 소수점 연산을 사용하여 수치를 처리한다. 
    이로 인해 매우 작은 수치적 오차가 발생할 수 있으며, 특히 많은 계산을 반복할 경우 이러한 오차가 누적되어 정확도에 영향을 미친다.
    
 4. 디지털 신호 처리 알고리즘의 한계
  - 이론적으로 이상적인 알고리즘을 사용하더라도, 실제 구현에서는 알고리즘의 최적화, 메모리 관리, 병렬 처리 등 다양한 요소가 신호 재구성의 정확도에서 영향을 미칠 수 있다.
 5. 실시간 처리 제약
  - 이 프로그램은 reconstruction된 신호를 계산하기 위해 모든 샘플을 한 번에 처리한다.
    하지만 실시간 신호 처리에서는 이러한 방식이 비효율적일 수 있으며, 계산 속도와 자원의 한계로 인해 완벽한 재구성이 어렵다.
    
 Reconstruction의 정확도를 높이기 위해서는, 샘플링 주기 최적화, Windowing, Aliasing 방지 등 다양한 방법을 종합적으로 적용해야한다.
 이러한 개선 방안을 통해 이 프로그램의 Reconstruction 정확도를 크게 상승시킬 수 있을 것이다.
"""