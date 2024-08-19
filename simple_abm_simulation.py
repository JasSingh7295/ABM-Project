from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

# Define an Agent class
class MyAgent(Agent):
    """ An agent with a fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.is_active = True  # Example attribute

    def step(self):
        
        self.is_active = not self.is_active

        
        possible_moves = self.model.grid.get_neighborhood(
            self.pos,  
            moore=True,  
            include_center=False  
        )
        new_position = self.random.choice(possible_moves)
        self.model.grid.move_agent(self, new_position)


def agent_portrayal(agent):
    """ This function dictates how agents are visually represented in the simulation."""
    portrayal = {
        "Shape": "circle",
        "Color": "blue" if agent.is_active else "red",
        "Filled": "true",
        "Layer": 0,
        "r": 0.5
    }
    return portrayal


class MyModel(Model):
    def __init__(self, N):
        
        super().__init__()
        self.num_agents = N
        self.grid = MultiGrid(10, 10, True)
        self.schedule = RandomActivation(self)
        
        
        for i in range(self.num_agents):
            a = MyAgent(i, self)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.schedule.step()

# Set up the visualization
grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = ModularServer(MyModel,
                       [grid],
                       "My Model",
                       {"N":10})  
server.launch()
