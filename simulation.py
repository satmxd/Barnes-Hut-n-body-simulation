import tkinter as tk
from quadtree import Point, Rectangle, QuadTree
import random
import time
from numpy import random as rd


start = time.time()
width, height = 800, 800
root = tk.Tk()
canvas = tk.Canvas(root, width = width, height = height, background='black')
canvas.pack()

rect = Rectangle(width/2, height/2, width/2, height/2)
quadtree = QuadTree(rect, 4)

# for i in range(1000):
#     x, y = random.randrange(0, width), random.randrange(0, height)
#     quadtree.insert(Point(x, y))
#
#     canvas.create_oval(x, y, x + 4, y + 4, fill='white')
points = 5000
gaussian =rd.normal(width/2, 100, size = (points, 2))

for i in range(points):
    x, y = gaussian[i][0], gaussian[i][1]
    canvas.create_oval(x, y, x + 4, y + 4, fill='white')
    quadtree.insert(Point(x, y))

quadtree.display(canvas)

end = time.time()
print(end - start)
tk.mainloop()

