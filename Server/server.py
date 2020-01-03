from flask import Flask
from flask import render_template
from yeelight import Bulb, RGBTransition, Flow, transitions

bulb0 = Bulb("192.168.1.181")
bulb1 = Bulb("192.168.1.182")

app = Flask(__name__)

@app.route('/')
def index():
    
    return (render_template('index.html'), 200)


# Turn the bulb on.
@app.route('/start_yeelight/<int:id_bulb>')
def start_yeelight(id_bulb=None):
    if id_bulb != None:
        if id_bulb == 0:
            bulb0.turn_on()
        elif id_bulb == 1:
            bulb1.turn_on()
    return ('', 204)
# Turn the bulb off.
@app.route('/stop_yeelight/<int:id_bulb>')
def stop_yeelight(id_bulb=None):
    if id_bulb != None:
        if id_bulb == 0:
            bulb0.turn_off()
        elif id_bulb == 1:
            bulb1.turn_off()
    return ('', 204)

# Toggle power.
@app.route('/toggle_yeelight/<int:id_bulb>')
def toggle_yeelight(id_bulb=None):
    if id_bulb != None:
        if id_bulb == 0:
            bulb0.toggle()
        elif id_bulb == 1:
            bulb1.toggle()
        elif id_bulb == 2:
            bulb0.toggle()
            bulb1.toggle()    
    return ('', 204)


####################### TEST #############################


flow = Flow(
    count=0,  # Cycle forever.
    transitions=transitions.christmas()
)

# Infinite color cycle
@app.route('/start_color_cycle_yeelight/<int:id_bulb>')
def cycle_yeelight(id_bulb=None):
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
def stop_cycle_yeelight(id_bulb=None):
    if id_bulb != None:
        if id_bulb == 0:
            bulb0.stop_flow()
        elif id_bulb == 1:
            bulb1.stop_flow()
        elif id_bulb == 2:
            bulb0.stop_flow()
            bulb1.stop_flow()    
    return ('', 204)


if __name__ == "__main__":
    app.run(debug=True, port=5000)