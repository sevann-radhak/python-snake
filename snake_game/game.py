import pygame
from game_display import GameDisplay
from snake import Snake
from colors import Colors
from direction import Direction
from food import Food


class Game:
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 600
        self.cell_size = 10
        self.update_snake = 0    
        self.food = Food(self.screen_width, self.screen_height, self.cell_size)
        self.new_food = True    
        self.new_piece = [0, 0]
        self.colors = Colors().colors
        self.snake = Snake(self.screen_width, self.screen_height, self.cell_size)
        self.display = GameDisplay(self.screen_width, self.screen_height, self.cell_size, self.colors, self.snake)
        self.snake.create()
        self.clock = pygame.time.Clock()
        self.FPS = 10
        self.font = pygame.font.Font(None, 24)
       
       
    def run(self):
        self.snake.create()
        while True:   
            self.display.draw_screen()    
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
            
            self.display.draw_food()
            
            if self.snake.check_if_snake_has_eaten_the_food(self.display.food):
                self.food.randomize_position()
                self.new_piece = list(self.snake.snake_pos[-1])
                self.snake.add_piece(self.new_piece)
                        
            self.display.draw_food()      
            self.snake.move()
                
            self.display.draw_snake_pos()                
            pygame.display.update()            
            self.clock.tick(self.FPS)
   
   
if __name__ == "__main__":
    game = Game()
    game.run()