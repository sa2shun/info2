import pyxel



class Game():
    def __init__(self):
        pyxel.init(200, 200)
        self.ball_x = 0
        self.ball_y = 0
        self.angle = 0
        self.vx = 0
        self.vy = 0
        self.reset_ball()
        pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
        pyxel.sound(1).set(
            "r a1b1c2 b1b1c2d2 g2g2g2g2 c2c2d2e2" "f2f2f2e2 f2e2d2c2 d2d2d2d2 g2g2r r ",
            "s",
            "6",
            "nnff vfff vvvv vfff svff vfff vvvv svnn",
            25,
        )
        self.pad_x= 0
        self.pad_y = 200
        pyxel.run(self.update, self.draw)

    def reset_ball(self):
        self.ball_x = pyxel.rndi(0, 200)
        self.ball_y = 0
        self.angle = pyxel.rndi(30, 150)
        self.vx = pyxel.cos(self.angle)
        self.vy = pyxel.sin(self.angle)
    def check(self):
        if self.ball_x -5 < self.pad_x < self.pad_x +5:
            pyxel.play(0,1)
        else:
            pyxel.play(0,0)
    def update(self):
        self.pad_x = pyxel.mouse_x
        if self.ball_y >=200:
            self.check()
            self.reset_ball()
        else:
            self.ball_x += self.vx
            self.ball_y += self.vy

        if self.ball_x <= 0 or self.ball_x >=200:
            self.vx *= -1


    def draw(self):
        pyxel.cls(7)
        pyxel.circ(self.ball_x,self.ball_y,5,0)
        pyxel.rect(self.pad_x,195,10,5,2)
Game()