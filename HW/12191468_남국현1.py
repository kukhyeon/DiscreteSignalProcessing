import numpy as np
import matplotlib.pyplot as plt

# 변수 설정
start = 0
end = 20
impulse = 3

# 배열 생성
dt_seq = np.arange(start, end+1)

# 변수와 배열 상태 출력
print(f"Start: {start}, End: {end}, Impulse: {impulse}")
print("Sequence length: ", end-start)
print("Discrete-time sequence: {}".format(dt_seq))

# 리스트 표현식을 통해 Unit sample sequence 작성
unit_sample_list = [1 if (i+start) == impulse else 0 for i in range(end+1)]
unit_sample_array = np.array(unit_sample_list)

# Unit sample sequence 값 출력
print(f"Unit sample sequence: {unit_sample_array}")

plt.figure(figsize = (10, 5)) # 그래프 크기를 10x5로 설정
plt.stem(dt_seq, unit_sample_array); plt.grid() # dt_seq와 unit_sample_array를 이용해 그래프를 그림, 격자선 추가
plt.title("Unit sample sequence") # 그래프 제목 설정
plt.xlabel("n"); plt.ylabel("x[n]") # 축 라벨 지정

plt.show() # 그래프를 화면에 표시

# 새로운 값으로 변수 재설정
start = 0
end = 10
impulse = 3

# 배열을 다시 만들고, 리스트 표현식으로 Unit step sequence 생성
dt_seq = np.arange(start, end+1)
unit_sample_list = [1 if (i+start) >= impulse else 0 for i in range(end+1)]
unit_sample_array = np.array(unit_sample_list)

# Unit step sequence 값 출력
print(f"Unit sample sequence: {unit_sample_array}")

# np.zeros를 사용해 같은 작업을 수행
unit_sample_array = np.zeros(end+1, dtype=int)
unit_sample_array[impulse:] = 1

# Unit step sequence 값 다시 출력
print(f"Unit sample sequence: {unit_sample_array}")

# 그래프의 크기 설정
plt.figure(figsize= (10, 5))
# stem plot을 만들고, 그래프의 각 요소에 색상 설정을 위한 변수 추가
markers, stemlines, baseline = plt.stem(dt_seq, unit_sample_array); plt.grid()

# 각 그래프 요소에 색상을 적용
markers.set_color("red")
stemlines.set_color("blue")
baseline.set_color("green")

# 그래프 제목과 축 라벨 설정
plt.title("Unit step sequence")
plt.xlabel("n"); plt.ylabel("x[n]")

# 그래프 출력
plt.show()

# 정현파 DT 신호
n = np.linspace(0, 4*np.pi, 64) # 0에서 4π 사이를 64개의 구간으로 나누기
amp = 3 # 진폭 값을 3으로 설정
omega = 3*np.pi/8 # 각주파수를 3π/8로 설정
phase = np.pi/2 # 위상 값을 π/2로 설정
xn = amp * np.cos(omega*n + phase) # 정의된 변수들을 바탕으로 코사인 함수 생성

N = 2*np.pi / omega # 신호 주기 계산
print(f"Period: {N}, if k == 1") # 주기 출력

# 그래프 그리기
plt.figure(figsize= (10, 5)) # 그래프 사이즈 설정
plt.stem(n, xn, basefmt="blue"); plt.grid() # 이산 신호를 stem plot으로 표현하고, 파란색 베이스라인 추가
plt.title("Periodic sequence") # 그래프 제목 설정
plt.xlabel("n"); plt.ylabel("x[n]") # x축과 y축 라벨 설정

# 그래프 출력
plt.show()
