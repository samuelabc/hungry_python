import sys
import pygame
import time

from settings import Settings
from snake import Snake
from stats import Stats
from food import Food
from button import Button


class SnakeGame:
    def __init__(self):
        print(pygame.font.get_fonts())
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Hungry Python')

        self.stats = Stats(self)

        self.snakes = []
        self.direction = ["LEFT", "RIGHT", "UP", "DOWN"]
        self.food = Food(self)
        self.score = 0

        self._init_game()

        self.lose_button = Button(self, "You Lose!", 300, 250)
        self.restart_button = Button(self, "Click on spacebar or here to proceed", 300, 350, 30)
        self.highscore_button = Button(self, f"Highscore : {self.stats.highscore}", 480, 50, 30)
        self.score_button = Button(self, f"Score : {self.score}", 480, 50, 20)

    def _init_game(self):
        self.snakes = []
        self.snakes.append(
            Snake(self,
                  self.settings.snake_initial_x,
                  self.settings.snake_initial_y
                  )
        )
        self.snakes.append(Snake(self, 280, 300))
        self.snakes.append(Snake(self, 260, 300))

        self.moving_direction = self.direction[1]

        self.food.update()

        self.score = 0

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self._update_snakes()
                self._check_collision()
                time.sleep(self.settings.sleep_length)
            self._update_screen()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for snake in self.snakes:
            snake.draw()
        self.food.draw()
        self.score_button.draw_button()
        if not self.stats.game_active:
            self.lose_button.draw_button()
            self.restart_button.draw_button()
            self.highscore_button.draw_button()
        pygame.display.flip()

    def _update_snakes(self, update_type="uncollided"):
        head_x = self.snakes[0].x
        head_y = self.snakes[0].y
        offset = self.settings.snake_speed

        if self.moving_direction == self.direction[0]:
            head_x -= offset
        elif self.moving_direction == self.direction[1]:
            head_x += offset
        elif self.moving_direction == self.direction[2]:
            head_y -= offset
        elif self.moving_direction == self.direction[3]:
            head_y += offset
        self.snakes.insert(0, Snake(self, head_x, head_y))
        if update_type == "uncollided":
            self.snakes.pop(-1)

    def _check_collision(self):
        if pygame.Rect.colliderect(self.snakes[0].rect, self.food.rect):
            self._update_snakes("collided")
            self.food = Food(self)
            self.score += self.settings.points
            self.score_button.update_text(f"Score : {self.score}")

        for a in range(0, len(self.snakes) - 1):
            for b in range(a + 1, len(self.snakes)):
                if pygame.Rect.colliderect(self.snakes[a].rect, self.snakes[b].rect):
                    self._lose()
        x = self.snakes[0].x
        y = self.snakes[0].y
        offset = self.settings.cube_length
        if x < 0 or x + offset > self.settings.screen_width:
            self._lose()
        elif y < 0 or y + offset > self.settings.screen_height:
            self._lose()

    def _lose(self):
        self.stats.game_active = False
        self.stats.update_highscore(self.score)
        self.highscore_button.update_text(f"Highscore : {self.stats.highscore}")
        self._init_game()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_button_mouse(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_LEFT and not self.moving_direction == self.direction[1]:
            self.moving_direction = self.direction[0]
        elif event.key == pygame.K_RIGHT and not self.moving_direction == self.direction[0]:
            self.moving_direction = self.direction[1]
        elif event.key == pygame.K_UP and not self.moving_direction == self.direction[3]:
            self.moving_direction = self.direction[2]
        elif event.key == pygame.K_DOWN and not self.moving_direction == self.direction[2]:
            self.moving_direction = self.direction[3]
        elif event.key == pygame.K_SPACE:
            if not self.stats.game_active:
                self.stats.game_active = True

    def _check_button_mouse(self, mouse_pos):
        button_clicked = self.restart_button.text_rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.game_active = True


if __name__ == '__main__':
    sg = SnakeGame()
    sg.run_game()
