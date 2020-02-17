import pygame
from constants import *
from game import Game
from food import Food
from snake import Snake


def main():
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    game = Game(Snake(10, 10), Food())

    running = True
    while running:
        clock.tick(7)
        game.reset_input()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                quit()
            elif event.type == pygame.KEYUP:
                game.handle_user_input(event.key)

        game.tick()
        if game.game_over():
            pygame.quit()
            running = False
            quit()

        print(game.snake.get_snake_around())
        game.draw(win)


if __name__ == "__main__":
    main()
