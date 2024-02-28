import tkinter as tk
from quadtree import Point, Rectangle, QuadTree
import random
import time
from numpy import random as rd


start = time.time()
width, height = 700, 700
root = tk.Tk()
canvas = tk.Canvas(root, width = width, height = height, background='black')
canvas.pack()
colours = ["cyan",
           "magenta",
           "red",
           "blue",
           "gray"]

rect = Rectangle(width/2, height/2, width/2, height/2)

points = 50

quadtree = QuadTree(rect,  4, '')


# for i in range(10000):
#     x, y = random.randrange(0, width), random.randrange(0, height)
#     quadtree.insert(Point(x, y, 1))
#
#     canvas.create_oval(x, y, x + 4, y + 4, fill='white')
gaussian =rd.normal(width/2, 100, size = (points, 2))
p = []
for i in range(points):
    x, y = gaussian[i][0], gaussian[i][1]
    canvas.create_oval(x, y, x + 15, y + 15, fill=random.choice(colours))
    # p.append(Point(x,y))
    quadtree.insert(Point(x,y))

# print(quadtree.query(quadtree.boundary, []))
# range = Rectangle(300, 300, 120, 120)
# canvas.create_rectangle(range.x-range.w,range.y-range.h, range.x+range.w, range.y+range.h, outline = 'green' , width = 1)
# pts = []
# quadtree.query(range, pts)
# print(len(pts))
# for p in pts:
#     canvas.create_oval(p.x, p.y, p.x + 5, p.y + 5, fill='green')

print('total points = ', len(quadtree))
quadtree.display(canvas)
end = time.time()
print(f'time: {end - start}')
tk.mainloop()

