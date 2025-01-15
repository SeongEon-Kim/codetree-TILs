secret_code, meeting_point, time = input().split()
time = int(time)

# Write your code here!
class Agent:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time
        

a = Agent(secret_code, meeting_point, time)

print("secret code :", a.code)
print("meeting point :", a.point)
print("time :", a.time)