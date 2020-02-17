import math
import os

import neat
import pygame

from constants import *
from food import Food
from snake import Snake


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def neat_main(genomes, config):
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    nets = []
    snakes = []
    foods = []
    ge = []
    for genome_id, genome in genomes:
        genome.fitness = 0  # start with fitness level of 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        snakes.append(Snake(3,3))
        foods.append(Food(15, 15))
        ge.append(genome)

    running = True
    while running and len(snakes) > 0:
        clock.tick(1000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                quit()

        for x, snake in enumerate(snakes):  # give each bird a fitness of 0.1 for each frame it stays alive
            snake.tick()
            angle = math.atan2(snake.y - foods[x].y, snake.x - foods[x].x )
            dist = distance((foods[x].x, foods[x].y), (snake.x, snake.y))

            if dist < snake.olddist:
                ge[x].fitness += 0.1
                snake.olddist = dist

            output = nets[snakes.index(snake)].activate(snake.get_snake_around() + (angle,dist))
            maxind = np.argmax(output)

            if maxind == 0:
                snake.move_left()
            if maxind == 1:
                snake.move_right()

        for snake in snakes:
            snindex = snakes.index(snake)
            if snake.is_dead():
                ge[snindex].fitness -= 1
                nets.pop(snindex)
                ge.pop(snindex)
                snakes.pop(snindex)
                foods.pop(snindex)
            elif foods[snindex].collide(snake):
                ge[snindex].fitness +=5
                snake.eat()
                snake.grow()
                foods[snindex].move_random()
                snake.olddist = 10000

        win.fill([255, 255, 255])
        for x, snake in enumerate(snakes):
            snake.draw(win)
            foods[x].draw(win)
        pygame.display.update()


def neat_run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)

    p = neat.Population(config)
    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    #p.add_reporter(neat.Checkpointer(5))

    # Run for up to 50 generations.
    winner = p.run(neat_main, 2000)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'neat.txt')
    neat_run(config_path)
