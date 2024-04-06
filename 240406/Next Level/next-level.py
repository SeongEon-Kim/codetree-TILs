class NextLevel():
    def __init__(self, id="codetree", lv="10"):
        self.id = id
        self.lv = lv


user_id, user_lv = list(map(str, input().split()))

basic_account = NextLevel()
hello_account = NextLevel("hello", "28")

print("user", basic_account.id, "lv", basic_account.lv)
print("user", hello_account.id, "lv", hello_account.lv)