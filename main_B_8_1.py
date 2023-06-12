import pyxel
pyxel.init(200,200)

start_x,start_y,end_x,end_y,flag =0,0,0,0,0
def update():
    global start_x,start_y,end_x,end_y,fla
    n =pyxel.btn(pyxel.KEY_SPACE)
    np = pyxel.btnp(pyxel.KEY_SPACE)
    if flag == False and np==True:
        start_x, start_y, end_x, end_y =0,0,0,0
    if n and np: #押し始めたとき
        start_x,start_y=pyxel.mouse_x,pyxel.mouse_y
    elif n or np: #押している間
        end_x,end_y=pyxel.mouse_x,pyxel.mouse_y
    flag = pyxel.btnp(pyxel.KEY_SPACE)
def draw():
    global a
    pyxel.cls(7)
    pyxel.line(start_x,start_y,end_x,end_y,0)

pyxel.run(update, draw)
