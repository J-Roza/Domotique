from flask import Flask
from flask import render_template
from yeelight import Bulb, RGBTransition, Flow, transitions, SleepTransition




bulb0 = Bulb("192.168.1.181", auto_on=True)
bulb1 = Bulb("192.168.1.182", auto_on=True)

bulb_list = [bulb0, bulb1, ]

app = Flask(__name__)

@app.route('/')
def index():    
    return (render_template('index.html'), 200)

@app.route('/bureau')
def bureau():    
    return (render_template('bureau.html'), 200)

@app.route('/test_page')
def test():
    return render_template('test_page.html')

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/salon')
def salon():
    return render_template('salon.html')






# Toggle power.
@app.route('/toggle_yeelight/<int:id_bulb>')
def toggle_yeelight(id_bulb=None):
    if id_bulb != None:
        for i, bulb in enumerate(bulb_list):
            if i == id_bulb:
                bulb.toggle(effect="sudden")
    return ('', 204)


####################### TEST #############################




# Infinite color cycle
@app.route('/start_color_cycle_yeelight/<int:id_bulb>')
def start_flow_yeelight(id_bulb=None):
    
    flow = Flow(
        count=0,  # Cycle forever.
        transitions=transitions.christmas()
    )

    if id_bulb != None:
        if id_bulb == 0:
            bulb0.start_flow(flow)
        elif id_bulb == 1:
            bulb1.start_flow(flow)
        elif id_bulb == 2:
            bulb0.start_flow(flow)
            bulb1.start_flow(flow)
    return ('', 204)

# Infinite color cycle stop
@app.route('/stop_color_cycle_yeelight/<int:id_bulb>')
def stop_flow_yeelight(id_bulb=None):
    if id_bulb != None:
        if id_bulb == 0:
            bulb0.stop_flow()
        elif id_bulb == 1:
            bulb1.stop_flow()
        elif id_bulb == 2:
            bulb0.stop_flow()
            bulb1.stop_flow()    
    return ('', 204)

# Turn the bulb on.
@app.route('/start_yeelight/<int:id_bulb>')
def start_yeelight(id_bulb=None):
    if id_bulb != None:
        if id_bulb == 0:
            bulb0.turn_on(effect="sudden")
        elif id_bulb == 1:
            bulb1.turn_on(effect="sudden")
        elif id_bulb == 2:
            bulb0.turn_on(effect="sudden")
            bulb1.turn_on(effect="sudden")
    return ('', 204)


# Turn the bulb off.
@app.route('/stop_yeelight/<int:id_bulb>')
def stop_yeelight(id_bulb=None):
    if id_bulb != None:
        if id_bulb == 0:
            bulb0.turn_off(effect="sudden")
        elif id_bulb == 1:
            bulb1.turn_off(effect="sudden")
        elif id_bulb == 2:
            bulb0.turn_off(effect="sudden")
            bulb1.turn_off(effect="sudden")
    return ('', 204)


#check the bulb’s state by reading its properties
@app.route('/check_state_yeelight/')
def check_state():
    properties = {}
    properties["bulb0"] = bulb0.get_properties()
    properties["bulb1"] = bulb1.get_properties()
    return {"properties": properties}, 200




#Set RGB Color
@app.route('/start_color_cycle_yeelight/<int:id_bulb>/<rgb_value>')
def rgb_yeelight(id_bulb=None, rgb_value="ffffff"):
   
    int_rgb = int(rgb_value, 16)

    b_color = int_rgb & 0b11111111
    g_color = int_rgb >> 8 & 0b11111111
    r_color = int_rgb >> 16 & 0b11111111
    
    if id_bulb != None:
        if id_bulb == 0:
            bulb0.set_rgb(r_color, g_color, b_color, effect="sudden")
        elif id_bulb == 1:
            bulb1.set_rgb(r_color, g_color, b_color, effect="sudden")
        elif id_bulb == 2:
            bulb0.set_rgb(r_color, g_color, b_color, effect="sudden")
            bulb1.set_rgb(r_color, g_color, b_color, effect="sudden")
            

    return ('', 204)




if __name__ == "__main__":
    app.run(debug=True, port=5000)