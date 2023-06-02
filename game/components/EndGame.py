import pygame
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_STYLE

class EndGame:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.best_score = 0
        self.death_count = 0
        self.font = pygame.font.Font(FONT_STYLE, 30)

    def update(self, score, best_score, death_count):
        self.score, self.best_score, self.death_count = score, best_score, death_count

    def draw(self):
        self.screen.fill((255, 255, 255))

        texts = [
            (f'Your score: {self.score}', (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)),
            (f'Highest score: {self.best_score}', (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)),
            (f'Total deaths: {self.death_count}', (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        ]

        for text, pos in texts:
            text_surface = self.font.render(text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=pos)
            self.screen.blit(text_surface, text_rect)
        pygame.display.update()
