import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_TYPE,SOUND
from game.components.bullets.bullet import Bullet
from game.components.bullets.bullet_manager import BulletManager
from game.components.counter import Counter
from game.utils.constants import HEART


class Spaceship(Sprite):
 
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH //2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10
    ROTATION_SPEED = 5
    MAX_LIFE = 5


    def __init__(self,bullet_manager):
            self.image = SPACESHIP
            self.image = pygame.transform.scale(self.image,(40,60))
            self.rect = self.image.get_rect()
            self.rect.x = self.X_POS
            self.rect.y  = self.Y_POS
            self.type = 'player'
            self.bullet_manager = bullet_manager
            self.power_up_type = DEFAULT_TYPE
            self.has_power_up = False
            self.power_time_up = 0
            self.life = 3
            self.heart_image = pygame.transform.scale(HEART, (30, 30))
           
            self.increment_counter = Counter()
            self.game_over = False
            
            
    
    def update(self, user_input,game):
        
        if user_input[pygame.K_LEFT] and user_input[pygame.K_SPACE]: 
            self.move_left()
            self.shoot(game)
        if user_input[pygame.K_RIGHT] and user_input[pygame.K_SPACE]:
            self.move_right()
            self.shoot(game)
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
        

        self.check_bullet_collision(game)

    
        

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
     
      self.draw_hearts(screen)

     

    def shoot(self, game):
            bullet = Bullet(self)  
            game.bullet_manager.add_bullet(bullet)  
            SOUND["shoothing"].set_volume(0.02)
            SOUND["shoothing"].play()


    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.life = 3


    def set_image(self,size = (SHIP_WIDTH, SHIP_HEIGHT), image = SPACESHIP):
        self.image =  image
        self.image = pygame.transform.scale(self.image, size)

    def increment_life(self):
        if self.life <= self.MAX_LIFE:
            self.life += 1
        

    def check_bullet_collision(self, game):
        for bullet in game.bullet_manager.enemy_bullets:
            if bullet.rect.colliderect(self.rect) and bullet.rect.bottom > self.rect.centery:
                self.decrement_life()
                game.bullet_manager.enemy_bullets.remove(bullet)
                


    def decrement_life(self):
        self.life -= 1
        if self.life == 0:
            self.game_over = True


    def draw_hearts(self, screen):
        heart_size = self.heart_image.get_size()
        for i in range(self.life):
            heart_x = i * (heart_size[0] + 10)
            heart_y = 0
            screen.blit(self.heart_image, (heart_x, heart_y))
