from turtle import title
import dearpygui.dearpygui as dpg
import os, sys
from cryptography.fernet import Fernet
import pickle
import mysql.connector

database = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="mysql",
database="bhauserdb"
)

Cursor = database.cursor()
Cursor.execute('CREATE DATABASE IF NOT EXISTS bhauserdb')
Cursor.execute('CREATE TABLE IF NOT EXISTS USERS (username varchar(25) PRIMARY KEY, email varchar(30), password varchar(150), current bool default false)')

print(Cursor.fetchall())

if not os.path.exists('data\\key.txt') or os.stat('data\\key.txt').st_size == 0:
    key = Fernet.generate_key()
    with open('data\\key.txt', 'wb') as file:
        pickle.dump(key, file)
else:
    with open('data\\key.txt', 'rb') as file:
        key = pickle.load(file)

with open('loadid.txt', 'w') as file:
    pass#important to erase data in the begining for saving/loading


def login_callback(sender, app_data, user_data):
    Cursor.execute('SELECT username FROM USERS')
    usernames = Cursor.fetchall()
    Cursor.execute('SELECT password FROM USERS')
    passwords = Cursor.fetchall()

    users = dict(zip(map(lambda x: x[0], usernames),map(lambda x: x[0], passwords)))
    print(users)

    username = dpg.get_value("login_username").lower()
    print(username)
    password = dpg.get_value("login_password")

    if username in users:
        cipher_suite = Fernet(key)
        ciphered_text = users[username].encode('ascii')
        pw = cipher_suite.decrypt(ciphered_text).decode('ascii')
        if password == pw:
            dpg.set_value("login_status", f"Welcome back, {username}!")
            with open('currentuser.txt', 'w') as file:
                file.write(username)
            query = f'''UPDATE USERS SET current = true WHERE username = "{username}"'''
            print(query)
            Cursor.execute(query)
            database.commit()
            print(Cursor.execute('SELECT * FROM USERS'))
            print('Updated...')
            os.execv(sys.executable, [sys.executable, 'mainmenu.py'])
        else:
            dpg.set_value("login_status", "Incorrect password. Please try again.")

    else:
        dpg.set_value("login_status", "User does not exist, Register first.")

def register_callback(sender, app_data, user_data):
    Cursor.execute('SELECT username FROM USERS')
    usernames = Cursor.fetchall()
    Cursor.execute('SELECT password FROM USERS')
    passwords = Cursor.fetchall()

    users = dict(zip(map(lambda x: x[0], usernames),map(lambda x: x[0], passwords)))
    username = dpg.get_value("register_username").lower()
    password = dpg.get_value("register_pw")
    password_confirm = dpg.get_value("register_pw_confirm")
    email = dpg.get_value("register_email")
    # confirm_password = dpg.get_value("confirm_password")


    if username in users:
        dpg.set_value("reg_status", "Username already exists. Please choose another.")
    # elif password != confirm_password:
    #     dpg.set_value("register_status", "Passwords do not match. Please try again.")
    elif all([username, password, password_confirm]):
        if '@' not in email or '.' not in email:
            dpg.set_value("reg_status", "Invalid email")
        elif password != password_confirm:
            dpg.set_value("reg_status", "Passwords do not match")
        else:
            cipher_suite = Fernet(key)
            ciphered_text = cipher_suite.encrypt(password.encode('ascii')) .decode('ascii')
            print(len(ciphered_text))
            query = f'''INSERT INTO USERS VALUES ('{username}', '{email}', '{ciphered_text}', false)'''
            Cursor.execute(query)
            database.commit()
            dpg.set_value("reg_status", f"User '{username}' registered successfully!")
    else:
        dpg.set_value("reg_status", "Invalid details")
dpg.create_context()
dpg.create_viewport(title='Barnes hut algorithm', width=800, height=600)
dpg.set_viewport_resizable(False)
dpg.set_viewport_max_height(600)
dpg.set_viewport_max_width(800)
with dpg.font_registry():
    headingfont = dpg.add_font("data/fonts/Montserrat-Black.ttf", 32)
    mediumfont = dpg.add_font("data/fonts/Montserrat-SemiBold.ttf", 28)
    df = dpg.add_font("data/fonts/Montserrat-Medium.ttf", 24)
    bf = dpg.add_font("data/fonts/Montserrat-Bold.ttf", 28)
    lf = dpg.add_font("data/fonts/Montserrat-Medium.ttf", 18)

with dpg.texture_registry():
    width, height, channels, data = dpg.load_image("data\\imgs\\300x300.gif")
    texture_id = dpg.add_static_texture(width, height, data)

def home_page():
    os.execv(sys.executable, [sys.executable, 'mainmenu.py'])



def on_register_click():

    dpg.configure_item('registerpage', show = True)



