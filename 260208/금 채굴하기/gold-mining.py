# 벗어난 영역도 OK, 금 채굴 인정 x
# 마름모: 특정 중심점을 기준으로 K번 이내 상하좌우의 인접한 곳으로 이동하는 걸 반복했을 때 갈 수 있는 모든 영역이 색칠되어 있는 모양
# 채굴 비용: K^2 + (K+1)^2 <= 금 한개의 가격 = M 을 만족하는 가장 큰 K

n, m = tuple(map(int, input().split()))
grid = [ list(map(int, input().split())) for _ in range(n)]
print(n, m , grid)

drs, dcs = [-1, 1, 0, 0], [0, 0, -1, 1]
r, c = 0, 0
k = 0

# if. k = 1 