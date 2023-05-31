import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy(Sprite):
    
    Y_POS = 20
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    X_POS_LIST_TWO = [500, 550, 600, 700, 750, 800, 850, 900, 950, 1000]
    SPEED_Y = 5
    SPEED_X = 5
    MOV_X = {0: 'left', 1: 'right'}
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    
    def __init__(self):
        super().__init__()
        self.image = ENEMY_1
        self.image_two = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.image_two = pygame.transform.scale(self.image_two, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect_two = self.image_two.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0, 10)]
        self.rect_two.x = self.X_POS_LIST_TWO[random.randint(0, 9)]
        self.rect.y = self.Y_POS
        self.rect_two.y = self.Y_POS
        self.speed_y = self.SPEED_Y
        self.speed_x = self.SPEED_X
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.movement_x_two = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 100)
        self.move_x_for_two = random.randint(30, 100)
        self.index = 0
        self.index_two = 0

    def update(self, ships):
        self.rect.y += self.speed_y

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x

        self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def update_two(self, ships):
        self.rect_two.y += self.speed_y

        if self.movement_x_two == 'left':
            self.rect_two.x -= self.speed_x
        else:
            self.rect_two.x += self.speed_x

        self.change_movement_x_two()

        if self.rect_two.y >= SCREEN_HEIGHT:
            if self in ships:
                ships.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        screen.blit(self.image_two, (self.rect_two.x, self.rect_two.y))

    def change_movement_x(self):
        self.index += 1

        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.SHIP_WIDTH):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.index = 0

    def change_movement_x_two(self):
        self.index_two += 1

        if (self.index_two >= self.move_x_for_two and self.movement_x_two == 'right') or (self.rect_two.x >= SCREEN_WIDTH - self.SHIP_WIDTH):
            self.movement_x_two = 'left'
            self.index_two = 0
        elif (self.index_two >= self.move_x_for_two and self.movement_x_two == 'left') or (self.rect_two.x <= 10):
            self.movement_x_two = 'right'
            self.index_two = 0
