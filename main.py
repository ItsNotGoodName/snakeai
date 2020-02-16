import pygame
from constants import *
from board import Board
from food import Food
from snake import Snake


def main():
    win=pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    snake = Snake(10, 10)
    food = Food()
    board = Board(snake, food)

    running = True
    while running:
        clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                quit()
            elif event.type == pygame.KEYUP:
                board.handle_user_input(event.key)

        board.tick()

        if board.snake.is_dead():
            pygame.quit()
            running = False
            quit()

        board.draw(win)

if __name__ == "__main__":
    main()