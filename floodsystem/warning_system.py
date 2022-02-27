from datetime import timedelta
import numpy as np
from floodsystem.analysis import *
from floodsystem.station import *
from floodsystem.stationdata import *
from floodsystem.flood import *
from floodsystem.datafetcher import *
from matplotlib import dates

def polynomial_derivatives(station):
    """input: a station object
    output: a tuple of 1st and 2nd derivatives of the water-level polynomial at the latest time"""
    #convert to relative water levels
    station_rwl = [station, station.relative_water_level()]

    #fetch dates-level data and create a list of dates in numbers.
    dates, levels = fetch_measure_levels(station.measure_id, dt = timedelta(days = 5))
    dates_num = matplotlib.dates.date2num(dates)

    #give the best fit curve function and the time shift
    poly, timeshift =  polyfit(dates, levels, 3)
    latest_time = dates_num[-1] - timeshift
    #give the 1st derivative and the 2nd derivative of the water_level function.
    #can give different weight to the derivative in the following analysis
    dp_expression = poly.deriv()
    d2p_expression = poly.deriv(2)

    dp = dp_expression(latest_time)
    d2p = d2p_expression(latest_time)

    return (dp,d2p)






