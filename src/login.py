import dearpygui.dearpygui as dpg
import os, sys
from cryptography.fernet import Fernet
import pickle
import mysql.connector

database = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="*SatvikMYSQL*",
database="bhauserdb"
)

Cursor = database.cursor()
Cursor.execute('CREATE DATABASE IF NOT EXISTS bhauserdb')
Cursor.execute('CREATE TABLE IF NOT EXISTS USERS (username varchar(25) PRIMARY KEY, password varchar(150), current bool default false)')

print(Cursor.fetchall())

if not os.path.exists('data\\key.txt') or os.stat('data\\key.txt').st_size == 0:
    key = Fernet.generate_key()
    with open('data\\key.txt', 'wb') as file:
        pickle.dump(key, file)
else:
    with open('data\\key.txt', 'rb') as file:
        key = pickle.load(file)
print(key.decode('ascii'))
cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt('admin'.encode('ascii')) .decode('ascii')
print((ciphered_text))


def login_callback(sender, app_data, user_data):
    Cursor.execute('SELECT username FROM USERS')
    usernames = Cursor.fetchall()
    Cursor.execute('SELECT password FROM USERS')
    passwords = Cursor.fetchall()

    users = dict(zip(map(lambda x: x[0], usernames),map(lambda x: x[0], passwords)))

    username = dpg.get_value("login_username")
    password = dpg.get_value("login_password")

    if username in users:
        cipher_suite = Fernet(key)
        ciphered_text = users[username].encode('ascii')
        pw = cipher_suite.decrypt(ciphered_text).decode('ascii')
        if password == pw:
            dpg.set_value("login_status", f"Welcome back, {username}!")
            query = f'''UPDATE USERS SET current = true WHERE username = "{username}"'''
            print(query)
            Cursor.execute(query)
            database.commit()
            print(Cursor.execute('SELECT * FROM USERS'))
            print('Updated...')
            os.execv(sys.executable, [sys.executable, 'sharedmemory.py'])
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
    username = dpg.get_value("login_username")
    password = dpg.get_value("login_password")
    # confirm_password = dpg.get_value("confirm_password")

    if username in users:
        dpg.set_value("login_status", "Username already exists. Please choose another.")
    # elif password != confirm_password:
    #     dpg.set_value("register_status", "Passwords do not match. Please try again.")
    elif len(username) > 5:
        cipher_suite = Fernet(key)
        ciphered_text = cipher_suite.encrypt(password.encode('ascii')) .decode('ascii')
        print(len(ciphered_text))
        query = f'''INSERT INTO USERS VALUES ('{username}', '{ciphered_text}', false)'''
        Cursor.execute(query)
        database.commit()
        
        dpg.set_value("login_status", f"User '{username}' registered successfully!")
    elif len(username) <= 5:
        dpg.set_value("login_status", "Username must be longer than 5 characters")
dpg.create_context()
dpg.create_viewport(title='Barnes hut algorithm', width=400, height=200)
dpg.set_viewport_resizable(False)

with dpg.font_registry():
    df = dpg.add_font("data/fonts/Montserrat-Medium.ttf", 24)
    bf = dpg.add_font("data/fonts/Montserrat-Bold.ttf", 28)
    lf = dpg.add_font("data/fonts/Montserrat-Medium.ttf", 18)

with dpg.texture_registry():
    width, height, channels, data = dpg.load_image("300x300.gif")
    texture_id = dpg.add_static_texture(width, height, data)



with dpg.window(label="Login", tag = 'primary', pos=(0, 0), no_resize=True):
    t = dpg.add_text("User Login", color='')
    dpg.add_spacer(height=10)
    dpg.add_input_text(label="Username", tag="login_username")
    dpg.add_input_text(label="Password", tag="login_password", password=True)
    dpg.add_spacer(height=10)
    dpg.add_spacer(width=60)
    dpg.add_same_line()
    dpg.add_button(label="Login", callback=login_callback)
    dpg.add_same_line()
    dpg.add_spacer(width=50)
    dpg.add_same_line()
    dpg.add_button(label='Register', callback = register_callback)
    ls = dpg.add_text("", tag="login_status")
    dpg.bind_font(df)
    dpg.bind_item_font(t,bf)
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
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8, category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 2, category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("primary", True)

dpg.start_dearpygui()

dpg.destroy_context()
