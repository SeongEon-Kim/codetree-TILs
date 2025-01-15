user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Write your code here!
class NextLevel:
    def __init__(self, id="codetree", level=10):
        self.id=id
        self.level=level
    def print_info(self):
        print("user", self.id, "lv", self.level)


user1 = NextLevel()
user2 = NextLevel(user2_id, user2_level)

user1.print_info()
user2.print_info()
