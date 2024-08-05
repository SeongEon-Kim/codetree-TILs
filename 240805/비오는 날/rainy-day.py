class RainDay:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day 
        self.weather = weather
    def get_rain_day_info(self):
        pass

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]

rain_info = [RainDay(date, day, weather) for date, day, weather in arr]

target_idx = 0
for i, day in enumerate(rain_info):
    if day.date < rain_info[target_idx].date and day.weather == 'Rain':
        target_idx = i

print(rain_info[target_idx].date, rain_info[target_idx].day, rain_info[target_idx].weather)