import tkinter as tk
from quadtreetkinter import Point, Rectangle, QuadTree, return_nodes
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
           "green",
           "white",
           "brown",
           "blue",
           "gray"]

rect = Rectangle(width/2, height/2, width/2, height/2)

quadtree = QuadTree(rect,  50, '', canvas)

def spawn_particles(n, gauss = False):
    for i in range(n):
        try:
            if gauss:
                gaussian = rd.normal(width / 2, 100, size=(n, 2))
                x, y = int(gaussian[i][0]), int(gaussian[i][1])

            else:
                x, y = random.randrange(0, width), random.randrange(0, height)

            quadtree.insert(Point(x, y))
            #canvas.create_oval(x, y, x + 5, y + 5, fill=random.choice(colours))
            #canvas.create_text(x, y - 10, text=str([x, y]), fill='white')
        except:
            pass
def click(event = None):
    canvas.delete('e')
    quadtree.insert(Point(event.x,event.y))
    quadtree.mainloop()
    canvas.create_oval(event.x, event.y, event.x + 5, event.y + 5, fill=random.choice(colours))
    #print(len(return_nodes()))
    #canvas.create_text(event.x, event.y-10, text=str([event.x,event.y]), fill='white')
    #print(quadtree.points)

#spawn_particles(10000, False)
points = 100000
a = time.time()
gaussian = rd.normal(width / 2, 100, size=(points, 2))
x = list(quadtree.insert(Point(gaussian[i][0], gaussian[i][1])) for i in range(points))
#y = list(canvas.create_oval(int(gaussian[i][0]), int(gaussian[i][1]), int(gaussian[i][0]) + 3, int(gaussian[i][1]) + 3, fill='white') for i in range(points))
b = time.time()

print('loop time: ', b-a)
quadtree.mainloop()
end = time.time()
print(f'run time: {end - start}')
canvas.bind('<Button-1>', click)
tk.mainloop()

