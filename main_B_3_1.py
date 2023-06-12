import pyxel

pyxel.init(240, 240)
pyxel.cls(13)
for k in range(13):
    for i in range(13):
        pyxel.line(20*k, 0, 20*i,240 , 0)
pyxel.show()