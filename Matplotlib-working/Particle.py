from random import uniform

class Point:
    def __init__(self, x, y, ax):
        self.x = x
        self.y = y
        self.mass = 1
        self.plot = ax

    def move(self):
        print('moving point')
        self.x += round(uniform(-1,1),3)
        self.y += round(uniform(-1,1),3)

    def render(self):
        print('rendering point')
        self.plot.plot(self.x, self.y, 'o', color = 'white', markersize = 2)

