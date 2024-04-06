class CodeName():
    def __init__(self, code_name, score):
        self.code_name = code_name
        self.score = score


agent_list = [list(map(str, input().split())) for _ in range(5)]

agents = [CodeName(agent[0], int(agent[1])) for agent in agent_list]

min_score = 1000

for idx in range(5):
    if min_score > agents[idx].score:
        min_score = agents[idx].score
        min_code_name = agents[idx].code_name
        
print(min_code_name, min_score)