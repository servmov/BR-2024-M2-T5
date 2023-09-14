import random

from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):
    def __init__(self, images):
        index = random.randint(0, 1)
        image = images[index]
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)

        self.rect.y = 325 if index == 0 else 300
