import pygame
import sprite_list
from properties import *


class Game:

    def __init__(self):
        # Initialize Game
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.font_name = pygame.font.match_font(FONT)
        self.level_max = 2
        self.level = 1
        self.running = True

        self.all_sprites = pygame.sprite.Group()
        self.all_platforms = pygame.sprite.Group()
        self.all_walls = pygame.sprite.Group()
        self.all_wins = pygame.sprite.Group()



    def new(self):  # Start a new Game

        self.player = sprite_list.Player(self, *Player_Array[self.level-1])
        self.all_sprites.add(self.player)

        self.win = sprite_list.Win(*Win_Condition_Array[self.level-1])
        self.all_sprites.add(self.win)
        self.all_wins.add(self.win)

        for i in (Platforms_Array[self.level-1]):
            p = sprite_list.Platform(*i)
            self.all_sprites.add(p)
            self.all_platforms.add(p)

        for i in (Walls_Array[self.level-1]):
            p = sprite_list.Wall(*i)
            self.all_sprites.add(p)
            self.all_walls.add(p)

        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing and self.level <= self.level_max:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        self.clock.tick(FPS)

    def update(self):
        self.all_sprites.update()
        collision = pygame.sprite.spritecollide(self.player, self.all_platforms, False)
        if collision:
            if self.player.vel_y > 0:
                self.player.rect.y = collision[0].rect.top - 1 - 30
                self.player.vel_y = 0
            elif self.player.vel_y < 0:
                self.player.rect.y = collision[0].rect.bottom + 1
                self.player.vel_y = 0

        wall_collision = pygame.sprite.spritecollide(self.player, self.all_walls, False)
        if wall_collision:
            if self.player.vel_x > 0:
                self.player.rect.right = wall_collision[0].rect.left
            else:
                self.player.rect.left = wall_collision[0].rect.right

        # Game Over
        if self.player.rect.top > HEIGHT:
            self.kill()
            self.playing = False

        win_collision = pygame.sprite.spritecollide(self.player, self.all_wins, False)
        if win_collision:
            self.level += 1
            if self.level > self.level_max:
                self.playing = False
            else:
                self.kill()
                self.new()

    def events(self):

        # Process Input (Events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def draw(self):

        # Draw/Render
        self.window.fill(TURQUOISE)
        self.all_sprites.draw(self.window)
        self.all_platforms.draw(self.window)
        self.all_walls.draw(self.window)
        self.all_wins.draw(self.window)

        self.text("Level "+str(self.level), 22, BLACK, WIDTH/2, 15)
        # Always do this last after drawing everything
        pygame.display.update()

    def kill(self): # Kill the Platforms/Walls/Win Condition
        self.all_platforms.empty()
        self.all_platforms.add()
        self.all_walls.empty()
        self.all_walls.add()
        self.all_sprites.empty()
        self.all_sprites.add()
        self.win.kill()
        self.player.kill()

    def show_start_screen(self):
        self.window.fill(WHITE)
        self.text("Welcome to "+TITLE, 50, BLACK, WIDTH/2, HEIGHT/4)
        self.text("Arrow Keys = Move", 20, BLACK, WIDTH/2, HEIGHT/2 + 50)
        self.text("Space Bar = Jump", 20, BLACK, WIDTH/2, HEIGHT/2 + 100)
        self.text("Press any Key to Start", 20, BLACK, WIDTH/2, HEIGHT/2 + 200)
        pygame.display.update()
        self.wait()

    def win_screen(self):
        if not self.running:
            return
        self.window.fill(WHITE)
        self.text("You Beat the Game. \(^.^)/", 50, BLACK, WIDTH / 2, 200)
        self.text("Press any Key to Exit", 20, BLACK, WIDTH / 2, HEIGHT / 2 + 50)
        pygame.display.update()
        self.wait()
        self.running = False

    def gameover_screen(self):
        if not self.running:
            return
        self.window.fill(WHITE)
        self.text("Rest in Peace Blocky", 50, BLACK, WIDTH / 2, 200)
        self.text("You have reached Level " + str(self.level), 20, BLACK, WIDTH / 2, HEIGHT / 2)
        self.text("Press any Key to Try Again", 20, BLACK, WIDTH / 2, HEIGHT / 2 + 50)
        self.level = 1
        pygame.display.update()
        self.wait()

    def wait(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    waiting = False

    def text(self, message, size, color, x, y):
        font =  pygame.font.Font(self.font_name, size)
        text_surface = font.render(message, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.window.blit(text_surface, text_rect)



start = Game()
start.show_start_screen()
while start.running:
    start.new()
    if start.level > start.level_max:
        start.win_screen()
    else:
        start.gameover_screen()
pygame.quit()
quit()
