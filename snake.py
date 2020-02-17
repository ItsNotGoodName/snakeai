import pygame

from constants import *


class Snake:
    MOVE_MATRIX = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    MOVE_MATRIX_LEN = len(MOVE_MATRIX)

    def __init__(self, x: object, y: object) -> object:
        self.body = []
        self.hunger = 200
        # Start snake with 4 body parts
        for i in reversed(range(1,5)):
            self.body.append((x, y+i))
        self.olddist = 10000
        self.new_body = False
        self.x = x
        self.y = y
        self.move_ind = 0

    def grow(self):
        self.new_body = True

    def tick(self):
        if self.new_body:
            self.body.append((self.x, self.y))
            self.new_body = False
        else:
            self.body.append((self.x, self.y))
            self.body.pop(0)

        x_vel, y_vel = self.MOVE_MATRIX[self.move_ind]

        self.x += x_vel
        self.y += y_vel
        self.hunger -= 1

    def eat(self):
        self.hunger += 50

    def update_board(self, board):
        for b in self.body:
            x, y = b
            board[y][x] = SNAKE_BODY_NUM
        board[y][x] = SNAKE_HEAD_NUM

    def move_left(self):
        self.move_ind = (self.move_ind - 1) % self.MOVE_MATRIX_LEN

    def move_right(self):
        self.move_ind = (self.move_ind + 1) % self.MOVE_MATRIX_LEN

    def is_dead(self):
        if self.hunger < 0 or (self.x, self.y) in self.body or self.x >= NUM_X_GRID or self.x < 0 or self.y >= NUM_Y_GRID or self.y < 0:
            return True
        return False

    def draw(self, win):
        for b in self.body:
            x, y = b
            pygame.draw.rect(win, [0, 0, 0], (x * X_GRID_SIZE, y * Y_GRID_SIZE, X_GRID_SIZE, Y_GRID_SIZE))
        pygame.draw.rect(win, [128,128, 128], (self.x * X_GRID_SIZE, self.y * Y_GRID_SIZE, X_GRID_SIZE, Y_GRID_SIZE))

    def get_snake_around(self):
        ret = []
        for xi, yi in self.MOVE_MATRIX:
            if self.x + xi < 0 or self.x + xi >= NUM_X_GRID or self.y + yi < 0 or self.y + yi >= NUM_Y_GRID or (self.x+xi, self.y+yi) in self.body:
                ret.append(WALL_NUM)
            else:
                ret.append(NOTHING_NUM)

        left = ret[(self.move_ind - 1) % self.MOVE_MATRIX_LEN]
        right = ret[(self.move_ind + 1) % self.MOVE_MATRIX_LEN]
        straight = ret[self.move_ind]

        return (left, straight, right)


