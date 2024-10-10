import math
#import seaborn as sb

theta = 0.35
G = 0.766
damp = 0.2

floatcutoff = 0.001
# r = sb.color_palette('mako', 29)
# colorrange = r.as_hex()[2:]
colorrange = ['#4a1079', '#56147d', '#621980', '#6d1d81', '#792282', '#842681', '#912b81', '#9c2e7f', '#aa337d', '#b73779', '#c23b75', '#cf4070', '#d9466b', '#e44f64', '#ec5860', '#f3655c', '#f7725c', '#fa815f', '#fc8e64', '#fe9d6c', '#feaa74', '#feb97f', '#fec68a', '#fed597', '#fde2a3', '#fcf0b2', "#fcf5cf"]
#colorrange = ['#3d0f71', '#4a1079', '#56147d', '#621980', '#6d1d81', '#792282', '#842681', '#912b81', '#9c2e7f', '#aa337d', '#b73779', '#c23b75', '#cf4070', '#d9466b', '#e44f64', '#ec5860', '#f3655c', '#f7725c', '#fa815f', '#fc8e64', '#fe9d6c', '#feaa74', '#feb97f', '#fec68a', '#fed597', '#fde2a3', '#fcf0b2']

##########################
data = {

#general#
    'show_config' : False,
    'show_node_data': True,
    'save_frames': False,###############
    'background_color': '#000000',
    'secondary_color': '#008000',
    'width': 1200,
    'height': 800,

#simulation#
    'particlemass':1,
    'dt':9,
#quadtree#
    'show_quadtree': True,
    'show_quadtree_depth': True,
    'show_centre_of_mass': True,
    'quadtree_thickness': 1,
    'quadtree_color': '#008000'
}

def update_value(key, value):
    if key in data:
        data[key] = value

def get_value(key):
    return data.get(key)

def return_config():
    return (data)



# def update_config():
#     print('updating..')
#     with open('config.txt', 'r') as file:
#         global data
#         data = eval(file.read())
#     print(data)

        
# update_config()
# print(data)

#general config#
show_config = False
show_node_data = True
save_frames = False
background_color = '#000000'
secondary_color = '#008000'
width, height = 1200, 800
#quadtree#
show_quadtree = True
show_quadtree_depth = True
show_centre_of_mass = True
quadtree_thickness = 1
quadtree_color = '#008000'
##########################

