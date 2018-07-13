import pygame
from properties import *
import random

global jumping
jumping = False

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
        self.jumping = False

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

        if pygame.KEYDOWN:
            if keys[pygame.K_SPACE]:
                self.rect.y += 1
                collision = pygame.sprite.spritecollide(self, self.Game.all_platforms, False)
                self.rect.y -= 1
                if collision and not self.jumping:
                    self.jumping = True
                    self.vel_y = -JUMP
                    self.Game.jump_sound.play()


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


class PowerUp(pygame.sprite.Sprite):

    def __init__(self, Game, x, y):
        self.Game = Game
        pygame.sprite.Sprite.__init__(self)
        self.image = self.Game.spritesheet.getImage(432, 288, 70, 70)
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Enemies(pygame.sprite.Sprite):

    def __init__(self, Game, x, y):
        self.Game = Game
        pygame.sprite.Sprite.__init__(self)
        self.load_images()
        self.x = x
        self.y = y
        self.current_frame = 0
        self.last_update = 0
        self.vel_x = 0
        self.direction = random.choice(["Left", "Right"])
        self.update()

    def update(self):
        now = pygame.time.get_ticks()

        if now - self.last_update > 350:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.walking_frames_l)

            if self.direction is "Left":
                self.vel_x = -ENEMY_SPEED
                self.x += self.vel_x
                self.image = self.walking_frames_l[self.current_frame]
            else:
                self.vel_x = ENEMY_SPEED
                self.x += self.vel_x
                self.image = self.walking_frames_r[self.current_frame]

            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y

            # Enemy Collision Check with Platform
            self.rect.y += 1
            if self.direction is "Left":
                self.rect.x -= 30
                collision = pygame.sprite.spritecollide(self, self.Game.all_platforms, False)
                self.rect.x += 30
            else:
                self.rect.x += 30
                collision = pygame.sprite.spritecollide(self, self.Game.all_platforms, False)
                self.rect.x -= 30
            self.rect.y -= 1
            if not collision:
                if self.direction is "Left":
                    self.direction = "Right"
                    self.vel_x *= -1
                else:
                    self.direction = "Left"
                    self.vel_x *= -1
                self.rect.x += self.vel_x





    def load_images(self):

        self.walking_frames_l = [pygame.transform.scale(self.Game.enemy_spritesheet.getImage(52, 125, 50, 28), (30, 20)),
                                 pygame.transform.scale(self.Game.enemy_spritesheet.getImage(0, 125, 51, 26), (30, 20))]
        for frame in self.walking_frames_l:
            frame.set_colorkey(BLACK)
        self.walking_frames_r = [pygame.transform.scale(pygame.transform.flip(self.Game.enemy_spritesheet.getImage(52, 125, 50, 28), True, False), (30, 20)),
                                 pygame.transform.scale(pygame.transform.flip(self.Game.enemy_spritesheet.getImage(0, 125, 51, 26), True, False), (30, 20))]
        for frame in self.walking_frames_r:
            frame.set_colorkey(BLACK)

class SpriteSheet:

    def __init__(self, file):
        self.spritesheet = pygame.image.load(file).convert()

    def getImage(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.spritesheet, (0, 0), (x, y, w, h))
        return image

