import pyxel
import random

class Note:
    def __init__(self, lane, y, speed):
        self.lane = lane
        self.y = y
        self.speed = speed

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.lanes = {
            "w": 40,
            "a": 60,
            "s": 80,
            "d": 100
        }
        self.notes = []
        self.score = 0
        self.combo = 0
        self.miss = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if random.random() < 0.01:
            # Occasionally create a new note in a random lane
            self.notes.append(Note(random.choice(list(self.lanes.keys())), 0, random.randint(1, 3)))

        for note in list(self.notes):
            note.y += note.speed
            if note.y > 120:
                # The note has reached the bottom of the screen
                self.notes.remove(note)
                self.combo = 0
                self.miss += 1
            elif pyxel.btnp(getattr(pyxel, f"KEY_{note.lane.upper()}")) and 110 < note.y < 130:
                # The user has hit the note
                self.notes.remove(note)
                self.score += int(100 - abs(note.y - 120) / 10)
                self.combo += 1

    def draw(self):
        pyxel.cls(0)
        pyxel.text(5, 5, f"Score: {self.score}", 7)
        pyxel.text(5, 15, f"Combo: {self.combo}", 7)
        pyxel.text(5, 25, f"Miss: {self.miss}", 7)
        for note in self.notes:
            pyxel.circ(self.lanes[note.lane], note.y, 3, 8)
        pyxel.line(0, 120, 160, 120, 7)  # draw the line

App()
