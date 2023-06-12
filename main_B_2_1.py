import pyxel

pyxel.init(120, 120)
pyxel.cls(13)
for i in range(13):
    pyxel.line(i*4, 0, 40+4*i,120 , 0)
pyxel.show()