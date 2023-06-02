import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT
from game.components.bullets.bullet import Bullet
from game.components.bullets.bullet_manager import BulletManager


class Spaceship(Sprite):
 
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH //2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10
    ROTATION_SPEED = 5


    def __init__(self,bullet_manager):
            self.image = SPACESHIP
            self.image = pygame.transform.scale(self.image,(40,60))
            self.rect = self.image.get_rect()
            self.rect.x = self.X_POS
            self.rect.y  = self.Y_POS
            self.type = 'player'
            self.bullet_manager = bullet_manager
            
    
    def update(self, user_input,game):
      if user_input[pygame.K_LEFT]:
        self.move_left()
      elif user_input[pygame.K_RIGHT]:
          self.move_right()
      elif user_input[pygame.K_UP]:
          self.move_up()
      elif user_input[pygame.K_DOWN]:
          self.move_down()
      elif user_input[pygame.K_SPACE]:
          self.shoot(game)

    
        

    def move_left(self):
         
         self.rect.x -= self.SHIP_SPEED
         if self.rect.left <0:
            self.rect.x = SCREEN_WIDTH -self.SHIP_WIDTH

    
   
    def move_right(self):
         self.rect.x += self.SHIP_SPEED
         if self.rect.left >= SCREEN_WIDTH -self.SHIP_HEIGHT:
            self.rect.x = 0

    
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT //2:
            self.rect.y -=  self.SHIP_SPEED


    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - self.rect.height:
            self.rect.y += self.SHIP_SPEED
          


    def draw(self,screen):
      screen.blit(self.image,(self.rect.x, self.rect.y))

    def shoot(self, game):
            bullet = Bullet(self)  
            game.bullet_manager.add_bullet(bullet)  

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS


                