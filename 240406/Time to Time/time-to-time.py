start_hour, start_min, finish_hour, finish_min = tuple(input().split())

difference =  -60 * int(start_hour) - int(start_min) + 60 * int(finish_hour) + int(finish_min)

print(difference)