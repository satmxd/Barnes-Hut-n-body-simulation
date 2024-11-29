from signal import signal
from quadtreepygame import Point, Rectangle, QuadTree, return_nodes
import random

import os, sys
import time
from numpy import random as rd
import pygame
from pygame.locals import *
flags = HWSURFACE | DOUBLEBUF

def load_gaussian(data, height, points):
    if data['num_of_particles']:
        num_points = data['num_of_particles']
    else:
        num_points = 100
    gaussian = rd.normal(height//2, 150, size=(num_points, 2))
    if data['override_sim']:
        points = list(Point(gaussian[i][0], gaussian[i][1]) for i in range(num_points))
    else:
        points += list(Point(gaussian[i][0], gaussian[i][1]) for i in range(num_points))
    data['should_load']=False
    return points



def load_torus(n, width,height,data, inner_radius=160, outer_radius=240):
    p2 = []
    for _ in range(n):
        p = (random.uniform(-outer_radius,outer_radius), random.uniform(-outer_radius,outer_radius))
        if (p[0]**2+p[1]**2 <= outer_radius**2) and (p[0]**2+p[1]**2 >= inner_radius**2):
            p2.append(Point(p[0]+width//2, p[1]+height//2))
    data['should_load']=False
    return p2

def double_gauss(height, n, shared_data):
    gaussian = rd.normal(height//2, 150, size=(n, 2))
    points = list(Point(gaussian[i][0], gaussian[i][1]) for i in range(n))
    points = load_gaussian(shared_data, height, [])
    points += [Point(450,450,500,4)]
    gaussian2 = rd.normal(2* height // 3, 50, size=(n, 2))
    #
    points += list(Point(gaussian2[i][0], gaussian2[i][1]) for i in range(n))

'''SUCCESS: The process "python.exe" with PID 10484 has been terminated.
SUCCESS: The process "python.exe" with PID 13172 has been terminated.
SUCCESS: The process "python.exe" with PID 17972 has been terminated.
SUCCESS: The process "python.exe" with PID 15224 has been terminated.
SUCCESS: The process "python.exe" with PID 3492 has been terminated.'''
def home_page():
    os.execv(sys.executable, [sys.executable, 'mainmenu.py'])

def main(shared_data):
    
    # config = get_config()
    start = time.time()
    #TODO: set w, h back to config values
    width, height = 800,800
    pygame.init()
    screen = pygame.display.set_mode((width, height), flags)
    screen.set_alpha(None)
    pygame.display.set_caption("Quadtree")
    pygame.font.init()
    font = pygame.font.SysFont('Monospace', 16, bold=True)
    clock = pygame.time.Clock()
    fps = 60
    pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
    backbtn = pygame.image.load("data/imgs/backbtn.png").convert()
    backbtn = pygame.transform.scale(backbtn, (25,25))




    colours = ["cyan",
               "magenta",
               "red",
               "green",
               "white",
               "brown",
                  "blue",
               "gray"]



    num_points = 100
    a = time.time()

    points = []
    config = shared_data
    if config['sim_type'] == 'gauss':
        points = load_gaussian(config, height, points)
    elif config['sim_type'] == 'torus':
        points = load_torus(200, width, height, config)
    elif config['sim_type'] == 'double_gauss':
        pass
    elif config['sim_type'] == 'col_gauss':
        pass
    elif config['sim_type'] == 'random':
        points = list(Point(random.randint(0, width), random.randint(0, height)) for i in range(100))

    elif config['sim_type'] == 'new_sim':
        pass
    #points = load_torus(200, width, height)
    rect = Rectangle(width / 2, height / 2, width / 2, height / 2)

    b = time.time()

    print(f'loop time: {b-a}')
    i = 0
    run = 'y'
    print('loading..')
    #time.sleep(3)





    while run == 'y':
        config = shared_data
        x = time.time()
        pygame.display.set_caption("QuadTree Fps: " + str(int(clock.get_fps())))
        clock.tick(60)

        quadtree = QuadTree(rect, config['pthresh'], '')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #rmb
                    x, y = pygame.mouse.get_pos()                    
                    if x <= width and y <= height:
                        point = Point(x, y, m=config['particlemass'])
                        points.append(point)
                    if all([x>=0, x<=30, y<=30, y>= 0]):
                        home_page()
                #TODO: fix mass increment using scroll to config file
                # elif event.button == 4:#up
                #     config.update_value('particlemass', config['particlemass']+1)
                # elif event.button == 5:#down4    
                #     if config['particlemass') >1:
                #         config.update_value('particlemass', config['particlemass']-1)
                
                else:
                    print('oub')

            if event.type == pygame.KEYDOWN:
                if event.key == K_c:
                    #pygame.image.save(screen, f"frames\\screenshot{i}.jpeg")
                    i += 1
            



        list(map(quadtree.insert, points))
        screen.fill(config['background_color'])
        screen.blit(backbtn, (5, 5))
        if config['should_load']:
            if config['premade_sim_type'] == 'Random':
                if config['override_sim']:
                    points = list(Point(random.randint(0, width), random.randint(0, height)) for i in range(config['num_of_particles']))
                else:
                    points += list(Point(random.randint(0, width), random.randint(0, height)) for i in range(config['num_of_particles']))
                config['should_load']=False
            elif config['premade_sim_type'] == 'Gaussian':
                points = load_gaussian(config, height, points)
            elif config['premade_sim_type'] == 'Torus':
                if config['override_sim']:
                    points = load_torus(config['num_of_particles'], width, height, config)
                else:
                    points += load_torus(config['num_of_particles'], width, height, config)

        quadtree.mainloop()
        quadtree.display(screen, config)
        for point in points:
            if point.x > width or point.x < 0 or point.y > height or point.y < 0:
                points.remove(point)
            else:
                fx, fy = quadtree.calculate_force(point)
                point.momentum[0] += config['dt'] * fx
                point.momentum[1] += config['dt'] * fy
                point.x += config['dt'] * (point.momentum[0]/point.mass) * 0.4
                point.y += config['dt'] * (point.momentum[1]/point.mass) * 0.4
        if config['show_node_data'] and config['show_config']:
            lenpoints = font.render('Number of particles: ' + str(len(points)), 1, config['quadtree_color'])
            lennodes = font.render('Number of nodes: ' + str(len(return_nodes())), 1,  config['quadtree_color'])
            pointinfo = font.render(f'{pygame.mouse.get_pos()}', 1,  config['quadtree_color'])
            pointmassinfo = font.render(f" mass: {config['particlemass']}", 1,  config['quadtree_color'])
            screen.blit(pointinfo, (0,height-35))
            screen.blit(pointmassinfo, (0,height-20))

            screen.blit(lenpoints, (0, 0))
            screen.blit(lennodes, (0, 20))
        if config['save_frames']:
            pygame.image.save(screen, f"frames\\frame{i}.jpeg")
        i+=1

        pygame.display.flip()
        quadtree.clear()
        y = time.time()
        #print(y-x)

    pygame.quit()

if __name__ == '__main__':
    main()



# if __name__ == "__main__":
#     processes = [Process(target=GUI.main()), Process(target=main()) ]
#     [process.start() for process in processes]

# def main(in_q):
    
#     # config = get_config()
#     start = time.time()
#     width, height = config.get_value('width'), config.get_value('height')
#     pygame.init()
#     screen = pygame.display.set_mode((width, height), flags)
#     screen.set_alpha(None)
#     pygame.display.set_caption("Quadtree")
#     pygame.font.init()
#     font = pygame.font.SysFont('Monospace', 16, bold=True)
#     clock = pygame.time.Clock()
#     fps = 60
#     pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])



#     colours = ["cyan",
#                "magenta",
#                "red",
#                "green",
#                "white",
#                "brown",
#                "blue",
#                "gray"]



#     num_points = 100
#     a = time.time()

#     #doughnut
#     # n = num_points
#     #
#     # circle_outer_radius = 200
#     # circle_inner_radius = 140
#     # points = []
#     #
#     # for _ in range(n):
#     #     p = (random.uniform(-circle_outer_radius,circle_outer_radius), random.uniform(-circle_outer_radius,circle_outer_radius))
#     #     if (p[0]**2+p[1]**2 <= circle_outer_radius**2) and (p[0]**2+p[1]**2 >= circle_inner_radius**2):
#     #         points.append(Point(p[0]+width//2, p[1]+height//2))


#     gaussian = rd.normal(height//2, 150, size=(num_points, 2))
#     points = list(Point(gaussian[i][0], gaussian[i][1]) for i in range(num_points))
#     #points += [Point(450,450,500,4)]
#     # gaussian2 = rd.normal(2* height // 3, 50, size=(num_points, 2))
#     # #
#     # points += list(Point(gaussian2[i][0], gaussian2[i][1]) for i in range(num_points))


#     rect = Rectangle(width / 2, height / 2, width / 2, height / 2)

#     b = time.time()

#     print(f'loop time: {b-a}')
#     i = 0
#     run = 'y'
#     print('loading..')
#     #time.sleep(3)
#     while run == 'y':
        
#         x = time.time()
#         pygame.display.set_caption("QuadTree Fps: " + str(int(clock.get_fps())))
#         clock.tick(60)

#         quadtree = QuadTree(rect, 4, '')
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False

#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1: #rmb
#                     x, y = pygame.mouse.get_pos()                    
#                     if x <= width and y <= height:
#                         point = Point(x, y, m=config.get_value('particlemass'))
#                         points.append(point)
#                 elif event.button == 4:#up
#                     config.update_value('particlemass', config.get_value('particlemass')+1)
#                 elif event.button == 5:#down4    
#                     if config.get_value('particlemass') >1:
#                         config.update_value('particlemass', config.get_value('particlemass')-1)
#                 else:
#                     print('oub')

#             if event.type == pygame.KEYDOWN:
#                 if event.key == K_c:
#                     #pygame.image.save(screen, f"frames\\screenshot{i}.jpeg")
#                     i += 1
            




#         list(map(quadtree.insert, points))
#         screen.fill(config.get_value('background_color'))
#         quadtree.mainloop()
#         quadtree.display(screen)
#         for point in points:
#             if point.x > width or point.x < 0 or point.y > height or point.y < 0:
#                 points.remove(point)
#             else:
#                 fx, fy = quadtree.calculate_force(point)
#                 point.momentum[0] += config.get_value('dt') * fx
#                 point.momentum[1] += config.get_value('dt') * fy
#                 point.x += config.get_value('dt') * (point.momentum[0]/point.mass) * 0.4
#                 point.y += config.get_value('dt') * (point.momentum[1]/point.mass) * 0.4
#         if config.get_value('show_node_data'):
#             lenpoints = font.render('Number of particles: ' + str(len(points)), 1, config.get_value('secondary_color'))
#             lennodes = font.render('Number of nodes: ' + str(len(return_nodes())), 1,  config.get_value('secondary_color'))
#             pointinfo = font.render(f'{pygame.mouse.get_pos()}', 1,  config.get_value('secondary_color'))
#             pointmassinfo = font.render(f" mass: {config.get_value('particlemass')}", 1,  config.get_value('secondary_color'))
#             screen.blit(pointinfo, (0,height-35))
#             screen.blit(pointmassinfo, (0,height-20))

#             screen.blit(lenpoints, (0, 0))
#             screen.blit(lennodes, (0, 20))
#         if config.get_value('save_frames'):
#             pygame.image.save(screen, f"frames\\frame{i}.jpeg")
#         i+=1


#         pygame.display.flip()
#         quadtree.clear()
#         y = time.time()
#         #print(y-x)

#     pygame.quit()