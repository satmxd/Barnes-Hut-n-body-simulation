import math
from random import uniform
import pygame
from config import *
pygame.font.init()
font = pygame.font.SysFont('Monospace', 12)

class Point:
    cached_images = {}
    def __init__(self, x, y, m = 1, s = 1):
        self.x = x
        self.y = y
        self.momentum = [0,0]
        self.mass = m
        self.size = self.mass
        self.quadrant = None
        self.colordensity = None
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

    def render(self, screen, show_col = False):
        if show_col:
            self.colordensity = min(int(self.quadrant.mass * 50 // (self.quadrant.boundary.w * 2)), 100)
            colorindex = round(11 * math.log10(self.colordensity + 0.446) + 4, 4)
            colorindex = (11 * math.log10(self.colordensity + 0.446) + 4)
            pygame.draw.circle(screen, pygame.Color(colorrange[int(colorindex)]), (self.x, self.y), self.size)
        else:
            #cdf = font.render((str(self.colordensity)), 1, (0,255,0))
            pygame.draw.circle(screen, (255,255,255), (self.x, self.y), self.size)

            #screen.blit(cdf, (self.x, self.y+5))

    def distance(self, pos):
        try:
            return math.sqrt((pos[0]-self.x)**2+(pos[1]-self.y)**2)
        except:
            pass
