
import random

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])

class Model:
    def __init__(self, num_agents, width, height):
        self.agents = [Agent(random.randint(0, width), random.randint(0, height)) for _ in range(num_agents)]
        self.width = width
        self.height = height

    def step(self):
        for agent in self.agents:
            agent.move()

    def print_agents(self):
        for agent in self.agents:
            print(f"Agent position: ({agent.x}, {agent.y})")

num_agents = 5
width = 10
height = 10
model = Model(num_agents, width, height)


print("Initial agent positions:")
model.print_agents()

for i in range(3):
    model.step()
    print(f"\nAgent positions after step {i+1}:")
    model.print_agents()
