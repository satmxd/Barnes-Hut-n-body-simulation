import math
import seaborn as sb

theta = 0.5
G = 0.8
dt = 8
floatcutoff = 0.01
r = sb.color_palette('rocket', 55)
colorrange = r.as_hex()[15:]


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