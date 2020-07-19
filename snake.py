import pygame
import random


class Snake:
    def __init__(self, snake_game, init_x, init_y):
        self.screen = snake_game.screen
        self.settings = snake_game.settings

        self.x = init_x
        self.y = init_y

        self.rect = pygame.Rect(self.x, self.y,
                                self.settings.snake_cube_length,
                                self.settings.snake_cube_length)

    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.settings.snake_color,
            self.rect
        )
        # print(self.rect)
