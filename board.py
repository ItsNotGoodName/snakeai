import pygame
from constants import *


class Board:
    """
        0 = nothing
        1 = snake-head
        2 = snake-body
        3 = food
    """

    def __init__(self, snake, food):
        self.board = []
        for _ in range(Y_GRID_SIZE):
            row = []
            for _ in range(X_GRID_SIZE):
                row.append(0)
            self.board.append(row)
        self.snake = snake
        self.food = food
        # Key bindings
        # --------------------------------------------------------------------------------------------------------------
        self.left = False
        self.right = False
        # --------------------------------------------------------------------------------------------------------------

    def update_board(self):
        self.snake.update_board(self.board)

    def tick(self):
        # Key checking
        # --------------------------------------------------------------------------------------------------------------
        if self.left:
            self.snake.move_left()
            self.left = False
        if self.right:
            self.snake.move_right()
            self.right = False
        # --------------------------------------------------------------------------------------------------------------
        self.snake.tick()
        if self.food.collide(self.snake):
            self.snake.grow()
            self.food.move_random()

    def draw(self, win):
        win.fill([255, 255, 255])
        self.snake.draw(win)
        self.food.draw(win)
        pygame.display.update()

    # Key press handling
    # ------------------------------------------------------------------------------------------------------------------
    def handle_user_input(self, key):
        if key == pygame.K_LEFT:
            self.left = True
        elif key == pygame.K_RIGHT:
            self.right = True
