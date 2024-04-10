import numpy as np

from quadtreepygame import Point, Rectangle, QuadTree, return_nodes
import random
import time
from numpy import random as rd
import pygame
from pygame.locals import *
flags = HWSURFACE | DOUBLEBUF



start = time.time()
width, height = 600, 600

screen = pygame.display.set_mode((width, height), flags)
screen.set_alpha(None)
pygame.display.set_caption("Quadtree")
clock = pygame.time.Clock()
fps = 60
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

colours = ["cyan",
           "magenta",
           "red",
           "green",
           "white",
           "brown",
           "blue",
           "gray"]



num_points = 0
a = time.time()
gaussian = rd.normal(height / 2, 100, size=(num_points, 2))
points = list(Point(gaussian[i][0], gaussian[i][1]) for i in range(num_points))
rect = Rectangle(width / 2, height / 2, width / 2, height / 2)
# quadtree = QuadTree(rect, 4, '')
# list(map(quadtree.insert, points))
# quadtree.mainloop()
b = time.time()

print(f'loop time: {b-a}')

run = 'y'
while run == 'y':

    screen.fill((0,0,0))
    pygame.display.set_caption("QuadTree Fps: " + str(int(clock.get_fps())))
    clock.tick(fps)

    quadtree = QuadTree(rect, 3, '')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            point = Point(x, y)
            points.append(point)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                pass

    list(map(quadtree.insert, points))
    #print(len(return_nodes()))
    quadtree.mainloop()
    quadtree.display(screen)

    for point in points:
        fx, fy = quadtree.calculate_force(screen, point)
        #print(fx, fy)


    # for node in return_nodes():
    #     for point in points:
    #         if not node.com == (point.x, point.y) and node.com != (None,None):
    #                 s = node.boundary.w*2
    #                 d = point.distance(node.com)
    #                 if s/d > theta:
    #                     pass
    #                 else:
    #                     pygame.draw.line(screen, (0,255,0), (point.quadrant.com[0],point.quadrant.com[1]), (node.com[0], node.com[1]), 2)



    pygame.display.flip()
    quadtree.clear()
pygame.quit()










def spawn_particles(n, gauss = False):
    for i in range(n):
        try:
            if gauss:
                gaussian = rd.normal(width / 2, 100, size=(n, 2))
                x, y = int(gaussian[i][0]), int(gaussian[i][1])

            else:
                x, y = random.randrange(0, width), random.randrange(0, height)

            quadtree.insert(Point(x, y))
            #canvas.create_oval(x, y, x + 5, y + 5, fill=random.choice(colours))
            #canvas.create_text(x, y - 10, text=str([x, y]), fill='white')
        except:
            pass
def click(event = None):
    # canvas.delete('e')
    quadtree.insert(Point(event.x,event.y))
    quadtree.mainloop()
    # canvas.create_oval(event.x, event.y, event.x + 5, event.y + 5, fill=random.choice(colours))
    #print(len(return_nodes()))
    #canvas.create_text(event.x, event.y-10, text=str([event.x,event.y]), fill='white')
    #print(quadtree.points)

