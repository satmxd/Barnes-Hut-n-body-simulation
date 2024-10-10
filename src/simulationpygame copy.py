from socket import timeout
from quadtreepygame import Point, Rectangle, QuadTree, return_nodes
#from config import get_config
import random
import time
from numpy import random as rd
import pygame
from pygame.locals import *
flags = HWSURFACE | DOUBLEBUF



def main(in_q):
    
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


    gaussian = rd.normal(height//2, 150, size=(num_points, 2))
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
    print('loading..')
    #time.sleep(3)
    while run == 'y':
        
        x = time.time()
        pygame.display.set_caption("QuadTree Fps: " + str(int(clock.get_fps())))
        clock.tick(60)

        quadtree = QuadTree(rect, 4, '')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #rmb
                    x, y = pygame.mouse.get_pos()                    
                    if x <= width and y <= height:
                        point = Point(x, y, m=config['particlemass'])
                        points.append(point)
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
            



        config = in_q.get()
        list(map(quadtree.insert, points))
        screen.fill(config['background_color'])
        configtext = font.render(str(config), 1, '#ffffff')
        screen.blit(configtext, (0,height-40))



        quadtree.mainloop()
        quadtree.display(screen)
        for point in points:
            if point.x > width or point.x < 0 or point.y > height or point.y < 0:
                points.remove(point)
            else:
                fx, fy = quadtree.calculate_force(point)
                point.momentum[0] += config['dt'] * fx
                point.momentum[1] += config['dt'] * fy
                point.x += config['dt'] * (point.momentum[0]/point.mass) * 0.4
                point.y += config['dt'] * (point.momentum[1]/point.mass) * 0.4
        if config['show_node_data']:
            lenpoints = font.render('Number of particles: ' + str(len(points)), 1, config['secondary_color'])
            lennodes = font.render('Number of nodes: ' + str(len(return_nodes())), 1,  config['secondary_color'])
            pointinfo = font.render(f'{pygame.mouse.get_pos()}', 1,  config['secondary_color'])
            pointmassinfo = font.render(f" mass: {config['particlemass']}", 1,  config['secondary_color'])
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