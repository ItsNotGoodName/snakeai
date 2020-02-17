import pygame
from constants import *


class Game:
    """
        0 = wall/body
        2 = snake-head
        3 = nothing
        4 = food
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

    def game_over(self):
        return self.snake.is_dead()

    def update_board(self):
        self.snake.update_board(self.board)

    def tick(self):
        self.snake.tick()
        if self.food.collide(self.snake):
            self.snake.grow()
            self.snake.eat()
            self.food.move_random()

    def draw(self, win):
        win.fill([255, 255, 255])
        self.snake.draw(win)
        self.food.draw(win)
        pygame.display.update()

    # Rest key presses
    # ------------------------------------------------------------------------------------------------------------------
    def reset_input(self):
        self.left = False
        self.right = False

    # Key press handling
    # ------------------------------------------------------------------------------------------------------------------
    def handle_user_input(self, key):
        if key == pygame.K_LEFT and self.left is False:
            self.snake.move_left()
            self.left = True
        elif key == pygame.K_RIGHT and self.right is False:
            self.snake.move_right()
            self.right = True
    # Key press handling
    # ------------------------------------------------------------------------------------------------------------------
    def snake_key_check(self):
        if self.left:
            self.snake.move_left()
            self.left = False
        if self.right:
            self.snake.move_right()
            self.right = False
    # ------------------------------------------------------------------------------------------------------------------
