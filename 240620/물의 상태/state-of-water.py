water_temperature = int(input())

if water_temperature < 0:
    print("ice")
elif water_temperature >= 100:
    print("vapor")
else:
    print("water")