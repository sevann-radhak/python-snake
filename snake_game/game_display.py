import pygame


class GameDisplay:
    TEXT_OFFSET_X = 50
    TEXT_OFFSET_Y = 20

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

    def render_text(self, text, color, position):
        rendered_text = self.font.render(text, True, color)
        self.screen.blit(rendered_text, position)

    def draw_rectangle(self, color, position):
        pygame.draw.rect(self.screen, color, position)

    def draw_game_over(self):
        self.draw_rectangle(self.colors['black'], self.play_again_rect)
        self.render_text('Game Over', self.colors['black'], [self.screen_width / 2 - self.TEXT_OFFSET_X, self.screen_height / 2 - self.TEXT_OFFSET_Y])
        self.render_text('Press here to play again', self.colors['white'], [self.screen_width / 2 - self.TEXT_OFFSET_X - 50, self.screen_height / 2 + self.TEXT_OFFSET_Y])
        pygame.display.flip()
        
    def draw_score(self, score):
        self.render_text('Score: ' + str(score), self.colors['black'], [0, 0])
        
    def draw_screen(self):
        self.screen.fill(self.colors['light-gray']) 
      
    def draw_snake_pos(self):           
        for i, pos in enumerate(self.snake.snake_pos):
            if i == 0:
                self.draw_rectangle(self.colors['dark-green'], (pos[0], pos[1], self.cell_size, self.cell_size))
                self.draw_rectangle(self.colors['darker-green'], (pos[0] + 1, pos[1] + 1, self.cell_size - 2, self.cell_size - 2))
            else:
                self.draw_rectangle(self.colors['dark-green'], (pos[0], pos[1], self.cell_size, self.cell_size))
                self.draw_rectangle(self.colors['light-green'], (pos[0] + 1, pos[1] + 1, self.cell_size - 2, self.cell_size - 2))
    
    def draw_food(self):        
        self.draw_rectangle(self.colors['red'], (self.food.pos[0], self.food.pos[1], self.cell_size, self.cell_size))