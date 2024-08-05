def is_subsequence(A, B):
    n1 = len(A)
    n2 = len(B)

    # 슬라이딩 윈도우를 사용하여 A에서 B의 길이만큼의 부분 배열을 비교
    for i in range(n1 - n2 + 1):
        if A[i:i+n2] == B:
            return "Yes"
    return "No"

# 입력 처리
n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 결과 출력
print(is_subsequence(A, B))