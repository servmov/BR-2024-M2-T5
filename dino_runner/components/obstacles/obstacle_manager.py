import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import HAMMER_TYPE, RESET_SPEED_TYPE, DEATH_SOUND


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        obstacle_type = [
            Cactus(),
            Bird(),
        ]

        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0, 1)])

        for obstacle in self.obstacles:
            print("type", game.player.type)
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    self.death_play()
                    pygame.time.delay(2000)
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    if game.player.type == HAMMER_TYPE:
                        self.obstacles.remove(obstacle)
                    elif game.player.type == RESET_SPEED_TYPE:
                        game.game_speed = 20
                        pygame.time.delay(2000)
                        game.playing = False
                        game.death_count += 1
                        self.death_play()

    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def death_play(self):
        pygame.mixer.music.load(DEATH_SOUND)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume == 60 