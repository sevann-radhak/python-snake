from direction import Direction

class Snake:
    def __init__(self, screen_width, screen_height, cell_size):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.snake_pos = [[int(self.screen_width/2), int(self.screen_height/2)]]
        self.direction = Direction.UP     
        self.game_is_over = False
        
    
    def check_if_snake_has_eaten_the_food(self, food):        
        return self.snake_pos[0] == food.pos
    
    
    def add_piece(self, new_piece):
        if self.direction == Direction.UP:
            new_piece[1] += self.cell_size
        elif self.direction == Direction.DOWN:
            new_piece[1] -= self.cell_size
        elif self.direction == Direction.RIGHT:
            new_piece[0] -= self.cell_size
        elif self.direction == Direction.LEFT: 
            new_piece[0] += self.cell_size  
        
        self.snake_pos.append(new_piece)
        
    def create(self):
        self.snake_pos.append([int(self.screen_width/2), int(self.screen_height/2) + self.cell_size * 1])
        self.snake_pos.append([int(self.screen_width/2), int(self.screen_height/2) + self.cell_size * 2])
        self.snake_pos.append([int(self.screen_width/2), int(self.screen_height/2) + self.cell_size * 3])
        
        
    def move(self):
        self.snake_pos = self.snake_pos[-1:] + self.snake_pos[:-1]

        if self.direction == Direction.UP:
            self.snake_pos[0][0] = self.snake_pos[1][0]
            self.snake_pos[0][1] = self.snake_pos[1][1] - self.cell_size
        elif self.direction == Direction.DOWN:
            self.snake_pos[0][0] = self.snake_pos[1][0]
            self.snake_pos[0][1] = self.snake_pos[1][1] + self.cell_size
        elif self.direction == Direction.RIGHT:
            self.snake_pos[0][1] = self.snake_pos[1][1]
            self.snake_pos[0][0] = self.snake_pos[1][0] + self.cell_size
        elif self.direction == Direction.LEFT:
            self.snake_pos[0][1] = self.snake_pos[1][1]
            self.snake_pos[0][0] = self.snake_pos[1][0] - self.cell_size
            