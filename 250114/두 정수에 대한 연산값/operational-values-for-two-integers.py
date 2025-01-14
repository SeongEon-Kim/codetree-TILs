a, b = map(int, input().split())

# 계산 함수
def calculation(a, b):
    if a < b:
        return f"{a * 2} {b + 25}"  # 출력 형식을 문자열로 반환
    else:
        return f"{b * 2} {a + 25}"  # 출력 형식을 문자열로 반환

# 결과 출력
print(calculation(a, b))
