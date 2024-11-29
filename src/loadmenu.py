import dearpygui.dearpygui as dpg
import os, sys

dpg.create_context()
dpg.create_viewport(title='Barnes hut algorithm', width=1200, height=800)
dpg.set_viewport_resizable(False)
dpg.set_viewport_max_height(800)
dpg.set_viewport_pos((0,0))
dpg.set_viewport_max_width(1200)
with dpg.font_registry():
    headingfont = dpg.add_font("data/fonts/Montserrat-Black.ttf", 32)
    mediumfont = dpg.add_font("data/fonts/Montserrat-SemiBold.ttf", 28)
    df = dpg.add_font("data/fonts/Montserrat-Medium.ttf", 24)
    bf = dpg.add_font("data/fonts/Montserrat-Bold.ttf", 28)
    lf = dpg.add_font("data/fonts/Montserrat-Medium.ttf", 18)

with dpg.texture_registry():
    width, height, channels, data = dpg.load_image("data/imgs/gaussframe.png")
    gauss_texture = dpg.add_static_texture(width, height, data)
    width, height, channels, data = dpg.load_image("data/imgs/doublegaussframe.png")
    double_gauss_texture = dpg.add_static_texture(width, height, data)
    width, height, channels, data = dpg.load_image("data/imgs/torusframe.png")
    torus_texure = dpg.add_static_texture(width, height, data)
    width, height, channels, data = dpg.load_image("data/imgs/colgaussframe.png")
    col_gauss_texture = dpg.add_static_texture(width, height, data)
    width, height, channels, data = dpg.load_image("data/imgs/new_texture.png")
    new_texture = dpg.add_static_texture(width, height, data)
    width, height, channels, data = dpg.load_image("data/imgs/random.png")
    random_texture = dpg.add_static_texture(width, height, data)
    width, height, channels, data = dpg.load_image("data/imgs/backbtn.png")
    backbtn = dpg.add_static_texture(width, height, data)
def home_page():
    os.execv(sys.executable, [sys.executable, 'mainmenu.py'])



def start_gauss():
    with open('sim_callback.txt', 'w') as file:
        file.write('gauss')
    os.execv(sys.executable, [sys.executable, 'sharedmemory.py'])

def start_double_gauss():
    with open('sim_callback.txt', 'w') as file:
        file.write('double_gauss')
    os.execv(sys.executable, [sys.executable, 'sharedmemory.py'])

def start_torus():
    with open('sim_callback.txt', 'w') as file:
        file.write('torus')
    os.execv(sys.executable, [sys.executable, 'sharedmemory.py'])

def start_col_gauss():
    with open('sim_callback.txt', 'w') as file:
        file.write('col_gauss')
    os.execv(sys.executable, [sys.executable, 'sharedmemory.py'])
def start_random():
    with open('sim_callback.txt', 'w') as file:
        file.write('random')
    os.execv(sys.executable, [sys.executable, 'sharedmemory.py'])
def new_sim():
    with open('sim_callback.txt', 'w') as file:
        file.write('new_sim')
    os.execv(sys.executable, [sys.executable, 'sharedmemory.py'])


with dpg.window(label="Load page", tag = 'loadpage', pos=(0, 0)):
    bb = dpg.add_image_button(backbtn, width = 40, height=40, callback=home_page)
    dpg.add_spacer(height=30)
    dpg.add_spacer(width=450)
    dpg.add_same_line()
    heading = dpg.add_text("Load simulation", color='')
    dpg.add_spacer(height=30)
    dpg.add_spacer(width=50)
    dpg.add_same_line()
    gap = 50
    dpg.add_image_button(gauss_texture, label = 'Gaussian', width = 200, height = 200, tag = 'gaussian', callback = start_gauss)
    dpg.add_same_line()
    dpg.add_spacer(width=gap)
    dpg.add_same_line()
    dpg.add_image_button(double_gauss_texture, label = 'Double Gaussian', width = 200, height = 200, tag = 'double_gauss', callback = start_double_gauss)
    dpg.add_same_line()
    dpg.add_spacer(width=gap)
    dpg.add_same_line()
    dpg.add_image_button(torus_texure, label = 'Torus', width = 200, height = 200, tag = 'torus', callback = start_torus)
    dpg.add_same_line()
    dpg.add_spacer(width=gap)
    dpg.add_same_line()
    dpg.add_image_button(col_gauss_texture, label = 'Colored gaussian', width = 200, height = 200, tag = 'col_gauss', callback = start_col_gauss)
    dpg.add_spacer(height=10)
    dpg.add_spacer(width=120)
    dpg.add_same_line()
    dpg.add_text("Cluster")
    dpg.add_same_line()
    dpg.add_spacer(width=185)
    dpg.add_same_line()
    dpg.add_text("Double Cluster")
    dpg.add_same_line()
    dpg.add_spacer(width=175)
    dpg.add_same_line()
    dpg.add_text("Ring")
    dpg.add_same_line()
    dpg.add_spacer(width=200)
    dpg.add_same_line()
    dpg.add_text("Dense Cluster")
    dpg.add_spacer(height=25)
    dpg.add_same_line()
    dpg.add_spacer(height=35)
    dpg.add_spacer(width=50)
    dpg.add_same_line()
    dpg.add_image_button(random_texture, label = 'random_sim', width = 200, height = 200, tag = 'random_sim', callback = start_random)
    dpg.add_same_line()
    dpg.add_spacer(width=gap)
    dpg.add_same_line()
    dpg.add_image_button(new_texture, label = 'new_sim', width = 200, height = 200, tag = 'new_sim', callback = new_sim)
    dpg.add_spacer(height=20)
    dpg.add_spacer(width=120)
    dpg.add_same_line()
    dpg.add_text("Random")
    dpg.add_same_line()
    dpg.add_spacer(width=175)
    dpg.add_same_line()
    dpg.add_text("New Simulation")
    ls = dpg.add_text("", tag="temp")
    dpg.bind_font(lf)
    dpg.bind_item_font(heading,headingfont)
    dpg.bind_item_font(bb,headingfont)
    #dpg.bind_item_font(gaussbtn,headingfont)
    # dpg.bind_item_font(logint,mediumfont)
    dpg.bind_item_font(ls,lf)

with dpg.theme() as global_theme:

    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (18, 18, 18), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (36, 36, 36))
        dpg.add_theme_color(dpg.mvThemeCol_Border, (44, 44, 44), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (36, 36, 36), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 4, category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("loadpage", True)

dpg.start_dearpygui()

dpg.destroy_context()