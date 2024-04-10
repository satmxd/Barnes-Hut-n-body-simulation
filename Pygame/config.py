import math

import numpy

theta = 0.5
G = 0.449
dt = 10
floatcutoff = 0.002

def force(mass, x, y,d, body):
    if d > floatcutoff:
        f = G*mass*body.mass/(d**2)
        dx = body.com[0] - x
        dy = body.com[1] - y
        angle = math.atan2(dy, dx)
        fx = math.cos(angle) * f
        fy = math.sin(angle) * f
        #print(fx, fy, body.depth)
        return (fx, fy)
    else:
        return (0,0)