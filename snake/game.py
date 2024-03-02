import pygame
from colors import Colors
from direction import Direction

class GameDisplay:
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.screen_width = 600
        self.screen_height = 600
        self.cell_size = 10
        self.colors = Colors().colors  
        self.direction = Direction.UP
        self.update_snake = 0
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake')


    def draw_screen(self):
        self.screen.fill(self.colors['light-gray']) 
       
       
    def create_snake(self):
        self.snake_pos = [[int(self.screen_width/2), int(self.screen_height/2)]]        
        self.snake_pos.append([int(self.screen_width/2), int(self.screen_height/2) + self.cell_size * 1])
        self.snake_pos.append([int(self.screen_width/2), int(self.screen_height/2) + self.cell_size * 2])
        self.snake_pos.append([int(self.screen_width/2), int(self.screen_height/2) + self.cell_size * 3])
        
        
    def draw_snake_pos(self):           
        for i, pos in enumerate(self.snake_pos):
            if i == 0:
                pygame.draw.rect(self.screen, self.colors['dark-green'], (pos[0], pos[1], self.cell_size, self.cell_size))
                pygame.draw.rect(self.screen, self.colors['darker-green'], (pos[0] + 1, pos[1] + 1, self.cell_size - 2, self.cell_size - 2))
            else:
                pygame.draw.rect(self.screen, self.colors['dark-green'], (pos[0], pos[1], self.cell_size, self.cell_size))
                pygame.draw.rect(self.screen, self.colors['light-green'], (pos[0] + 1, pos[1] + 1, self.cell_size - 2, self.cell_size - 2))
          
        
    def draw_snake(self):
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
           
   
    def run(self):
        self.create_snake()
        while True:   
            self.draw_screen()    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != Direction.DOWN:
                        self.direction = Direction.UP
                    elif event.key == pygame.K_DOWN and self.direction != Direction.UP:
                        self.direction = Direction.DOWN
                    elif event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                        self.direction = Direction.LEFT
                    elif event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                        self.direction = Direction.RIGHT
            
            if self.update_snake > 99:
                print(f'update_snake: {self.update_snake}')
                self.update_snake = 0        
                self.draw_snake()
                
            self.draw_snake_pos()
                
            pygame.display.update()
            self.update_snake += 1
