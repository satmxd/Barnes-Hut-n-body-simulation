from multiprocessing import Process, Manager

import GUI
import simulationpygame
import mysql.connector

database = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="*SatvikMYSQL*",
database="bhauserdb"
)

Cursor = database.cursor()

if __name__ == '__main__':
    manager = Manager()

    shared_data = manager.dict()
    d = {
    #savefile#
    'username' : 'null',
    'save_name' : 'null',
    'save_time' : None,
    #general#
    'show_config' : False,
    'show_node_data': False,
    'save_frames': False,###############
    'background_color': (0,0,0),
    'secondary_color': (0, 128, 0),
    'width': 1200,
    'height': 800,

    #simulation#
    'particlemass':1,
    'dt':9,
    'theta':0.35,
    'G':0.766,
    'damp':0.2,
    #loadingsim#
    'num_of_particles':100,
    'premade_sim_type': 'Gaussian',
    'should_load':False,
    'override_sim':False,


    #quadtree#
    'show_quadtree': False,
    'pthresh': 4,
    'show_quadtree_depth': False,
    'show_centre_of_mass': False,
    'quadtree_thickness': 1,
    'quadtree_color': '#008000'
}
    #name = input("Enter username: ")
    Cursor.execute('SELECT username FROM users WHERE current = true')
    names = Cursor.fetchall()[0]
    print(names[0])
    d['username'] = names[0]

    Cursor.execute(f'''UPDATE USERS SET current = false WHERE username = "{names[0]}"''')
    database.commit()
    shared_data.update(d)

    p1 = Process(target=GUI.main, args=(shared_data,))
    p2 = Process(target=simulationpygame.main, args=(shared_data,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()