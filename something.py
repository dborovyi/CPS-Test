import time
from tkinter import *

class CPSScore:
    def __init__(self, root, color):
        self.root = root
        self.score = 0
        self.id = self.root.create_text(150, 60, text=self.score, font=("SF Pro Display", 45), fill=color)
        self.root.bind_all('<Button-1>', self.add_click)
        self.root.bind_all('<space>', self.add_click)

    def add_click(self, evt):
        self.score += 1
        self.root.itemconfig(self.id, text=self.score)
        total_clicks.score += 1
        total_clicks.root.itemconfig(total_clicks.id, text=f"total:{total_clicks.score}")

    def drop(self):
        self.score = 0
        self.root.itemconfig(self.id, text=self.score)

class CPSText:
    def __init__(self, root, color):
        self.root = root
        self.id = self.root.create_text(150, 20, text="your cps below:", font=("SF Pro Display", 12), fill=color)

class TotalClicks:
    def __init__(self, root, color):
        self.root = root
        self.score = 0
        self.id = self.root.create_text(100, 100, text=f"total:{self.score}", font=("SF Pro Display", 12), fill=color)

class HighScore:
    def __init__(self, root, color):
        self.root = root
        self.score = [0]
        self.id = self.root.create_text(200, 100, text=f"high:{self.score[0]}", font=("SF Pro Display", 12), fill = color)

    def draw(self):
        if self.score[0] <= cps.score:
            self.score.insert(0, int(cps.score))
            del self.score[-1]
            self.root.itemconfig(self.id, text=f"high:{self.score[0]}")

window = Tk()
window.resizable(0, 0)
root = Canvas(window, background="white", width=300, height=120, highlightthickness=0)
root.pack()

top_text = CPSText(root, "grey")
cps = CPSScore(root, "grey")
total_clicks = TotalClicks(root, "grey")
high = HighScore(root, "grey")
window.title(f"Clicks Per Second: {cps.score}")

fps = "60"

while True:
    cps.drop()
    for x in range(int(fps)):
        time.sleep(1/int(fps))
        window.update()
        high.draw()
        window.title(f"Clicks Per Second: {cps.score}")