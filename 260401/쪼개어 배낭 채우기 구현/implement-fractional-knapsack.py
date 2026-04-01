N, M = map(int, input().split())
jewels = []

for _ in range(N):
    w, v = map(int, input().split())
    jewels.append((v / w, w, v))  # (가성비, 무게, 가격)

jewels.sort(reverse=True)

total_value = 0.0
remain = M

for ratio, weight, value in jewels:
    if remain == 0:
        break

    if weight <= remain:
        total_value += value
        remain -= weight
    else:
        total_value += ratio * remain
        remain = 0

print(f"{total_value:.3f}")