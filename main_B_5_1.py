import pyxel

pyxel.init(200, 200)
pyxel.cls(13)
for k in range(10):
    for i in range(10):
        if k+i <= 4:
            col =2
        elif k+i <=9 :
            col = 3
        elif k+i <= 14:
            col = 6
        else:
            col =14
        pyxel.circ(10+20*k, 10+20*i,10 , col)
pyxel.show()