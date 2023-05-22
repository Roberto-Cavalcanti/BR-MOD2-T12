import random

from dino_runner.components.obstacles.obstacle import Obstacle
# from dino_runner.utils.constants import SMALL_CACTUS_Y_POS, LARGE_CACTUS_Y_POS

class Cactus(Obstacle):
    def __init__(self, images, Y, type): # Posso criar um parâmetro para substituir o random e adicionar todas as opções em lista.
        self.type = type    #random.randint(0, 2)
        super().__init__(images, self.type)

        self.rect.y = Y