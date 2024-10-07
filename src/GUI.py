import dearpygui.dearpygui as dpg



def send_values(sender):
    #print(sender, dpg.get_value(sender))
    data = {}
    data["show_quadtree"] = dpg.get_value('struct')
    data["show_quadtree_depth"] = dpg.get_value('depth')
    data["quadtree_thickness"] = round(dpg.get_value('thickness'), 3)
    data["quadtree_color"]= dpg.get_value('quadcol')
    data["background_color"] = dpg.get_value('bgcolor')
    data["show_config"] = dpg.get_value('showconfig')
    print(data)
    with open('config.txt', 'w') as file:
        file.write(str(data))

def load_values():
    with open('config.txt', 'r') as file:
        print(file.read())


def main():
    dpg.create_context()
    dpg.create_viewport(title='Config', width=250, height=800)



    with dpg.window(label="General", width=250, height = 140, pos=(0,0), no_move=True, no_resize=True, no_close = True, no_collapse=True):
        dpg.add_text("General properties")
        dpg.add_color_edit(label="BG Color", tag = 'bgcolor', callback=send_values, display_mode=dpg.mvColorEdit_hex)
        dpg.add_checkbox(label="Show config", tag = 'showconfig', callback = send_values)
        dpg.add_button(label="Send data", tag='senddata',callback=send_values)
        dpg.add_button(label="Load data", tag='loaddata',callback=load_values)


    with dpg.window(label="Quadtree", width=250, height = 200, pos=(0,140), no_move=True, no_resize=True, no_close = True, no_collapse=True):
        dpg.add_text("Internal quadtree properties")
        dpg.add_checkbox(label="Quadtree structure", tag = 'struct', callback = send_values)
        dpg.add_checkbox(label="Quadtree depth", tag = 'depth', callback = send_values)
        dpg.add_slider_float(label="Line thickness", default_value=1, max_value=5, width=100, tag = 'thickness', callback = send_values)
        dpg.add_color_edit(label="Color", tag = 'quadcol', callback=send_values, display_mode=dpg.mvColorEdit_hex)







    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

main()