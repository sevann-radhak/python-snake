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
        self.play_again_rect = pygame.Rect(self.screen_height / 2 - 50, self.screen_width / 2, 250, 50)
        self.snake = Snake(self.screen_width, self.screen_height, self.cell_size)
        self.display = GameDisplay(self.screen_width, self.screen_height, self.cell_size, self.colors, self.snake, self.food, self.play_again_rect)
        self.snake.create()
        self.clock = pygame.time.Clock()
        self.FPS = 10
        self.score = 0
        self.game_is_over = False
        
    def check_if_game_is_over(self):
        if self.snake.snake_pos[0][0] >= self.screen_width or self.snake.snake_pos[0][0] < 0:
            return True
        elif self.snake.snake_pos[0][1] >= self.screen_height or self.snake.snake_pos[0][1] < 0:
            return True
        for block in self.snake.snake_pos[1:]:
            if self.snake.snake_pos[0] == block:
                return True
        return False
       
       
    def run(self):
        self.snake.create()
        clicked = False
        while True:   
            self.display.draw_screen() 
            self.display.draw_score(self.score) 
            
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
                                self.snake = Snake(self.screen_width, self.screen_height, self.cell_size)
                                self.food = Food(self.screen_width, self.screen_height, self.cell_size)
                                self.display = GameDisplay(self.screen_width, self.screen_height, self.cell_size, self.colors, self.snake, self.food, self.play_again_rect)
                                self.snake.create()
                                self.score = 0
            else: 
                self.display.draw_food()
                
                if self.snake.check_if_snake_has_eaten_the_food(self.food):
                    self.food.randomize_position()
                    self.new_piece = list(self.snake.snake_pos[-1])
                    self.snake.add_piece(self.new_piece)
                    self.score += 1
                            
                self.display.draw_food()   
                self.snake.move()
                    
                self.display.draw_snake_pos()                
            pygame.display.update()            
            self.clock.tick(self.FPS)
   
   
if __name__ == "__main__":
    game = Game()
    game.run()