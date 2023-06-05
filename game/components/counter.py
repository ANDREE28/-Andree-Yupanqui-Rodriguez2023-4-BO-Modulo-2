import pygame
from game.utils.constants import FONT_STYLE
class Counter:
    def __init__(self):
        self.count = 0
        self.increment_count = 0
        self.font = pygame.font.Font(None, 36)
        

    def update(self):
        self.count += 1
        

        
    def draw(self, screen):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score:{self.count}',True,(255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (1000,50)
        screen.blit(text,text_rect)

    def reset(self):
        self.count = 0

    def set_count(self, value):
        self.count = value

    def set_increment_count(self, count):
        self.increment_count = count

    def draw_increment(self, screen, x, y):
        if self.increment_count > 0:
            text = self.font.render(f"+{self.increment_count} Life!", True, (0, 255, 0))
            screen.blit(text, (x, y))

    
        