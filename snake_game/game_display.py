import random
import pygame
from food import Food

class GameDisplay:
    def __init__(self, screen_width, screen_height, cell_size, colors, snake, food, play_again_rect):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.cell_size = cell_size
        self.colors = colors      
        self.snake = snake
        self.food = food
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake')
        self.font = pygame.font.SysFont(None, 25)
        self.play_again_rect = play_again_rect

    def draw_game_over(self):
        game_over_text = self.font.render('Game Over', True, self.colors['black'])
        self.screen.blit(game_over_text, [self.screen_width / 2 - 50, self.screen_height / 2 - 20])  # Adjust the y-coordinate
        
        play_again = self.font.render('Press any key to play again', True, self.colors['black'])
        pygame.draw.rect(self.screen, self.colors['black'], self.play_again_rect, 2)
        self.screen.blit(play_again, [self.screen_width / 2 - 50, self.screen_height / 2 + 20])  # Adjust the y-coordinate
        
        pygame.display.flip()
        
    def draw_score(self, score):
        score_text = self.font.render('Score: ' + str(score), True, self.colors['black'])
        self.screen.blit(score_text, [0, 0])
        
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
        pygame.draw.rect(self.screen, self.colors['red'], (self.food.pos[0], self.food.pos[1], self.cell_size, self.cell_size))
   