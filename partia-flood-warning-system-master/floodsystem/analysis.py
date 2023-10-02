import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    if len(levels) == 0:
        pass

    if type(dates) != list:
        raise RuntimeError("dates must form a list")
    if type(levels) != list:
        raise RuntimeError("levels must form a list")
    if type(p) != int:
        raise RuntimeError("p must be an integer")

    x = matplotlib.dates.date2num(dates)
    xs = sorted(x)
    y = levels

# Using shifted x values, find coefficient of best-fit
# polynomial f(x) of degree 4
    
    p_coeff = np.polyfit(x - xs[0], y, p)

# Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)

    return (poly, xs[-1] - xs[0])




