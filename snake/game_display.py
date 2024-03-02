import pygame
from colors import Colors
from direction import Direction
from snake import Snake

class GameDisplay:
    def __init__(self):
        pygame.init()
        self.screen_width = 600
        self.screen_height = 600
        self.cell_size = 10
        self.colors = Colors().colors  
        self.update_snake = 0        
        self.snake = Snake(self.screen_width, self.screen_height, self.cell_size)
    
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake')


    def draw_screen(self):
        self.screen.fill(self.colors['light-gray']) 
      
        
    def draw_snake_pos(self):           
        for i, pos in enumerate(self.snake.snake_pos):
            if i == 0:
                pygame.draw.rect(self.screen, self.colors['dark-green'], (pos[0], pos[1], self.cell_size, self.cell_size))
                pygame.draw.rect(self.screen, self.colors['darker-green'], (pos[0] + 1, pos[1] + 1, self.cell_size - 2, self.cell_size - 2))
            else:
                pygame.draw.rect(self.screen, self.colors['dark-green'], (pos[0], pos[1], self.cell_size, self.cell_size))
                pygame.draw.rect(self.screen, self.colors['light-green'], (pos[0] + 1, pos[1] + 1, self.cell_size - 2, self.cell_size - 2))
         
   
    def run(self):
        
        self.snake.create()
        while True:   
            self.draw_screen()    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != Direction.DOWN:
                        self.snake.direction = Direction.UP
                    elif event.key == pygame.K_DOWN and self.snake.direction != Direction.UP:
                        self.snake.direction = Direction.DOWN
                    elif event.key == pygame.K_LEFT and self.snake.direction != Direction.RIGHT:
                        self.snake.direction = Direction.LEFT
                    elif event.key == pygame.K_RIGHT and self.snake.direction != Direction.LEFT:
                        self.snake.direction = Direction.RIGHT
            
            if self.update_snake > 99:
                print(f'update_snake: {self.update_snake}')
                self.update_snake = 0        
                self.snake.move()
                
            self.draw_snake_pos()
                
            pygame.display.update()
            self.update_snake += 1
