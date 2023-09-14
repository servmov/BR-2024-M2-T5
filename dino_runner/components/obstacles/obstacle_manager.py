import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.start_time = pygame.time.get_ticks()  # para registrar o tempo inicial do jogo

    def update(self, game):
        current_time = pygame.time.get_ticks()  # para obter o tempo atual do jogo

        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus([SMALL_CACTUS, LARGE_CACTUS]))


            if current_time - self.start_time > 5000: # Timer para aparecimento do passaro
                self.obstacles.append(Bird())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)