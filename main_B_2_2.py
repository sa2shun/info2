import pyxel

pyxel.init(120, 120)
pyxel.cls(13)
for i in range(12):
    pyxel.line(i*10, 0,0, 120-i*10, 0)
pyxel.show()