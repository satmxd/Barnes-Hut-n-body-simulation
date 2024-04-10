from quadtreematplotlib import Point, Rectangle, QuadTree, return_nodes
import random
import time
import datashader as ds
import pandas as pd
import colorcet as cc
import matplotlib.pyplot as plt
from numpy import random as rd
import numpy as np

start = time.time()
width, height = 900, 900

px = 1/plt.rcParams['figure.dpi']  # pixel in inches
fig, ax = plt.subplots(figsize=(height*px, width*px))
ax.set_facecolor("black")

colours = ["cyan",
           "magenta",
           "red",
           "green",
           "white",
           "brown",
           "blue",
           "gray"]

rect = Rectangle(width/2, height/2, width/2, height/2)

quadtree = QuadTree(rect,  4, '')

def main():
    points = 5
    a = time.time()
    gaussian = rd.normal(height / 2, 100, size=(points, 2))
    xpoints = []
    ypoints = []
    list(quadtree.insert(Point(gaussian[i][0], gaussian[i][1], ax)) for i in range(points))
    # list(xpoints.append(int(gaussian[i][0])) for i in range(points))
    # list(ypoints.append(int(gaussian[i][1])) for i in range(points))

    b = time.time()
    print('loop time: ', b-a)
    quadtree.display(ax)

    #plt.plot(xpoints, ypoints, 'o', color='white', marker='.', markersize=1)
    plt.plot(0,0)

    quadtree.mainloop()
    end = time.time()

    print(f'run time: {end - start}')
    print((quadtree.calculate_mass()))
    print(return_nodes())
    plt.show()


if __name__ == "__main__":
    main()






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
    # canvas.delete('e')
    quadtree.insert(Point(event.x,event.y))
    quadtree.mainloop()
    # canvas.create_oval(event.x, event.y, event.x + 5, event.y + 5, fill=random.choice(colours))
    #print(len(return_nodes()))
    #canvas.create_text(event.x, event.y-10, text=str([event.x,event.y]), fill='white')
    #print(quadtree.points)








#spawn_particles(10000, False)


# points = 2500
# a = time.time()
# gaussian = rd.normal(height / 2, 200, size=(points, 2))
# x = list(quadtree.insert(Point(gaussian[i][0], gaussian[i][1])) for i in range(points))
# y = list(arcade.draw_point(int(gaussian[i][0]), int(gaussian[i][1]), arcade.color.WHITE, 3) for i in range(points))
# b = time.time()
# print('loop time: ', b-a)
# quadtree.mainloop()
# end = time.time()

# print(f'run time: {end - start}')

# print(len(quadtree.query((rect), [])))

# arcade.finish_render()
# arcade.run()

# canvas.bind('<Button-1>', click)
# tk.mainloop()

