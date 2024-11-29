import subprocess
from random import choice, randint, uniform, randrange
from numpy import random as rd
from numpy import array, sqrt, sum as npsum 

import pygame
import pygame_gui
import os, sys
import webbrowser
from Menuparticle import Particle
pygame.init()
width, height = 1200, 800
pygame.display.set_caption('Main')
window_surface = pygame.display.set_mode((width, height))

background = pygame.Surface((width, height))
background.fill(pygame.Color('#000000'))

# vid = VideoPlayer(Video(r'vid.mkv'), (0,0,300,300), loop=True)
# vid.queue(Video(r'vid.mkv'))

# imp = pygame.image.load("frame4.jpeg").convert()
# imp = pygame.transform.scale(imp , (300,300))


manager = pygame_gui.UIManager((width, height), theme_path="theme.json")
button_gap_h = 50
button_gap_w = 30
button_height = 50
button_width = 150

buttons = {'startbtn': 'Start','savesbtn': 'Saves','gallerybtn': 'Gallery', 'exitbtn': 'Exit'}
# buttons = {'startbtn': 'start','savesbtn': 'saves','optnsbtn': 'options','exitbtn': 'exit'}

btns = []

font32 = pygame.font.Font('data/fonts/Montserrat-Bold.ttf', 50)
font22 = pygame.font.Font('data/fonts/Montserrat-Medium.ttf', 22)
font18 = pygame.font.Font('data/fonts/Montserrat-Medium.ttf', 18)

c = 0
for i in buttons:
    btns.append(pygame_gui.elements.UIButton(relative_rect=pygame.Rect((button_gap_h, window_surface.get_height()//2-(len(buttons)*button_height+button_gap_h)//2+(button_height+button_gap_h)*c), (button_width, button_height)),
                                         text=buttons[i],
                                         manager=manager, object_id=i))
    c+=1
credits = pygame_gui.elements.UITextBox("<font face=candara size = 18 color = #c2dde4><a href='creditsid'>Made by Satvik Madayi</a></font>", relative_rect=pygame.Rect((button_gap_h-10,(len(buttons)*button_height+button_gap_h)//2+(button_height+button_gap_h)),(200,50)), manager = manager)
#c9374c, 76101e
maintext = font32.render('Simulating Galaxies', True, '#ffffff')
subtext = font22.render(' using the Barnes Hut algorithm', True, '#ffffff')

user = None
try:
    with open('currentuser.txt', 'r') as file:
        user = file.read()
except Exception as e:
    print(e)
usertext = font18.render(f'Welcome {user}', True, '#bfbfbf')

maintextrect = maintext.get_rect()
subtextrect = subtext.get_rect()
usertextrect = usertext.get_rect()
# set the center of the rectangular object.
maintextrect.center = (window_surface.get_width()// 2, 50)
subtextrect.center = (window_surface.get_width()// 2, 90)
usertextrect.midleft = (50, 50)

def start():
    os.execv(sys.executable, [sys.executable, 'loadmenu.py'])

def saves():
    os.execv(sys.executable, [sys.executable, 'savesmenu.py'])
def options():
    pass

def gallery():
    os.execv(sys.executable, [sys.executable, 'savesmenu.py'])


clock = pygame.time.Clock()
is_running = True

num_points=1700
particle_group = pygame.sprite.Group()

particles = []

gaussian = array(rd.normal((width//2, height//2), 170, size=(num_points, 2)))
dists = sqrt(npsum((gaussian[:]-array([[600,400]]*num_points))**2, axis=1))
gaussian = [list(map(round, gaussian[i])) for i in range(num_points)  if dists[i] > 75]
print(len(gaussian))
particles += list(Particle(particle_group,
 (gaussian[i][0], gaussian[i][1]),
  '#FFFFFF',
  (pygame.math.Vector2(uniform(-1,1),
  uniform(-1,1))).normalize(),
  randint(1,25)) for i in range(len(gaussian)))

particles += list(Particle(particle_group,
 (randrange(0, width), randrange(0, height)),
  '#FFFFFF',
  (pygame.math.Vector2(uniform(-1,1),
  uniform(-1,1))).normalize(),
  randint(1,25)) for i in range(200))




#############Centre Burst effect############
# for i in range(200):
#     pos = (width//2,height//2)
#     color = choice(("red", "green", "blue"))
#     direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1))
#     direction = direction.normalize()
#     speed = randint(50, 100)
#     Particle(particle_group, pos, color, direction, speed)
# for i in range(20):
#     particle_group.update(0.004, width//2,height//2)
############################################


while is_running:
    time_delta = clock.tick()/1000.0
    events = pygame.event.get()
    particle_group.draw(background)

    #print(len(particle_group.sprites()))
    x,y = pygame.mouse.get_pos()
    particle_group.update(0.004, x,y)
    pygame.display.set_caption("fps: " + str(int(clock.get_fps())))

    for event in events:
        if event.type == pygame.QUIT:
            is_running = False

        manager.process_events(event)
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_object_id == 'startbtn':
                start()
            elif event.ui_object_id == 'savesbtn':
                print('save btn pressed')
                saves()
            elif event.ui_object_id == 'optionsbtn':
                options()
            elif event.ui_object_id == 'exitbtn':
                exit()
        if event.type == pygame_gui.UI_TEXT_BOX_LINK_CLICKED:
            if event.ui_element is credits:
                webbrowser.open('https://github.com/satmxd')
        if event.type == pygame.WINDOWRESIZED:
            maintextrect.center = (window_surface.get_width()//2, 50)
            subtextrect.center = (window_surface.get_width()//2, 90)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                for i in range(50):
                    pos = pygame.mouse.get_pos()
                    color = choice(("red", "green", "blue"))
                    direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1))
                    direction = direction.normalize()
                    speed = randint(50, 150)
                    Particle(particle_group, pos, color, direction, speed)

        manager.update(time_delta)
    
    
    
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    window_surface.blit(maintext, maintextrect)
    window_surface.blit(subtext, subtextrect)
    window_surface.blit(usertext, usertextrect)

    #window_surface.blit(imp, (0, 0))


    pygame.display.flip()
    background.fill('#000000')


