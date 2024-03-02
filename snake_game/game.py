import pygame
from game_display import GameDisplay
from snake import Snake
from colors import Colors
from direction import Direction
from food import Food
from game_settings import GameSettings


class Game:
    def __init__(self, settings):
        self.settings = settings
        self.new_food = True    
        self.new_piece = [0, 0]
        self.colors = Colors().colors
        rect_width = 250
        self.play_again_rect = pygame.Rect(self.settings.screen_width / 2 - rect_width / 2, self.settings.screen_height / 2, rect_width, 50)        
        self.clock = pygame.time.Clock()
        self.game_is_over = False
        self.reset_game()
       
        
    def check_if_game_is_over(self):
        return self.is_snake_out_of_bounds() or self.is_snake_collided_with_itself()


    def is_snake_out_of_bounds(self):
        return self.snake.snake_pos[0][0] >= self.settings.screen_width or self.snake.snake_pos[0][0] < 0 or self.snake.snake_pos[0][1] >= self.settings.screen_height or self.snake.snake_pos[0][1] < 0

   
    def is_snake_collided_with_itself(self):
        return any(block == self.snake.snake_pos[0] for block in self.snake.snake_pos[1:])
               
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != Direction.DOWN:
                    self.snake.direction = Direction.UP
                elif event.key == pygame.K_DOWN and self.snake.direction != Direction.UP:
                    self.snake.direction = Direction.DOWN
                elif event.key == pygame.K_LEFT and self.snake.direction != Direction.RIGHT:
                    self.snake.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT and self.snake.direction != Direction.LEFT:
                    self.snake.direction = Direction.RIGHT
        return True
            
    
    def reset_game(self):
        self.snake = Snake(self.settings.screen_width, self.settings.screen_height, self.settings.cell_size)
        self.food = Food(self.settings.screen_width, self.settings.screen_height, self.settings.cell_size)
        self.display = GameDisplay(self.settings.screen_width, self.settings.screen_height, self.settings.cell_size, self.colors, self.snake, self.food, self.play_again_rect)
        self.snake.create()
        self.score = 0
        self.settings.FPS = 10
        
       
    def run(self):
        while True:   
            self.display.draw_screen() 
            self.display.draw_score(self.score) 
            
            if not self.handle_events():
                return
            
            if self.check_if_game_is_over():
                self.display.draw_game_over()
                game_over = True
                while game_over:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            return
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()
                            if self.play_again_rect.collidepoint(pos):
                                print('Game over')
                                game_over = False
                                self.reset_game()
            else: 
                self.display.draw_food()
                
                if self.snake.check_if_snake_has_eaten_the_food(self.food):
                    self.food.randomize_position()
                    self.new_piece = list(self.snake.snake_pos[-1])
                    self.snake.add_piece(self.new_piece)
                    self.settings.FPS += 1
                    self.score += 1
                            
                self.display.draw_food()   
                self.snake.move()
                self.display.draw_snake_pos()                
            pygame.display.update()            
            self.clock.tick(self.settings.FPS)
   
   
if __name__ == "__main__":
    settings = GameSettings()
    game = Game(settings)
    game.run()