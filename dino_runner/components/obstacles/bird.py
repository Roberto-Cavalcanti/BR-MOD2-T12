import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD_Y_POS

class Bird(Obstacle):
    def __init__(self, images, type):
        super().__init__(images, type)
        if type == 0:
            self.rect.y = BIRD_Y_POS
        else:
            self.rect.y = BIRD_Y_POS + 50
    
    def fly(self):
        pass