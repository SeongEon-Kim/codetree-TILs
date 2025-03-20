n, k, t = input().split()
n, k = int(n), int(k)
string_list = [input() for _ in range(n)]

# starts_with 함수 직접 구현
def starts_with(string, prefix):
    return string[:len(prefix)] == prefix

# t로 시작하는 문자열만 필터링
include_list = [string for string in string_list if starts_with(string, t)]

# 사전순 정렬 후 k번째 원소 출력
sorted_include_list = sorted(include_list)
print(sorted_include_list[k-1])
