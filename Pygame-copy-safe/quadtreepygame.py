import math
from config import *

import pygame
from Particle import Point
pygame.font.init()
font = pygame.font.SysFont('Monospace', 12)
class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w  # Distance from center to boundary - Actual width/2
        self.h = h


    def contains(self, point):
        return (point.x >= self.x-self.w and point.x < self.x + self.w and point.y >= self.y - self.h and point.y < self.y + self.h)  # Check if Rectangle contains point

    def intersects(self, range):
        return not(range.x - range.w > self.x + self.w or
                   range.x + range.w < self.x - self.w or
                   range.y - range.h > self.y + self.h or
                   range.y + range.h < self.y - self.h)
    # def draw(self, canvas, depth, mass, com):
    #     canvas.create_rectangle(self.x-self.w,self.y-self.h, self.x+self.w, self.y+self.h, outline = 'white' , width = 1)
    #     canvas.create_text(self.x-20, self.y, text = depth, fill = 'white', tag = 'e')
    #     canvas.create_text(self.x+20, self.y, text = mass, fill = 'white', tag = 'e')
    #     if not com[0] == 0 and not com[1] == 0:
    #         canvas.create_oval(com[0], com[1],com[0] +  max(0, 40-5*len(depth)),com[1] +  max(0, 40-5*len(depth)), fill='yellow', tag = 'e')
    #         canvas.create_text(com[0], com[1]+45, text=com, fill='white', tag = 'e')
    #         canvas.create_text(com[0], com[1]+30, text=depth, fill='white', tag = 'e')
    def draw(self, screen,  mass, com):
        #pass
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x-self.w, self.y-self.h, self.w*2, self.h*2), 1)
        #mass_text = font.render(str(mass), False, (255,255,255))
        #screen.blit(mass_text, (self.x, self.y))
        try:
            pygame.draw.circle(screen, (255,0,0), (com[0], com[1]), 4)
        except:
            pass

