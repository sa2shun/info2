import pyxel

pyxel.init(200, 200)
pyxel.cls(13)
for k in range(10):
    for i in range(10):
        col = 6 if (k+i) %2 == 0 else 14
        pyxel.circ(10+20*k, 10+20*i,10 , col)
pyxel.show()