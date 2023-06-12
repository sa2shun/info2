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

        pyxel.run(self.update, self.draw)

    def reset_ball(self):
        self.ball_x = pyxel.rndi(0, 200)
        self.ball_y = 0
        self.angle = pyxel.rndi(30, 150)
        self.vx = pyxel.cos(self.angle)
        self.vy = pyxel.sin(self.angle)

    def update(self):
        if self.ball_y >=200:
            self.reset_ball()
        else:
            self.ball_x += self.vx
            self.ball_y += self.vy

        if self.ball_x <= 0 or self.ball_x >=200:
            self.vx *= -1

    def draw(self):
        pyxel.cls(7)
        pyxel.circ(self.ball_x,self.ball_y,5,0)

Game()