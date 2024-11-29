import dearpygui.dearpygui as dpg
import os, sys
import warnings ; warnings.warn = lambda *args,**kwargs: None

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
    width, height, channels, data = dpg.load_image("data/imgs/gallery/bwgauss01.png")
    bwgauss01 = dpg.add_static_texture(width, height, data)
    width, height, channels, data = dpg.load_image("data/imgs/gallery/bwdoublegauss01.png")
    bwdoublegauss01 = dpg.add_static_texture(width, height, data)
    width, height, channels, data = dpg.load_image("data/imgs/gallery/bwtorus01.png")
    bwtorus01 = dpg.add_static_texture(width, height, data)
    width, height, channels, data = dpg.load_image("data/imgs/gallery/coldoublegauss01.png")
    coldoublegauss01 = dpg.add_static_texture(width, height, data)
    width, height, channels, data = dpg.load_image("data/imgs/gallery/colgauss01.png")
    colgauss01 = dpg.add_static_texture(width, height, data)
    width, height, channels, data = dpg.load_image("data/imgs/gallery/colring01.png")
    colring01 = dpg.add_static_texture(width, height, data)
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


with dpg.window(label="Gallery page", tag = 'gallerypage', pos=(0, 0)):
    bb = dpg.add_image_button(backbtn, width = 30, height=30, callback=home_page)
    dpg.add_spacer(height=15)
    dpg.add_spacer(width=525)
    dpg.add_same_line()
    heading = dpg.add_text("Gallery", color='')
    dpg.add_spacer(height=10)
    dpg.add_spacer(width=50)
    dpg.add_same_line()
    dpg.add_text("Premade simulations: ")
    dpg.add_spacer(height=10)
    dpg.add_spacer(width=50)
    dpg.add_same_line()
    gap = 50
    dpg.add_image_button(bwgauss01, label = 'Single cluster', width = 200, height = 200, tag = 'gaussian', callback = start_gauss)
    dpg.add_same_line()
    dpg.add_spacer(width=gap)
    dpg.add_same_line()
    dpg.add_image_button(bwdoublegauss01, label = 'Double cluster', width = 200, height = 200, tag = 'double_gauss', callback = start_double_gauss)
    dpg.add_same_line()
    dpg.add_spacer(width=gap)
    dpg.add_same_line()
    dpg.add_image_button(bwtorus01, label = 'Ring cluster', width = 200, height = 200, tag = 'torus', callback = start_torus)
    dpg.add_same_line()
    dpg.add_spacer(width=gap)
    dpg.add_same_line()
    dpg.add_image_button(colgauss01, label = 'Heatmap cluster', width = 200, height = 200, tag = 'col_gauss', callback = start_col_gauss)
    dpg.add_spacer(height=10)
    dpg.add_spacer(width=100)
    dpg.add_same_line()
    dpg.add_text("Single cluster")
    dpg.add_same_line()
    dpg.add_spacer(width=160)
    dpg.add_same_line()
    dpg.add_text("Double Cluster")
    dpg.add_same_line()
    dpg.add_spacer(width=150)
    dpg.add_same_line()
    dpg.add_text("Ring Cluster")
    dpg.add_same_line()
    dpg.add_spacer(width=150)
    dpg.add_same_line()
    dpg.add_text("Cluster Heatmap")
    dpg.add_spacer(height=25)
    dpg.add_spacer(width=gap)
    dpg.add_same_line()
    dpg.add_image_button(coldoublegauss01, label = 'Heatmap double cluster', width = 200, height = 200, tag = 'col_gauss', callback = start_col_gauss)
    dpg.add_same_line()
    dpg.add_spacer(width=gap)
    dpg.add_same_line()
    dpg.add_image_button(colring01, label = 'Heatmap ring', width = 200, height = 200, tag = 'col_gauss', callback = start_col_gauss)
    dpg.add_spacer(height=10)
    dpg.add_spacer(width=65)
    dpg.add_same_line()
    dpg.add_text("Double cluster heatmap")
    dpg.add_same_line()
    dpg.add_spacer(width=110)
    dpg.add_same_line()
    dpg.add_text("Ring heatmap")
    ls = dpg.add_text("", tag="temp")
    dpg.bind_font(lf)
    dpg.bind_item_font(heading,headingfont)
    dpg.bind_item_font(bb,headingfont)
    #dpg.bind_item_font(gaussbtn,headingfont)
    # dpg.bind_item_font(logint,mediumfont)
    dpg.bind_item_font(ls,lf)

with dpg.theme() as global_theme:

    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (6, 6, 6), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (6, 6, 6))
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (36, 36, 36), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8, category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("gallerypage", True)

dpg.start_dearpygui()

dpg.destroy_context()