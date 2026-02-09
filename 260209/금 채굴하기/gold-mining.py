n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_gold = 0

# 1. k를 0부터 n+1까지 확장 (마름모가 격자를 완전히 벗어날 때까지)
for k in range(n + 2):
    cost = k * k + (k + 1) * (k + 1)
    
    # 2. 모든 좌표(r, c)를 마름모의 중심으로 잡아보기
    for r in range(n):
        for c in range(n):
            gold_count = 0
            
            # 3. 마름모 영역 안의 금 개수 세기 (상하좌우 K번 이동 = 거리 k 이하)
            # 팁: 격자 전체를 다 돌지 않고, 중심 근처만 돌면 더 빨라요!
            for i in range(r - k, r + k + 1):
                for j in range(c - k, c + k + 1):
                    # 격자 안에 있고, 거리가 k 이하인 지점만 확인
                    if 0 <= i < n and 0 <= j < n:
                        if abs(i - r) + abs(j - c) <= k:
                            if grid[i][j] == 1:
                                gold_count += 1
            
            # 4. 손해를 보지 않는다면 최대 금 개수 갱신
            if gold_count * m >= cost:
                max_gold = max(max_gold, gold_count)

print(max_gold)