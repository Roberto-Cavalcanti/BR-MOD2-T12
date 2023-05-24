import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, SMALL_CACTUS_Y_POS, LARGE_CACTUS, LARGE_CACTUS_Y_POS, BIRD, DINO_DEAD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        random_obs = random.randint(0,2)
        if len(self.obstacles) == 0:
            if random_obs == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS, SMALL_CACTUS_Y_POS))
            elif random_obs == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS, LARGE_CACTUS_Y_POS))
            elif random_obs == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                game.player.dino_run = False
                game.player.image = DINO_DEAD
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles.clear()