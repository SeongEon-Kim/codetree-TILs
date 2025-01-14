a, b = map(int, input().split())

def calculation(a, b):
    # 작은 값과 큰 값을 판단하여 조건에 따라 처리
    if a < b:
        small = a * 2
        large = b + 25
    else:
        small = b * 2
        large = a + 25

    # 결과를 공백으로 구분하여 반환
    return f"{small} {large}"

# 함수 실행 후 출력
print(calculation(a, b))
