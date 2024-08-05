class RainDay:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day 
        self.weather = weather

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]

rain_info = [RainDay(date, day, weather) for date, day, weather in arr]
# 비오는 날만 필터링하여 새로운 리스트 생성
rain_days = [day for day in rain_info if day.weather == 'Rain']

target_idx = 0
for i, day in enumerate(rain_days):
    if day.date < rain_days[target_idx].date:
        target_idx = i

print(rain_days[target_idx].date, rain_days[target_idx].day, rain_days[target_idx].weather)