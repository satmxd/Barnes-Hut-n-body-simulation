from dataclasses import dataclass
import dearpygui.dearpygui as dpg

import mysql.connector

database = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="*SatvikMYSQL*",
database="bhadb"
)

Cursor = database.cursor()
Cursor.execute('CREATE DATABASE IF NOT EXISTS bhadb')

#TODO- Update all data to database on clicking save button.
#TODO- Create table with username if not exists


def create_table():
    username = data['username']
    Cursor.execute(f"SHOW TABLES LIKE '{username}'")
    if Cursor.fetchone():
        print('Table exists, continuing...')
    else:
        print('Creating table')
        Cursor.execute(f"CREATE TABLE IF NOT EXISTS {username} (load_id int PRIMARY KEY)")
        for key, value in data.items():
            try:
                if type(value) in (tuple, list, str):
                    Cursor.execute(f"""ALTER TABLE {username} ADD {key} varchar(25)""")
                elif value == None:
                    if key == 'save_time':
                        Cursor.execute(f"""ALTER TABLE {username} ADD {key} datetime""")
                else:
                    Cursor.execute(f"""ALTER TABLE {username} ADD {key} {str(type(value))[8:].rstrip("'>")}""")
            except Exception as e:
                print(f'Error occured {e} at value: {key, value}')
        # Cursor.execute("ALTER TABLE admin ADD save_name varchar(25) AFTER load_id")
        # Cursor.execute("ALTER TABLE admin ADD save_time datetime AFTER load_id")
        Cursor.execute(f"DESC {username}")
        print(Cursor.fetchall())

def save_sim():
    create_table()
    values = [round(i, 3) if type(i) == float else [round(j) for j in i] if type(i) == list else i for i in data.values()[3:]]
    values = str([f"{i}" if type(i) in (tuple, str) else f"{tuple(i)}" if type(i) == list else i for i in values])
    Cursor.execute(f"SELECT COUNT(*) FROM {data['username']}")
    count = Cursor.fetchone()[0]
    print(count)
    load_id = count+1
    try:
        query = f'''INSERT INTO {data['username']} values ({load_id}, '{data['username']}', 'Save{load_id}', CURRENT_TIMESTAMP, {values.lstrip('[').rstrip(']')})'''
        print(query)
        Cursor.execute(query)
        database.commit()
        Cursor.execute(f"SELECT * FROM {data['username']}")
        print(Cursor.fetchall())
        print('Entry added...')
    except Exception as e:
        print(f'Error occured on entry: {e}')
    




def send_values():
    #print(sender, dpg.get_value(sender))
    if data != None:
        data["show_quadtree"] = dpg.get_value('struct')
        data["show_quadtree_depth"] = dpg.get_value('depth')
        data["quadtree_thickness"] = round(dpg.get_value('thickness'), 3)
        data["quadtree_color"]= dpg.get_value('quadcol')
        data["background_color"] = dpg.get_value('bgcolor')
        data["show_config"] = dpg.get_value('showconfig')
        data['show_node_data'] = dpg.get_value('nodedata')
        data['particlemass']= dpg.get_value('pmass')
        data['pthresh'] = dpg.get_value('pthresh')
        data['show_centre_of_mass']= dpg.get_value('showcom')
        data['save_frames'] = False
        data['secondary_color']= (0, 128, 0)
        data['width']= 800
        data['height']= 800
        data['dt']= 9
        data['G']=dpg.get_value('G')
        data['damp']=dpg.get_value('damp')
        data['theta']=dpg.get_value('theta')
        #print('Data sent: ', data)
    else:
        print('No data found')

def load_premade_sim():
    data['premade_sim_type']= dpg.get_value('premade_sim_type')
    data['num_of_particles']= dpg.get_value('num_of_particles')
    data['override_sim']=dpg.get_value('override_sim')
    data['should_load']=True




def load_values():
    with open('config.txt', 'r') as file:
        print(file.read())


