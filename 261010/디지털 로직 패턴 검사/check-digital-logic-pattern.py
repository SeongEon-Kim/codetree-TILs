# 문자열 입력 받기
S = input()

# 정수 K와 M 입력 받기
K, M = map(int, input().split())

# 해싱값을 카운트하는 사전
cnt = {}

# 첫 길이 K의 패턴을 해싱
p = 0
for i in range(K):
    p = p * 2 + (ord(S[i]) - ord('0'))

cnt[p] = 1

for i in range(K, len(S)):
    # 이전 패턴의 해싱값을 이용하여 새로운 해싱값을 O(1)로 계산
    p = p * 2 - (ord(S[i - K]) - ord('0')) * (1 << K) + (ord(S[i]) - ord('0'))
    # 해싱된 패턴 개수 증가
    if p in cnt:
        cnt[p] += 1
    else:
        cnt[p] = 1

# M번 이상 등장한 패턴이 있는지 확인
flag = False
for value in cnt.values():
    if value >= M:
        flag = True
        break

# 결과 출력
print(int(flag))


# 1. 메모리 초과 풀이
# s = input()
# k, m = map(int, input().split()) # 길이 k 이상의 동일한 패턴 m번 이상 나오면 불안정한 디지털 로직

# counts = {}  # 패턴별 등장 횟수
# answer = 0

# for i in range(len(s) - k + 1): # s = 12, k = 3  => 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 까지 패턴
#     pattern = s[i:i + k]

#     if pattern in counts:
#         counts[pattern] += 1
#     else: 
#         counts[pattern] = 1
    
#     if counts[pattern] >= m:
#         answer = 1
#         break

# print(answer)