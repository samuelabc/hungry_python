import pygame
import random


class Food:
    def __init__(self, snake_game):
        self.screen = snake_game.screen
        self.settings = snake_game.settings
        self.x = random.randint(0, (self.settings.screen_width - self.settings.cube_length) / 20) * 20
        self.y = random.randint(0, (self.settings.screen_height - self.settings.cube_length) / 20) * 20
        self.rect = pygame.Rect(self.x, self.y,
                                self.settings.food_cube_length,
                                self.settings.food_cube_length)

    def update(self):
        self.x = random.randint(0, (self.settings.screen_width - self.settings.cube_length)/20) * 20
        self.y = random.randint(0, (self.settings.screen_height - self.settings.cube_length)/20) * 20
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.settings.food_color,
            self.rect
        )
