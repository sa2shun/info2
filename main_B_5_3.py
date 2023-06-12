import pyxel

pyxel.init(200, 200)
pyxel.cls(13)
for k in range(10):
    for i in range(200):
        x = 20*k+i
        y = 200-i**2
        pyxel.circ(x, y,1 , 0)
pyxel.show()