class QuadTree:
    def __init__(self, boundary, n, depth):
        self.boundary = boundary  # Rectangle
        self.capacity = n
        self.points_ = []
        self.subdivided = False
        self.children = []
        self.depth = depth
        self.com = (None, None)
        self.mass = 0


    @property
    def points(self):
        return self.points_
    @points.setter
    def points(self, updated_points):
        self.points_ = updated_points
        self.mainloop()

    def subdivide(self):

        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w
        h = self.boundary.h
        # Create 4 quadrants which QuadTree divides into
        tr = Rectangle(x + w/2, y - h/2, w/2, h/2)
        tl = Rectangle(x - w/2, y - h/2, w/2, h/2)
        bl = Rectangle(x - w / 2, y + h / 2, w / 2, h / 2)
        br = Rectangle(x + w / 2, y + h / 2, w / 2, h / 2)
        # Define each quadrant as another QuadTree
        self.topright = QuadTree(tr, self.capacity, self.depth+'B')
        self.topleft = QuadTree(tl, self.capacity, self.depth+'A')
        self.bottomleft = QuadTree(bl, self.capacity, self.depth+'C')
        self.bottomright = QuadTree(br, self.capacity, self.depth+'D')
        self.children = [self.topright, self.topleft, self.bottomright, self.bottomleft]
        nodes.append(self.topright)
        nodes.append(self.topleft)
        nodes.append(self.bottomright)
        nodes.append(self.bottomleft)
        #print('nodes extended')
        for i in range(len(self.points)):
            self.topright.insert(self.points[i])
            self.topleft.insert(self.points[i])
            self.bottomleft.insert(self.points[i])
            self.bottomright.insert(self.points[i])
        self.subdivided = True


    def insert(self, point):
        if not self.boundary.contains(point):
            return False

        if len(self.points) < self.capacity:
            point.quadrant = self
            self.points += [point]

            return True
        else:
            if not self.subdivided:
                self.subdivide()

            return (self.topright.insert(point) or
                    self.topleft.insert(point) or
                    self.bottomright.insert(point) or
                    self.bottomleft.insert(point))

    def query(self, range, found_points):
        if not self.boundary.intersects(range):
            return
        for point in self.points:
            if range.contains(point):
                found_points.append(point)

        if self.subdivided:
            self.topright.query(range, found_points)
            self.topleft.query(range, found_points)
            self.bottomright.query(range, found_points)
            self.bottomleft.query(range, found_points)
        return found_points

    #Must be called in order to return value of self.mass, else self.mass will be = 0
    def calculate_mass(self):
        self.mass = len(self.points)
        if self.subdivided:
            self.mass = self.topright.calculate_mass()+self.topleft.calculate_mass()+self.bottomright.calculate_mass()+self.bottomleft.calculate_mass()
        if not self.mass == 0:
            return self.mass
        else:
            return 0

    def calculate_com(self):
        comx = comy = 0
        for point in self.points:
            comx += point.x * point.mass
            comy += point.y * point.mass
        if not self.mass == 0:
            self.com = (comx//self.mass, comy//self.mass)
            if self.subdivided:
                # tr = self.topright.com = self.topright.calculate_com()
                # tl = self.topleft.com = self.topleft.calculate_com()
                # br = self.bottomright.com = self.bottomright.calculate_com()
                # bl = self.bottomleft.com = self.bottomleft.calculate_com()
                tr = self.topright.calculate_com()
                tl = self.topleft.calculate_com()
                br = self.bottomright.calculate_com()
                bl = self.bottomleft.calculate_com()

                self.com = ((tr[0]*self.topright.calculate_mass()
                            + tl[0]*self.topleft.calculate_mass()
                            + bl[0]*self.bottomleft.calculate_mass()
                            + br[0]*self.bottomright.calculate_mass())//self.calculate_mass(),
                            (tr[1]*self.topright.calculate_mass()
                            + tl[1]*self.topleft.calculate_mass()
                            + bl[1]*self.bottomleft.calculate_mass()
                            + br[1]*self.bottomright.calculate_mass())//self.calculate_mass())
                #print(tr, tl, br, bl)

            #print('com:', self.depth,  self.com)
            return self.com
        else:
            return (0,0)

    # def __len__(self):
    #     mass = len(self.points)
    #     if self.subdivided:
    #         mass = len(self.topright) + len(self.topleft) + len(self.bottomright) + len(self.bottomleft)
    #     return mass


    def display(self, screen):
        self.boundary.draw(screen, self.mass, self.com)
        list(p.render(screen) for p in self.points)

        #screen.blits([(p.image, (p.x, p.y)) for p in self.points])
        if self.subdivided:
            self.topleft.display(screen)
            self.topright.display(screen)
            self.bottomleft.display(screen)
            self.bottomright.display(screen)
            #print(f'tl: {len(self.topleft)},  tr: {len(self.topright)}, bl: {len(self.bottomleft)}, br: {len(self.bottomright)}')

    def calculate_force(self, screen, particle):
        if self.mass == 0:
            return 0,0
        if self.com[0] == particle.x or self.com[1] == particle.y or self.mass == particle.mass:
            return 0,0
        s = self.boundary.w*2
        d = math.sqrt((self.com[0] - particle.x)**2+(self.com[1]-particle.y)**2)
        if s/d < theta or self.children is None:
            pygame.draw.line(screen, (0, 255, 0), (particle.x, particle.y),
                             (self.com[0], self.com[1]), 2)
            return 1,1
        else:
            fx, fy = 0.0,0.0
            for node in self.children:
                    fx += node.calculate_force(screen, particle)[0]
                    fy += node.calculate_force(screen, particle)[1]
            # pygame.draw.line(screen, (0, 0, 255), (particle.x, particle.y),
            #                  (self.com[0], self.com[1]), 2)
            return fx, fy
    def mainloop(self):
        # list(p.move() for p in self.points)
        # if self.subdivided:
        #     list(p.move() for p in self.topright.points)
        #
        #     list(p.move() for p in self.topleft.points)
        #
        #     list(p.move() for p in self.bottomright.points)
        #
        #     list(p.move() for p in self.bottomleft.points)
        self.calculate_mass()
        self.calculate_com()

    def clear(self):
        global nodes
        nodes = []


nodes = []
def return_nodes():
    return nodes
