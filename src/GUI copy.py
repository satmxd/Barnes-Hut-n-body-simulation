import dearpygui.dearpygui as dpg
#from config import get_config
# out_queue = None
# def send_values():
#     config = get_config()
#     #print(sender, dpg.get_value(sender))
#     config.update_value('show_quadtree',dpg.get_value('struct'))
#     config.update_value('show_quadtree_depth',dpg.get_value('depth'))
#     config.update_value('quadtree_thickness',round(dpg.get_value('thickness'), 3))
#     config.update_value('quadtree_color',dpg.get_value('quadcol'))
#     config.update_value('background_color',dpg.get_value('bgcolor'))
#     config.update_value('show_config', dpg.get_value('showconfig'))
#     print(config.return_config())
#     print('Data sent')

def send_values():
    #print(sender, dpg.get_value(sender))
    data = {}
    data["show_quadtree"] = dpg.get_value('struct')
    data["show_quadtree_depth"] = dpg.get_value('depth')
    data["quadtree_thickness"] = round(dpg.get_value('thickness'), 3)
    data["quadtree_color"]= dpg.get_value('quadcol')
    data["background_color"] = dpg.get_value('bgcolor')
    data["show_config"] = dpg.get_value('showconfig')
    data['show_node_data'] = True
    data['save_frames'] = False
    data['secondary_color']= (0, 128, 0)
    data['width']= 800
    data['height']= 800
    data['particlemass']= 1
    data['dt']= 9
    data['show_centre_of_mass']= True
    if out_queue != None:
        out_queue.put(data)
        print('Data sent')
    else:
        print('No Queue found')
    # with open('config.txt', 'w') as file:
    #     file.write(str(data))

# def send_values():
#     #print(sender, dpg.get_value(sender))
#     config.show_quadtree = dpg.get_value('struct')
#     config.show_quadtree_depth = dpg.get_value('depth')
#     config.show_quadtree_depth = round(dpg.get_value('thickness'), 3)
#     config.quadtree_color= dpg.get_value('quadcol')
#     config.background_color = dpg.get_value('bgcolor')
#     config.show_config = dpg.get_value('showconfig')
#     config.G = dpg.get_value('G')
#     config.theta = dpg.get_value('theta')
#     config.damp = dpg.get_value('damp')
#     config.particlemass = dpg.get_value('pmass')
#     return ('Data sent')


def load_values():
    with open('config.txt', 'r') as file:
        print(file.read())


def main(data):
    global out_queue
    out_queue = out_q
    dpg.create_context()
    dpg.create_viewport(title='Config', width=250, height=800, resizable=False)


    #TODO: add rest of the options
    with dpg.window(label="General", width=250, height = 140, pos=(0,0), no_move=True, no_resize=True, no_close = True, no_collapse=True):
        dpg.add_text("General properties")
        dpg.add_color_edit(label="BG Color", tag = 'bgcolor', callback=send_values, user_data=out_q, display_mode=dpg.mvColorEdit_rgb)
        dpg.add_checkbox(label="Show config", tag = 'showconfig', callback = send_values, user_data=out_q)
        dpg.add_button(label="Send data", tag='senddata',callback=send_values, user_data=out_q)
        dpg.add_button(label="Load data", tag='loaddata',callback=load_values, user_data=out_q)


    with dpg.window(label="Quadtree", width=250, height = 200, pos=(0,140), no_move=True, no_resize=True, no_close = True, no_collapse=True):
        dpg.add_text("Internal quadtree properties")
        dpg.add_checkbox(label="Quadtree structure", tag = 'struct', callback = send_values, user_data=out_q)
        dpg.add_checkbox(label="Quadtree depth", tag = 'depth', callback = send_values, user_data=out_q)
        dpg.add_slider_float(label="Line thickness", default_value=1, max_value=5, width=100, tag = 'thickness', user_data=out_q, callback = send_values)
        dpg.add_color_edit(label="Color", tag = 'quadcol', callback=send_values, user_data=out_q, display_mode=dpg.mvColorEdit_hex)

    with dpg.window(label="Physics", width=250, height = 200, pos=(0,340), no_move=True, no_resize=True, no_close = True, no_collapse=True):
        dpg.add_text("Simulation settings")
        dpg.add_slider_float(label="Theta cutoff", default_value=0.35, max_value=1, width=100, tag = 'theta', user_data=out_q, callback = send_values)
        dpg.add_input_float(label="Gravitational constant G", width = 100, tag = 'G',default_value=0.766, user_data=out_q,callback = send_values)
        dpg.add_slider_float(label="Dampening factor", default_value=0.2, max_value=1, width=100, tag = 'damp', user_data=out_q, callback = send_values)
        dpg.add_input_int(label="Particle mass", width = 100, min_value=1, tag = 'pmass', user_data=out_q, callback=send_values)







    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == '__main__':
    main()