def main(shared_data):
    global data
    data = shared_data
    dpg.create_context()
    dpg.create_viewport(title='Config', width=300, height=800, resizable=False)

    #TODO: add rest of the options
    with dpg.window(label="General", width=300, height = 130, pos=(0,0), no_move=True, no_resize=True, no_close = True, no_collapse=True):
        dpg.add_text("General properties")
        dpg.add_color_edit(label="BG Color", tag = 'bgcolor',default_value=(0,0,0), callback=send_values, display_mode=dpg.mvColorEdit_rgb)
        dpg.add_checkbox(label="Show config", tag = 'showconfig',default_value=False, callback = send_values)
        dpg.add_checkbox(label="Node data", tag = 'nodedata',default_value=False, callback = send_values)
        #dpg.add_button(label="Send data", tag='senddata',callback=send_values)
        #dpg.add_button(label="Load data", tag='loaddata',callback=load_values)

    with dpg.window(label="Quadtree", width=300, height = 190, pos=(0,130), no_move=True, no_resize=True, no_close = True, no_collapse=True):
        dpg.add_text("Internal quadtree properties")
        dpg.add_checkbox(label="Quadtree structure", tag = 'struct',default_value=False, callback = send_values)
        dpg.add_checkbox(label="Quadtree depth", tag = 'depth',default_value=False, callback = send_values)
        dpg.add_slider_int(label="Particle Threshold", default_value=4, max_value=25,min_value=1, width=100, tag = 'pthresh', callback = send_values)
        dpg.add_checkbox(label="Show centre of mass", tag = 'showcom',default_value=False, callback = send_values)
        dpg.add_slider_int(label="Line thickness", default_value=1, max_value=5,min_value=1, width=100, tag = 'thickness', callback = send_values)
        dpg.add_color_edit(label="Color", tag = 'quadcol',default_value=(0, 128, 0), callback=send_values, display_mode=dpg.mvColorEdit_rgb)

    with dpg.window(label="Physics", width=300, height = 180, pos=(0,320), no_move=True, no_resize=True, no_close = True, no_collapse=True):
        dpg.add_text("Simulation settings")
        dpg.add_slider_float(label="Theta cutoff", default_value=0.35, max_value=1, width=100, tag = 'theta', callback = send_values)
        dpg.add_input_float(label=" ", width = 100, tag = 'G',default_value=0.766,callback = send_values)
        dpg.add_text("Gravitational constant G")
        dpg.add_slider_float(label="Dampening factor", default_value=0.2, max_value=1, width=100, tag = 'damp', callback = send_values)
        dpg.add_slider_int(label="Particle mass", width = 100,default_value=1, min_value=1,max_value=50, tag = 'pmass', callback=send_values)


    with dpg.window(label="Saving/Loading", width=300, height = 275, pos=(0,500), no_move=True, no_resize=True, no_close = True, no_collapse=True):
        dpg.add_text("Click to save each frame as .png")
        dpg.add_text("Warning! Running long simulations")
        dpg.add_text("require much more memory!")
        dpg.add_checkbox(label="Save frames", tag = 'saveframes',default_value=False, callback = send_values)

        dpg.add_text("Load premade simulations: ")
        dpg.add_combo(("Random", "Gaussian", "Doughnut"), default_value= "Gaussian", tag='premade_sim_type')
        dpg.add_input_int(label='Number of particles', min_value=1, max_value=1000, tag = 'num_of_particles')
        dpg.add_checkbox(label='Override current sim?', default_value=False, tag='override_sim')
        dpg.add_button(label = "Load simulation", callback=load_premade_sim)

        dpg.add_button(label='Save simulation', callback=save_sim)





    dpg.setup_dearpygui()
    dpg.show_viewport()
    while dpg.is_dearpygui_running():
        #print(shared_data)
        dpg.render_dearpygui_frame()
    dpg.destroy_context()




# def init(shared_data):
#     main()
#     send_values(shared_data)

if __name__ == '__main__':
    main()