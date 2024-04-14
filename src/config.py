import math
import seaborn as sb

theta = 0.45
G = 0.82
dt = 15
floatcutoff = 0.01
r = sb.color_palette('mako', 29)
colorrange = r.as_hex()[2:]
#colorrange = ['#3d0f71', '#4a1079', '#56147d', '#621980', '#6d1d81', '#792282', '#842681', '#912b81', '#9c2e7f', '#aa337d', '#b73779', '#c23b75', '#cf4070', '#d9466b', '#e44f64', '#ec5860', '#f3655c', '#f7725c', '#fa815f', '#fc8e64', '#fe9d6c', '#feaa74', '#feb97f', '#fec68a', '#fed597', '#fde2a3', '#fcf0b2']



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
