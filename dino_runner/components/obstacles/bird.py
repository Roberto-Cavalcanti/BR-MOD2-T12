import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD_Y_POS

class Bird(Obstacle):
    def __init__(self, images):
        self.type = random.randint(0, 1)
        super().__init__(images, self.type)

        self.rect.y = BIRD_Y_POS