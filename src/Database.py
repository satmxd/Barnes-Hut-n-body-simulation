from datetime import datetime
import mysql.connector

database = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="mysql",
database="bhadb"
)
data = {


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
    'quadtree_color': (0, 128, 0)
}
Cursor = database.cursor(buffered=True)

Cursor.execute("CREATE DATABASE IF NOT EXISTS BHAdb")
Cursor.execute("SHOW DATABASES")
username = input('Enter username: ')
Cursor.execute(f"CREATE TABLE IF NOT EXISTS {username} (load_id int PRIMARY KEY)")
Cursor.execute("DESC admin")
def init(data, override = False):
  if override:
    Cursor.execute(f"DROP TABLE {username}")
    Cursor.execute(f"CREATE TABLE {username} (load_id int PRIMARY KEY)")
    for key, value in data.items():
        try:
            if type(value) == tuple:
                Cursor.execute(f"""ALTER TABLE admin ADD {key} varchar(25)""")
                
            elif type(value) == str:
                Cursor.execute(f"""ALTER TABLE admin ADD {key} varchar({len(value)})""")

            else:
                Cursor.execute(f"""ALTER TABLE admin ADD {key} {str(type(value))[8:].rstrip("'>")}""")
        except Exception as e:
            print(e, key, value)


    Cursor.execute("ALTER TABLE admin ADD save_name varchar(25) AFTER load_id")
    Cursor.execute("ALTER TABLE admin ADD save_time datetime AFTER load_id")

init(data, False)
values = str([f"{i}" if type(i) in (tuple, str) else i for i in data.values()])
Cursor.execute(f"SELECT COUNT(*) FROM {username}")
count = Cursor.fetchone()[0]
print(count)
load_id = count+1
query = f'''INSERT INTO {username} values ({load_id}, CURRENT_TIMESTAMP, 'Save{load_id}', {values.lstrip('[').rstrip(']')})'''
print(query)
# Cursor.execute(query)
# database.commit()
