import pygame
import pygame_gui
import webbrowser
from pygamevideo import Video

pygame.init()
width, height = 1200, 800
pygame.display.set_caption('Main')
window_surface = pygame.display.set_mode((width, height), pygame.RESIZABLE)

background = pygame.Surface((width, height))
background.fill(pygame.Color('#000000'))

# vid = VideoPlayer(Video(r'vid.mkv'), (0,0,300,300), loop=True)
# vid.queue(Video(r'vid.mkv'))
vid = Video("400x400long.gif")
vid2 = Video("400x400doublevig.gif")
imp = pygame.image.load("frame4.jpeg").convert()
imp = pygame.transform.scale(imp , (300,300))
vid.play(loop=True)
vid2.play(loop=True)

manager = pygame_gui.UIManager((width, height), theme_path="theme.json")
button_gap_h = 50
button_gap_w = 30
button_height = 50
button_width = 150

buttons = {'startbtn': 'start','savebtn': 'saves','optnsbtn': 'options','exitbtn': 'exit'}
btns = []

font32 = pygame.font.Font('data/fonts/Montserrat-Bold.ttf', 50)
font22 = pygame.font.Font('data/fonts/Montserrat-Medium.ttf', 22)

c = 0
for i in buttons:
    btns.append(pygame_gui.elements.UIButton(relative_rect=pygame.Rect((button_gap_h, window_surface.get_height()//2-(len(buttons)*button_height+button_gap_h)//2+(button_height+button_gap_h)*c), (button_width, button_height)),
                                         text=buttons[i],
                                         manager=manager, object_id=i))
    c+=1
credits = pygame_gui.elements.UITextBox("<font face=candara size = 18 color = #c2dde4><a href='creditsid'>Made by Satvik Madayi</a></font>", relative_rect=pygame.Rect((button_gap_h-10,(len(buttons)*button_height+button_gap_h)//2+(button_height+button_gap_h)),(200,50)), manager = manager)
maintext = font32.render('Simulating Galaxies', True, '#c9374c')
subtext = font22.render(' using the Barnes Hut algorithm', True, '#76101e')

maintextrect = maintext.get_rect()
subtextrect = subtext.get_rect()
# set the center of the rectangular object.
maintextrect.center = (window_surface.get_width()// 2, 50)
subtextrect.center = (window_surface.get_width()// 2, 90)

def start():
    pass
def saves():
    pass
def options():
    pass



clock = pygame.time.Clock()
is_running = True
while is_running:
    time_delta = clock.tick(60)/1000.0
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            is_running = False

        manager.process_events(event)
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_object_id == 'startbtn':
                start()
            elif event.ui_object_id == 'savesbtn':
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

        manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    window_surface.blit(maintext, maintextrect)
    window_surface.blit(subtext, subtextrect)
    window_surface.blit(imp, (0, 0))

    vid.draw_to(window_surface,(window_surface.get_width()-vid.get_frame().get_width()-200, 150))
    vid2.draw_to(window_surface,(250, 300))

    pygame.display.flip()

