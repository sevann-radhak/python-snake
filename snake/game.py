import pygame
from colors import Colors

class GameDisplay:
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.screen_width = 600
        self.screen_height = 600
        self.cell_size = 10
        self.colors = Colors().colors  
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake')


    def draw(self):
        self.screen.fill(self.colors['light-gray']) 
       
       
    def draw_snake(self):
        snake_pos = [[int(self.screen_width/2), int(self.screen_height/2)]]        
        snake_pos.append([int(self.screen_width/2), int(self.screen_height/2) + self.cell_size * 1])
        snake_pos.append([int(self.screen_width/2), int(self.screen_height/2) + self.cell_size * 2])
        snake_pos.append([int(self.screen_width/2), int(self.screen_height/2) + self.cell_size * 3])
        
        for i, pos in enumerate(snake_pos):
            if i == 0:
                pygame.draw.rect(self.screen, self.colors['dark-green'], (pos[0], pos[1], self.cell_size, self.cell_size))
                pygame.draw.rect(self.screen, self.colors['darker-green'], (pos[0] + 1, pos[1] + 1, self.cell_size - 2, self.cell_size - 2))
            else:
                pygame.draw.rect(self.screen, self.colors['dark-green'], (pos[0], pos[1], self.cell_size, self.cell_size))
                pygame.draw.rect(self.screen, self.colors['light-green'], (pos[0] + 1, pos[1] + 1, self.cell_size - 2, self.cell_size - 2))
   
    def run(self):
        self.draw()
        while True:       
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if self.game.game_is_over:
                    if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
                        clicked = True
                    if event.type == pygame.MOUSEBUTTONUP and clicked:
                        clicked = False
                        print('game over')
                else:    
                    self.draw_snake()
                
                pygame.display.update()
