import pyxel
import random


class Note:
    def __init__(self):
        self.key = random.choice(['W', 'S', 'A', 'D'])
        self.point = -1
        self.x = random.randint(20, 180)
        self.y = -random.randint(0,5)
        self.speed = 2
        d = {'W': 5, 'S': 9, 'A': 14, 'D': 11}
        self.color = d[self.key]


class ListNote():
    def __init__(self):
        self.notes = []
        self.making_initialze_notes()
        self.scope = 0
        for i in range(0, 5):
            self.notes[i].y = -30 * i - i * random.randint(0, 20)
    def making_initialze_notes(self):
        for i in range(150):
            self.notes.append(Note())

    def update_notes(self):
        for i in range(self.scope, self.scope + 5):
            note = self.notes[i]
            note.y += note.speed
        if self.notes[self.scope].y >= 200:
            self.scope += 1


class App:
    def __init__(self):
        pyxel.init(200, 200)
        self.score = 0
        self.combo = 0
        self.max_combo = 0
        self.notes = ListNote()
        self.is_start = False
        self.is_end = False
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.is_start:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.is_start = True

        else:
            if self.is_end:
                return
            elif self.notes.scope >= 145:
                self.is_end = True
            self.notes.update_notes()
            self.notes.scope = self.notes.scope
            self.judge()
            self.score = 0
            for i in range(0,self.notes.scope):
                self.score += self.notes.notes[i].point

        if self.notes.notes[self.notes.scope].y <= self.notes.notes[self.notes.scope + 1].y:
            scope_note = self.notes.notes[self.notes.scope]
            next_note = self.notes.notes[self.notes.scope + 1]
            self.notes.notes[self.notes.scope] = next_note
            self.notes.notes[self.notes.scope + 1] = scope_note

    def judge(self):
        w = pyxel.btnp(pyxel.KEY_W)
        a = pyxel.btnp(pyxel.KEY_A)
        s = pyxel.btnp(pyxel.KEY_S)
        d = pyxel.btnp(pyxel.KEY_D)
        if self.notes.notes[self.notes.scope].point == -1:
            if (self.notes.notes[self.notes.scope].key == 'W' and w) or (self.notes.notes[self.notes.scope].key == 'A' and a) or (self.notes.notes[self.notes.scope].key == 'S' and s) or (self.notes.notes[self.notes.scope].key == 'D' and d):
                if abs(self.notes.notes[self.notes.scope].y - 188.5) <= 10:
                    self.notes.notes[self.notes.scope].point = 2
                    self.combo += 1
                    self.max_combo=max(self.max_combo,self.combo)
                elif abs(self.notes.notes[self.notes.scope].y - 188.5) <= 20:
                    self.notes.notes[self.notes.scope].point = 1
                    self.combo += 1
                    self.max_combo = max(self.max_combo, self.combo)
                else:
                    self.notes.notes[self.notes.scope].point = 0
                    self.combo = 0

    def draw(self):
        pyxel.cls(7)

        if not self.is_start:
            pyxel.text(50, 50, 'Rythme Game', 0)
            pyxel.text(50, 70, 'Press Space', 0)
        else:
            if self.is_end:

                pyxel.text(50, 50, 'Finished!', 0)
                pyxel.text(50, 70, f'SCORE:{self.score}' ,0)
                pyxel.text(50,90, f'COMBO BONUS!:+{self.max_combo}' ,0)
                pyxel.text(50, 110, f'Final Score:{self.score+self.max_combo}', 0)
                return
            pyxel.line(0, 185, 200, 185, 0)
            pyxel.line(0, 192, 200, 192, 0)

            for i in range(0, self.notes.scope + 5):
                note = self.notes.notes[i]
                if note.y <= 200:
                    pyxel.circ(note.x, note.y, 5, note.color)
                    pyxel.text(note.x, note.y, note.key, 0)
                    if note.point != -1:
                        score = ['Bad', 'Good', 'Perfect'][note.point]
                        pyxel.text(note.x+10, note.y, score, 0)
            pyxel.text(10, 10, f'SCORE:{str(self.score)}', 0)
            pyxel.text(10, 20, f'COMBO:{str(self.combo)}', 0)
            pyxel.text(10, 30, f'MAX_COMBO:{str(self.max_combo)}', 0)

            pyxel.text(10, 40, f'{self.notes.scope}', 0)

App()
