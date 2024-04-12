import math
import seaborn as sb

theta = 0.45
G = 0.82
dt = 9
floatcutoff = 0.01
# r = sb.color_palette('mako', 29)
# colorrange = r.as_hex()[2:]
colorrange = ['#251729', '#2d1d38', '#332345', '#382a54', '#3c3162', '#403872', '#413f80', '#40498e', '#3d5296', '#395d9c', '#37669e', '#3671a0', '#357ba3', '#3484a5', '#348ea7', '#3497a9', '#35a1ab', '#38aaac', '#3eb4ad', '#45bdad', '#50c6ad', '#60ceac', '#79d6ae', '#91dbb4', '#a9e1bd', '#bbe7c8', '#ceeed7']



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