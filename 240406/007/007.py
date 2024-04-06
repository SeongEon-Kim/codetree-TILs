class zzs:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

c, p, t = list(map(str, input().split()))

agent = zzs(c, p, t)

print("secret code :",agent.code)
print("meeting point :",agent.place)
print("time :",agent.time)