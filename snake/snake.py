import pygame
from pygame.locals import *

from game import GameDisplay

class Snake:
    def __init__(self):
        self.player = 1
        self.game_is_over = False
       
    


game = Snake()
display = GameDisplay(game)
display.run()