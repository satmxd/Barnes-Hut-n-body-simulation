import math

import numpy as np

import pygame
from Particle import Point
pygame.font.init()
font = pygame.font.SysFont('Monospace', 12)

# configdata = {}

# def update_config():
#     with open('config.txt', 'r') as file:
#         configdata = eval(file.read())

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
    def draw(self, screen,  mass, com, depth, config):
        #from config import show_config, show_centre_of_mass, show_node_data, show_quadtree,show_quadtree_depth, quadtree_color, quadtree_thickness
        # with open('config.txt', 'r') as file:
        #     dat = file.readlines()
        #data = config.data
        if config['show_config']:
            if config['show_quadtree']:
                pygame.draw.rect(screen, config['quadtree_color'], pygame.Rect(self.x-self.w, self.y-self.h, self.w*2, self.h*2),config['quadtree_thickness'])
                if config['show_quadtree_depth'] and depth != '':
                    d_text = font.render(f'depth: {depth}', False, (255, 255, 255))
                    screen.blit(d_text, (self.x, self.y + 10))
        # if config.show_config:
        #     if config.show_quadtree:
        #         pygame.draw.rect(screen, config.quadtree_color, pygame.Rect(self.x-self.w, self.y-self.h, self.w*2, self.h*2), config.quadtree_thickness)
        #         if config.show_quadtree_depth and depth != '':
        #             d_text = font.render(f'depth: {depth}', False, (255, 255, 255))
        #             screen.blit(d_text, (self.x, self.y + 10))
            #mass_text = font.render(str(mass), False, (255,255,255))
            #screen.blit(mass_text, (self.x, self.y))
            try:
                if config['show_centre_of_mass']:
                    pygame.draw.circle(screen, (255,0,0), (com[0], com[1]), 4)
                    com_text = font.render(f'com: {com}', False, (255, 255, 255))
                    screen.blit(com_text, (com[0], com[1]))
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
            self.points += [point]
            point.quadrant = self
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


    def display(self, screen, config):
        self.boundary.draw(screen, self.mass, self.com, self.depth, config)
        list(p.render(screen, config['show_particle_colours']) for p in self.points)

        #screen.blits([(p.image, (p.x, p.y)) for p in self.points])
        if self.subdivided:
            self.topleft.display(screen, config)
            self.topright.display(screen, config)
            self.bottomleft.display(screen, config)
            self.bottomright.display(screen, config)
            #print(f'tl: {len(self.topleft)},  tr: {len(self.topright)}, bl: {len(self.bottomleft)}, br: {len(self.bottomright)}')

    def force(self, mass, x, y,d, body):
        G = 0.766
        damp = 0.2
        floatcutoff = 0.001
        #TODO: change G, damp, fcutoff back to config values
        if d > floatcutoff:
            f =  G*mass*body.mass*damp/(d*d)
            dx = body.com[0] - x
            dy = body.com[1] - y
            angle = math.atan2(dy, dx)
            fx = math.cos(angle) * f
            fy = math.sin(angle) * f
            #print(fx, fy, body.depth)
            return (fx, fy)
        else:
            return (0,0)


    def calculate_force(self, particle, screen = None):
            
            theta = 0.35
            floatcutoff = 0.001
            if self.mass == 0 or self.mass is None:
                return (0,0)
            if self.com[0] == particle.x and self.com[1] == particle.y and self.mass == particle.mass:
                return (0,0)

            s = self.boundary.w*2

            d = np.sqrt((self.com[0]-particle.x)**2+(self.com[1]-particle.y)**2)
            if d > floatcutoff:
                if s < d*theta or self.children is None:
                    # pygame.draw.line(screen, (0, 255, 0), (particle.x, particle.y),
                    #                  (self.com[0], self.com[1]), 2)
                    return self.force(particle.mass, particle.x, particle.y,d, self)
                else:
                    fx, fy = 0.0,0.0
                    for node in self.children:
                        if node is not None:
                            f = node.calculate_force(particle)
                            fx += f[0]
                            fy += f[1]
                    # pygame.draw.line(screen, (0, 0, 255), (particle.x, particle.y),
                    #                  (self.com[0], self.com[1]), 2)
                    return (fx, fy)
            else:
                return (0,0)


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
