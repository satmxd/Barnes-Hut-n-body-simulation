import math
from random import uniform
import pygame
class Point:
    cached_images = {}
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.momentum = [0,0]
        self.mass = 1
        self.size = 1
        self.quadrant = None
        self.color = (255,255,255)
        #self.update_image()

    def move(self):
        self.x += round(uniform(-2,2),3)
        self.y += round(uniform(-2,2),3)

    def update_image(self):
        cache_lookup = (self.size, self.color)

        if not (cached_image := self.cached_images.get(cache_lookup, None)):
            cached_image = pygame.Surface((2*self.size, 2* self.size))
            cached_image.fill(self.color)

            self.cached_images[cache_lookup] = cached_image

        self.image = cached_image

    def render(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.x, self.y), 1)

    def distance(self, pos):
        try:
            return math.sqrt((pos[0]-self.x)**2+(pos[1]-self.y)**2)
        except:
            pass
