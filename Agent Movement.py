
import random

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])

agent = Agent(5, 5)


print("Agent initialized at position ({}, {})".format(agent.x, agent.y))


agent.move()


print("Agent moved to position ({}, {})".format(agent.x, agent.y))
