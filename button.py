import pygame


class Button:
    def __init__(self, snake_game, text, x=300, y=300, font_size=30):
        self.settings = snake_game.settings
        self.screen = snake_game.screen
        self.button_color = (0, 0, 0)  # white
        self.text_color = (255, 255, 255)  # black
        self.text_font = pygame.font.SysFont('calibri', font_size)

        self.text_surface = self.text_font.render(text, True, self.button_color, self.text_color)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (x, y)

    def draw_button(self):
        self.screen.fill(self.button_color, self.text_rect)
        self.screen.blit(self.text_surface, self.text_rect)

    def update_text(self, text):
        self.text_surface = self.text_font.render(text, True, self.button_color, self.text_color)
