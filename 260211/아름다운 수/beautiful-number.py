# 아름다운수: 1~4의 정수 / 
# 등장했다면 해당 숫자만큼 연달아 나와야함 ex: 133221 / 
# 동일한 숫자에 대해 연달아 같은 숫자 묶음이 나오는 것 또한 아름다운 수 ex: 111 <-> 222 (2 2번, 2 1번)

n = int(input())
cnt = 0

def beautiful_num(length):
    global cnt

    # 종료: 정확히 n자리면 카운트
    if length == n:
        cnt += 1
        return

    # 가지치기: n을 넘으면 중단
    if length > n:
        return

    # 블록 선택: 1~4 중 하나 붙이기
    for d in range(1, 5):
        if length + d <= n:
            beautiful_num(length+d)

beautiful_num(0)
print(cnt)

'''
# 변수 선언 및 입력:
n = int(input())
ans = 0
seq = list()


def is_beautiful():
    # 연달아 같은 숫자가 나오는 시작 위치를 잡습니다.
    i = 0
    while i < n:
        # 만약 연속하여 해당 숫자만큼 나올 수 없다면
        # 아름다운 수가 아닙니다.
        if i + seq[i] - 1 >= n:
            return False
        # 연속하여 해당 숫자만큼 같은 숫자가 있는지 확인합니다.
        # 하나라도 다른 숫자가 있다면
        # 아름다운 수가 아닙니다.
        for j in range(i, i + seq[i]):
            if seq[j] != seq[i]:
                return False
            
        i += seq[i]
        
    return True


def count_beautiful_seq(cnt):
    global ans
    
    if cnt == n:
        if is_beautiful():
            ans += 1
        return
	
    for i in range(1, 5):
        seq.append(i)
        count_beautiful_seq(cnt + 1)
        seq.pop()


count_beautiful_seq(0)
print(ans)
'''