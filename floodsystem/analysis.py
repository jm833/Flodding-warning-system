import numpy as np
import matplotlib

def polyfit(dates, levels, p):
    """Returns a polynomial of degree p representing the best fit for a function
    f(dates) = levels. It offsets dates such that the minimum value of the domain
    is equal to 0 to prevent floating point errors. The offset is returned alongside
    the polynomial as (polynomial,offset)."""
    times = matplotlib.dates.date2num(dates)
    dt = np.min(times)
    times = times - dt
    p_coeff = np.polyfit(times, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, dt





