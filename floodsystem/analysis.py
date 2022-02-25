import numpy as np
import matplotlib


def polyfit(dates, levels, p):
    """a function that given the water level time history (dates, levels) 
    for a station computes a least-squares fit of a polynomial of degree p 
    to water level data. 
    return: a tuple of (i) the polynomial object and 
    (ii) any shift of the time (date) axis"""
    x_f = matplotlib.dates.date2num(dates)
    x = [i - x_f[0] for i in x_f]
    y = levels

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree p
    p_coeff = np.polyfit(x , y, p)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)


    return poly, x_f[-1]



