import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
# from dino_runner.components.power_ups import power_up,hammer,shield
from dino_runner.utils.constants import SMALL_CACTUS, SMALL_CACTUS_Y_POS, LARGE_CACTUS, LARGE_CACTUS_Y_POS, BIRD, HAMMER_TYPE, SHIELD_TYPE

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
                if (game.player.type == SHIELD_TYPE and not random_obs == 2) or (game.player.type == HAMMER_TYPE and random_obs == 2)  or not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    # print(game.player.type)
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles.clear()