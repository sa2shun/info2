import pyxel

pyxel.init(200,200)

a = 0
flag=1
def update():
    flag2 = pyxel.btnp(pyxel.KEY_SPACE)
    global a,flag
    if flag2 == True:
        flag =flag*-1
    if flag ==1:
        a+=1
    else:
        a-=1
    if a<=0:
        flag=1
    if a>=200:
        flag=-1

def draw():
    global a
    pyxel.cls(7)
    pyxel.circ(a, a, 10, 0)

pyxel.run(update, draw)