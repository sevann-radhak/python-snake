import random

class Food:
    def __init__(self, screen_width, screen_height, cell_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.pos = [0, 0]
        self.randomize_position()

    def randomize_position(self):
        # if slf.new_food:
        # for _ in range(10):
        #     print()
        #     print(self.cell_size * random.randint(0, (self.screen_width // self.cell_size) - 1))
        #     print(self.cell_size * random.randint(0, (self.screen_width // self.cell_size) - 1))
        #     print()
        
        self.pos[0] = self.cell_size * random.randint(0, (self.screen_width // self.cell_size) - 1)
        self.pos[1] = self.cell_size * random.randint(0, (self.screen_width // self.cell_size) - 1)
            # self.new_food = False
        # print('food position')
        # print(self.pos[0], self.pos[1])