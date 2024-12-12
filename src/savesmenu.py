import dearpygui.dearpygui as dpg
import os, sys

dpg.create_context()
dpg.create_viewport(title='Barnes hut algorithm', width=1200, height=800)
dpg.set_viewport_resizable(False)
dpg.set_viewport_max_height(800)
dpg.set_viewport_pos((0,0))
dpg.set_viewport_max_width(1200)

import mysql.connector

database = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="*SatvikMYSQL*",
database="bhadb"
)

Cursor = database.cursor(buffered=True)




with dpg.font_registry():
    headingfont = dpg.add_font("data/fonts/Montserrat-Black.ttf", 32)
    mediumfont = dpg.add_font("data/fonts/Montserrat-SemiBold.ttf", 24)
    df = dpg.add_font("data/fonts/Montserrat-Medium.ttf", 24)
    bf = dpg.add_font("data/fonts/Montserrat-Bold.ttf", 28)
    lf = dpg.add_font("data/fonts/Montserrat-Medium.ttf", 20)



def home_page():
    os.execv(sys.executable, [sys.executable, 'mainmenu.py'])


with dpg.texture_registry():
    width, height, channels, data = dpg.load_image("data/imgs/backbtn.png")
    backbtn = dpg.add_static_texture(width, height, data)


currentuser = None
with open('currentuser.txt', 'r') as file:
    currentuser = file.read()

def retrieve_data():
    try:
        Cursor.execute(f'SELECT * FROM {currentuser}')
        data = Cursor.fetchall()
        edata = []
        for rdata in data:
            fdata = []
            for entry in rdata[:5]:
                fdata.append(str(entry))
            edata.append(fdata)
        return edata
    except Exception as e:
        return (f'Error occured while retrieving data: {e}')

print(retrieve_data())

def get_entry_count():
    try:
        Cursor.execute(f'SELECT COUNT(*) FROM {currentuser}')
        count = Cursor.fetchone()[0]
        return int(count)
    except Exception as e:
        print(f'Error occured while getting entry count: {e}')
        return 0

def get_column_names():
    try:
        Cursor.execute(f'DESC {currentuser}')
        rdata = Cursor.fetchall()
        fdata = []
        for i in rdata:
            fdata.append(i[0])
        return fdata[:5]
    except Exception as e:
        return (f'Error occured while retrieving column names: {e}')



def redirect_to_sim(sender, app_data, user_data):
    print('USERDAT: ',user_data)
    with open('loadid.txt', 'w') as file:
        file.write(str(user_data))
    os.execv(sys.executable, [sys.executable, 'sharedmemory.py'])

#TODO COMPLETE DELETE FUNCTIONALITY
def delete_entry():
    os.execv(sys.executable, [sys.executable, 'deletesavesmenu.py'])


with dpg.window(label="Load page", tag = 'loadpage', pos=(0, 0)):
    bb = dpg.add_image_button(backbtn, width = 40, height=40, callback=home_page)
    dpg.add_spacer(height=30)
    dpg.add_spacer(width=490)
    dpg.add_same_line()
    heading = dpg.add_text("User saves", color='')
    dpg.add_spacer(height=30)
    dpg.add_spacer(width=350)
    dpg.add_same_line()
    infotxt = dpg.add_text("Click on the load id to load particular saves")
    dpg.add_spacer(height=50)
    if get_entry_count() == 0:
        dpg.add_spacer(width=320)
        dpg.add_same_line()
        errortext = dpg.add_text("No entries exist for this user, save a simulation to view it here.")


    with dpg.table(header_row=True):

        # use add_table_column to add columns to the table,
        # table columns use slot 0
        if get_entry_count() > 0:
            for i in get_column_names():
                clmh = dpg.add_table_column(label=i)

        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
            for i in range(0, get_entry_count()): #rows
                with dpg.table_row():
                    for j in range(0, 5): #columns
                        if j == 0:
                            dpg.add_spacer(width=25)
                            dpg.add_same_line()
                            print('button text: ', retrieve_data()[i][j])
                            dpg.add_button(label = retrieve_data()[i][j], callback = redirect_to_sim,user_data = str(retrieve_data()[i][j]), width = 200)
                        else:
                        # dpg.add_text(f"Row{i} Column{j}")
                            dpg.add_text(retrieve_data()[i][j])
        else:
            print('text')
    dpg.add_spacer(height=30)
    dpg.add_spacer(width=495)
    dpg.add_same_line()
    if get_entry_count() > 0:
        delbtn = dpg.add_button(label = "Delete save", callback = delete_entry)
    

    ls = dpg.add_text("", tag="temp")
    dpg.bind_font(lf)
    dpg.bind_item_font(heading,headingfont)
    dpg.bind_item_font(bb,headingfont)
    #dpg.bind_item_font(gaussbtn,headingfont)
    # dpg.bind_item_font(logint,mediumfont)
    if get_entry_count() > 0:
        dpg.bind_item_font(delbtn, mediumfont)
    dpg.bind_item_font(infotxt, mediumfont)

    dpg.bind_item_font(ls,lf)

with dpg.theme() as global_theme:

    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (18, 18, 18), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (18, 18, 18))
        dpg.add_theme_color(dpg.mvThemeCol_Border, (10, 10, 10), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (10, 10, 10), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4, category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)

with dpg.theme() as item_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (18, 18, 18), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (36, 36, 36))
        dpg.add_theme_color(dpg.mvThemeCol_Border, (44, 44, 44), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (36, 36, 36), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4, category=dpg.mvThemeCat_Core)
if get_entry_count() > 0:
    dpg.bind_item_theme(delbtn, item_theme)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("loadpage", True)

dpg.start_dearpygui()

dpg.destroy_context()