with dpg.window(label="Register", tag = 'registerpage', pos=(0, 0), no_resize=True, no_move=True, show = False, width=800, height=600, no_title_bar=True):
    dpg.add_button(label=" < ", callback=lambda: dpg.configure_item("registerpage", show = False))
    dpg.add_spacer(height=50)
    dpg.add_spacer(width=175)
    dpg.add_same_line()
    w = 220
    heading = dpg.add_text("Barnes Hut Gravity simulation", color='')
    dpg.add_spacer(height=5)
    dpg.add_spacer(width=315)
    dpg.add_same_line()
    regt = dpg.add_text("Register User", color='')
    dpg.add_spacer(height=50)
    dpg.add_spacer(width=w)
    dpg.add_same_line()
    dpg.add_input_text(hint=" Username*", tag="register_username", width = 350)
    dpg.add_spacer(height=10)
    dpg.add_spacer(width=w)
    dpg.add_same_line()
    dpg.add_input_text(hint=" Email ID", tag="register_email", width = 350)
    dpg.add_spacer(height=10)
    dpg.add_spacer(width=w)
    dpg.add_same_line()
    dpg.add_input_text(hint=" Password*", tag="register_pw", width = 350, password=True)
    dpg.add_spacer(height=10)
    dpg.add_spacer(width=w)
    dpg.add_same_line()

    dpg.add_input_text(hint=" Confirm Password*", tag="register_pw_confirm", password=True, width = 350)
    dpg.add_spacer(height=50)
    dpg.add_spacer(width=350)
    dpg.add_same_line()
    dpg.add_button(label="Register", callback=register_callback)
    dpg.add_spacer(height=10)

    dpg.add_spacer(width=10)
    dpg.add_same_line()
    # dpg.add_same_line()
    # dpg.add_spacer(width=50)
    # dpg.add_same_line()
    # dpg.add_button(label='Register', callback = register_callback)
    ls = dpg.add_text("", tag="reg_status")    
    dpg.bind_font(df)
    dpg.bind_item_font(regt,mediumfont)
    dpg.bind_item_font(heading,headingfont)
    dpg.bind_item_font(ls,lf)






with dpg.window(label="Login", tag = 'loginpage', pos=(0, 0)):
    # dpg.add_button(label=" < ", callback=home_page)
    dpg.add_spacer(height=80)
    dpg.add_spacer(width=175)
    dpg.add_same_line()
    heading = dpg.add_text("Barnes Hut Gravity simulation", color='')
    dpg.add_spacer(height=5)
    dpg.add_spacer(width=315)
    dpg.add_same_line()
    logint = dpg.add_text("User Login", color='')
    dpg.add_spacer(height=70)
    dpg.add_spacer(width=200)
    dpg.add_same_line()
    dpg.add_input_text(tag="login_username", width = 350, hint="Username")
    dpg.add_spacer(height=10)
    dpg.add_spacer(width=200)
    dpg.add_same_line()
    dpg.add_input_text(tag="login_password", password=True, width = 350, hint = "Password")
    dpg.add_spacer(height=50)
    dpg.add_spacer(width=340)
    dpg.add_same_line()
    dpg.add_button(label="Login", callback=login_callback)
    dpg.add_spacer(height=10)
    dpg.add_spacer(width=329)
    dpg.add_same_line()
    dpg.add_button(label="Register", callback=on_register_click)
    dpg.add_spacer(height=50)

    dpg.add_spacer(width=275)
    dpg.add_same_line()
    # dpg.add_same_line()
    # dpg.add_spacer(width=50)
    # dpg.add_same_line()
    # dpg.add_button(label='Register', callback = register_callback)
    ls = dpg.add_text("", tag="login_status")
    dpg.bind_font(df)
    dpg.bind_item_font(heading,headingfont)
    dpg.bind_item_font(logint,mediumfont)
    dpg.bind_item_font(ls,lf)


# with dpg.window(label="Register", width=400, height=400, pos=(420, 0)):
#     dpg.add_text("Register Page")
#     dpg.add_spacer(height=10)
#     dpg.add_input_text(label="Username", tag="register_username")
#     dpg.add_input_text(label="Password", tag="register_password", password=True)
#     dpg.add_input_text(label="Confirm Password", tag="confirm_password", password=True)
#     dpg.add_button(label="Register", callback=register_callback)
#     dpg.add_spacer(height=10)
#     dpg.add_text("", tag="register_status")


with dpg.theme() as global_theme:

    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (18, 18, 18), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button, (36, 36, 36))
        dpg.add_theme_color(dpg.mvThemeCol_Border, (44, 44, 44), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (36, 36, 36), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 4, category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("loginpage", True)

dpg.start_dearpygui()

dpg.destroy_context()
