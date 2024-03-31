def select_min_value(*args):
    print(min(args))

a, b, c = tuple(map(int, input().split()))

select_min_value(a, b, c)