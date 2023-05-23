import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS, LARGE_CACTUS_Y_POS, SMALL_CACTUS_Y_POS

list_obs = [
Cactus(SMALL_CACTUS, SMALL_CACTUS_Y_POS, 0),
Cactus(SMALL_CACTUS, SMALL_CACTUS_Y_POS, 1),
Cactus(SMALL_CACTUS, SMALL_CACTUS_Y_POS, 2),
Cactus(LARGE_CACTUS,LARGE_CACTUS_Y_POS, 0), 
Cactus(LARGE_CACTUS,LARGE_CACTUS_Y_POS, 1), 
Cactus(LARGE_CACTUS,LARGE_CACTUS_Y_POS, 2), 
Bird(BIRD, 0),
Bird(BIRD, 1),
]

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            random_obs = random.randint(0,7)
            self.obstacles.append(list_obs[random_obs])

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles.clear()