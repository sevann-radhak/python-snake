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
        movements = {
            Direction.UP: [0, self.cell_size],
            Direction.DOWN: [0, -self.cell_size],
            Direction.RIGHT: [-self.cell_size, 0],
            Direction.LEFT: [self.cell_size, 0]
        }
        movement = movements[self.direction]
        new_piece[0] += movement[0]
        new_piece[1] += movement[1]
        self.snake_pos.append(new_piece)
        
        
    def create(self):
        for i in range(1, 4):
            self.snake_pos.append([int(self.screen_width/2), int(self.screen_height/2) + self.cell_size * i])

        
    def move(self):
        self.snake_pos = self.snake_pos[-1:] + self.snake_pos[:-1]

        movements = {
            Direction.UP: [0, -self.cell_size],
            Direction.DOWN: [0, self.cell_size],
            Direction.RIGHT: [self.cell_size, 0],
            Direction.LEFT: [-self.cell_size, 0]
        }
        
        movement = movements[self.direction]
        self.snake_pos[0][0] = self.snake_pos[1][0] + movement[0]
        self.snake_pos[0][1] = self.snake_pos[1][1] + movement[1]