# 구멍: n개 / 겹치지 않음
# 정수 고정 길이의 보수 패치를 사용해 구멍 수리 가능
# 보수 패치를 최대 K개 사용해 모든 구멍을 최소 길이의 패치로 효율적으로 수리
# e.g. 구멍: 1, 3, 4 / 보수패치 1개 -> 최소 길이 4 / 보수패치 2개 -> 최소 길이 2

# 시간 초과 풀이
# N, K = map(int, input().split())
# positions = list(map(int, input().split()))
# positions.sort()

# def possible(length):
#     used = 0
#     covered_until = -1

#     for pos in positions:
#         if pos > covered_until:
#             used += 1
#             covered_until = pos + length - 1

#     return used <= K

# max_length = positions[-1] - positions[0] + 1

# for length in range(1, max_length + 1):
#     if possible(length):
#         print(length)
#         break


N, K = map(int, input().split())
positions = list(map(int, input().split()))
positions.sort()

# 주어진 길이로 패치 K개 이하를 사용해 수리할 수 있는가?
def possible(length):
    used = 0
    covered_until = -1

    for pos in positions:
        if pos > covered_until:
            used += 1
            covered_until = pos + length - 1

    return used <= K

# 정답이 있을 길이 범위
left = 1
right = positions[-1] - positions[0] + 1

while left < right:
    mid = (left + right) // 2

    if possible(mid):
        right = mid      # 가능: 더 짧은 길이 찾아보기
    else:
        left = mid + 1   # 불가능: 더 긴 길이 찾아보기

print(left)