from constants import *
import random
import pygame


class Food:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.move_random()

    def move_random(self):
        self.x = random.randrange(NUM_X_GRID)
        self.y = random.randrange(NUM_Y_GRID)

    def draw(self, win):
        pygame.draw.rect(win, [0, 255, 0], (self.x * X_GRID_SIZE, self.y * Y_GRID_SIZE, X_GRID_SIZE, Y_GRID_SIZE))

    def collide(self, snake):
        if snake.x == self.x and snake.y == self.y:
            return True
        return False
