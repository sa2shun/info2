import pyxel

pyxel.init(200,200)
x=0
y=0
def update():
    global x,y
    if pyxel.btn(pyxel.KEY_SPACE):
        x,y = pyxel.mouse_x,pyxel.mouse_y
def draw():
    global a
    pyxel.cls(7)
    pyxel.line(0,0,x,y,0)

pyxel.run(update, draw)