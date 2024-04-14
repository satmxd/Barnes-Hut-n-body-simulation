from quadtreepygame import Point, Rectangle, QuadTree, return_nodes
from config import *
import random
import time
from numpy import random as rd
import pygame
from pygame.locals import *
flags = HWSURFACE | DOUBLEBUF



start = time.time()
width, height = 600,600

screen = pygame.display.set_mode((width, height), flags)
screen.set_alpha(None)
pygame.display.set_caption("Quadtree")
pygame.font.init()
font = pygame.font.SysFont('Monospace', 16)
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

#doughnut
# n = num_points
#
# circle_outer_radius = 200
# circle_inner_radius = 140
# points = []
#
# for _ in range(n):
#     p = (random.uniform(-circle_outer_radius,circle_outer_radius), random.uniform(-circle_outer_radius,circle_outer_radius))
#     if (p[0]**2+p[1]**2 <= circle_outer_radius**2) and (p[0]**2+p[1]**2 >= circle_inner_radius**2):
#         points.append(Point(p[0]+width//2, p[1]+height//2))


gaussian = rd.normal(450, 150, size=(num_points, 2))
points = list(Point(gaussian[i][0], gaussian[i][1]) for i in range(num_points))
#points += [Point(450,450,500,4)]
# gaussian2 = rd.normal(2* height // 3, 50, size=(num_points, 2))
# #
# points += list(Point(gaussian2[i][0], gaussian2[i][1]) for i in range(num_points))


rect = Rectangle(width / 2, height / 2, width / 2, height / 2)

b = time.time()

print(f'loop time: {b-a}')
i = 0
run = 'y'
while run == 'y':
    x = time.time()

    pygame.display.set_caption("QuadTree Fps: " + str(int(clock.get_fps())))
    clock.tick(fps)

    quadtree = QuadTree(rect, 4, '')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            point = Point(x, y)
            points.append(point)
        if event.type == pygame.KEYDOWN:
            if event.key == K_c:
                pygame.image.save(screen, f"frames\\screenshot{i}.jpeg")
                i += 1




    list(map(quadtree.insert, points))
    screen.fill((0, 0, 0))
    quadtree.mainloop()
    quadtree.display(screen)
    for point in points:
        if point.x > width or point.x < 0 or point.y > height or point.y < 0:
            points.remove(point)
        else:
            fx, fy = quadtree.calculate_force(point)
            point.momentum[0] += dt * fx
            point.momentum[1] += dt * fy
            point.x += dt * (point.momentum[0]/point.mass) * 0.1
            point.y += dt * (point.momentum[1]/point.mass) * 0.1

    lenpoints = font.render('Number of particles: ' + str(len(points)), 1, (0,255,0))
    lennodes = font.render('Number of nodes: ' + str(len(return_nodes())), 1, (0,255,0))
    screen.blit(lenpoints, (0, 0))
    screen.blit(lennodes, (0, 20))
    #pygame.image.save(screen, f"frames\\frame{i}.jpeg")


    pygame.display.flip()
    quadtree.clear()
    y = time.time()
    #print(y-x)
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

