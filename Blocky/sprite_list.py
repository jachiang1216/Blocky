import pygame
from properties import *

# Sprite Classes

class Player(pygame.sprite.Sprite):

    def __init__(self, Game, x, y):
        self.Game = Game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.acc_x = 0
        self.gravity = 1

    def update(self):

        self.acc_x = 0

        # Wall BOundaries
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= WIDTH - 30:
            self.rect.x = WIDTH - 30

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc_x = -ACC
        elif keys[pygame.K_RIGHT]:
            self.acc_x = ACC

        if keys[pygame.K_SPACE]:
            self.rect.y += 1
            collision = pygame.sprite.spritecollide(self, self.Game.all_platforms, False)
            self.rect.y -= 1
            if collision:
                self.vel_y = -JUMP

        self.acc_x += self.vel_x * FRICTION
        self.vel_x += self.acc_x
        self.rect.x += self.vel_x + 0.5 * self.acc_x

        self.vel_y += self.gravity
        self.rect.y += self.vel_y + 0.5 * self.gravity



class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Wall(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Win(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
