start_m, start_d, finish_m, finish_d = tuple(map(int, input().split()))
elapsed_days = 0
#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    if start_m == finish_m and start_d  == finish_d:
        break

    elapsed_days += 1
    start_d += 1

    if start_d > num_of_days[start_m]:
        start_m += 1
        start_d = 1

print(elapsed_days+1)