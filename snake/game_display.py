import random
import pygame

class GameDisplay:
    def __init__(self, screen_width, screen_height, cell_size, colors, snake, new_food):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.colors = colors      
        self.snake = snake
        self.new_food = new_food
    
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
    
    def draw_food(self):
        if self.new_food:
            self.food = [random.randrange(1, (self.screen_width//10)) * 10, random.randrange(1, (self.screen_height//10)) * 10]
            self.new_food = False
        
        pygame.draw.rect(self.screen, self.colors['red'], (self.food[0], self.food[1], self.cell_size, self.cell_size))
   