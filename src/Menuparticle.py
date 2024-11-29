from random import randint, uniform, randrange
import pygame
from math import sqrt
class Particle(pygame.sprite.Sprite):
    def __init__(self,
                 groups: pygame.sprite.Group,
                 pos: list[int],
                 color: str,
                 direction: pygame.math.Vector2,
                 speed: int):
        super().__init__(groups)
        self.pos = pos
        self.color = color
        self.direction = direction
        self.ogdir = direction
        self.speed = speed
        self.alpha = randint(10,200)
        self.fade_speed = 200
        self.size = randrange(1,5)

        self.create_surf()

    def create_surf(self):
        # self.image = pygame.Surface((self.size, self.size)).convert_alpha()
        self.image = pygame.image.load('data\\imgs\\sprite.png').convert_alpha()
        self.image.set_alpha(self.alpha)
        self.image.set_colorkey("black")
        #pygame.draw.circle(surface=self.image, color=self.color, center=(self.size / 2, self.size / 2), radius=self.size / 2)
        self.rect = self.image.get_rect(center=self.pos)

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos
    def changedir(self,x,y):
        if sqrt((self.pos[0]-x)**2+(self.pos[1]-y)**2) < 80:
            self.direction = 4*((pygame.math.Vector2(self.pos[0]-x,self.pos[1]-y)).normalize())
        else:
            self.direction = self.ogdir
    def fade(self, dt):
        self.alpha -= self.fade_speed * dt
        self.image.set_alpha(self.alpha)

    def check_pos(self):
        if (
            self.pos[0] < -50 or
            self.pos[0] > 1200 + 50 or
            self.pos[1] < -50 or
            self.pos[1] > 800 + 50
        ):
            self.kill()

    def check_alpha(self):
        if self.alpha <= 0:
            self.kill()

    def update(self, dt,x,y):
        self.move(dt)
        self.changedir(x,y)
        #self.fade(dt)
        self.check_pos()
        self.check_alpha()
