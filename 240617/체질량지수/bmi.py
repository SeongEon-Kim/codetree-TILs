n, m = list(map(int, input().split()))

def calc_bmi(n,m):
    bmi = (10000 * m)/n*n
    return bmi

bmi = calc_bmi(n,m)
if bmi >=25:
    print(bmi)
    print("Obesity")
else:
    print(bmi)