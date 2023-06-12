import pyxel
import random
class Ball():
    def __init__(self):
        self.x = random.randint(0,200)
        self.y = random.randint(0,150)
        self.angle = random.randint(30, 150)
        self.vx = pyxel.cos(self.angle) *2
        self.vy = pyxel.sin(self.angle) *5

    def reset_ball(self):
        self.x = random.randint(0, 200)
        self.y = 0
        self.angle = random.randint(30, 150)
        self.vx = pyxel.cos(self.angle) *2
        self.vy = pyxel.sin(self.angle) *5

class Balls():
    def __init__(self):
        self.balls = [Ball()]

    def add_ball(self):
        self.balls.append(Ball())

class Game():
    def __init__(self):
        pyxel.init(200, 200)
        pyxel.sound(0).set(notes='A2C3', tones='TT', volumes='33', effects='NN', speed=10)
        pyxel.sound(1).set(
            "r a1b1c2 b1b1c2d2 g2g2g2g2 c2c2d2e2" "f2f2f2e2 f2e2d2c2 d2d2d2d2 g2g2r r ",
            "s",
            "6",
            "nnff vfff vvvv vfff svff vfff vvvv svnn",
            25,
        )
        self.balls = Balls()

        self.pad_x = 0
        self.pad_y = 200
        self.count = 0
        self.flag10=False
        self.flag20=False
        pyxel.run(self.update, self.draw)

    def check(self):
        for ball in self.balls.balls:
            if ball.x -15 < self.pad_x < ball.x +5:
                pyxel.play(0,1)
                self.count += 1
            else:
                pyxel.play(0,0)

    def update(self):
        if self.count==10 and not self.flag10:
            self.balls.add_ball()
            self.flag10 = True

        if self.count==20 and not self.flag20:
            self.balls.add_ball()
            self.flag20= True

        self.pad_x = pyxel.mouse_x
        for ball in self.balls.balls:
            if ball.y >=200:
                self.check()
                ball.reset_ball()
            else:
                ball.x += ball.vx
                ball.y += ball.vy

            if ball.x <= 0 or ball.x >=200:
                ball.vx *= -1

    def draw(self):
        pyxel.cls(7)
        pyxel.text(100,100,str(self.count),2)
        for ball in self.balls.balls:
            pyxel.circ(ball.x,ball.y,5,0)
            pyxel.rect(self.pad_x, 195, 20, 5, 2)


Game()




