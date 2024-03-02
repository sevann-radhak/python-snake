import random

class Food:
    def __init__(self, screen_width, screen_height, cell_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.pos = [0, 0]
        self.randomize_position()

    def randomize_position(self):
        self.pos[0] = random.randint(0, self.screen_width // self.cell_size - 1) * self.cell_size
        self.pos[1] = random.randint(0, self.screen_height // self.cell_size - 1) * self.cell_size