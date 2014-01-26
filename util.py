import random

def rand_vals(xmax, ymax):
    x = random.randrange(0, xmax)
    y = random.randrange(0, ymax)
    return x, y

def norm_vec(x1, y1, x2, y2):
    vX = x1 - x2
    if vX != 0:
        vX = int(vX / abs(vX))
    vY = y1 - y2
    if vY != 0:
        vY = int(vY / abs(vY))
    return vX, vY

