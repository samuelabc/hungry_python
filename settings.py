import random
import pygame


class Settings:
    def __init__(self):
        self.sleep_length = 0.1
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        self.cube_length = 20

        self.snake_initial_x = self.screen_width / 2
        self.snake_initial_y = self.screen_height / 2
        self.snake_cube_length = self.cube_length
        self.snake_color = (230, 230, 230)
        self.snake_speed = self.cube_length

        self.food_color = (130, 130, 130)
        self.food_cube_length = self.cube_length

        self.points = 10
