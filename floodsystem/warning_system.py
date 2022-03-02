from datetime import timedelta
from logging import warning
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
    if station.typical_range_consistent():
        
        
        #fetch dates-level data and create a list of dates in numbers.
        dates, levels = fetch_measure_levels(station.measure_id, dt = timedelta(days = 5))
        dates_num = matplotlib.dates.date2num(dates)
        try:
            levels = np.array(levels)
            levels = (levels - station.typical_range[0])/(station.typical_range[1]-station.typical_range[0])
        except(TypeError, ValueError, KeyError, TypeError):
            #print("error with levels")
            pass
        
        
        #give the best fit curve function and the time shift
        #give the 1st derivative and the 2nd derivative of the water_level function.
        #can give different weight to the derivative in the following analysis
        try:
            poly, timeshift =  polyfit(dates, levels, 3)
            latest_time = dates_num[-1] - timeshift
            dp_expression = poly.deriv()
            d2p_expression = poly.deriv(2)

            dp = dp_expression(latest_time)
            d2p = d2p_expression(latest_time)

            dpval = dp.item()
            d2pval = d2p.item()
        
            return (dpval,d2pval)

        except (IndexError, ValueError, TypeError):
            #print("error with poly or latest time")
            pass

      
     
        
        
        


      
    
        


def obtain_rwl(station):
    rwl = station.consistent_relative_water_level()

    return rwl

def calculate_kvalue(stations):
    data = build_station_list()

    valid_rivers = []

    for station in stations:
        if station.typical_range_consistent():
            valid_rivers.append(station)
    
    k = dict()

    for v in valid_rivers:
        a = obtain_rwl(v)
        b = (polynomial_derivatives(v)[0])
        c = (polynomial_derivatives(v)[1])
        kvalue = 0.63 * a + 0.36 * b + 0.01 * c
        k[v.name] = kvalue
    
    return type(a)

def issue_warning(stations):
    k = calculate_kvalue(stations)
    alert = None

    warning = dict()

    for key, value in k.items():
        if value >= 1.5:
            alert = key + "(green flooding alert)"
            warning[key] = alert
        elif value >= 1.9:
            alert = key + "(yellow flooding alert)"
            warning[key] = alert
        elif value >= 2.2:
            alert = key + "(red flooding alert)"
            warning[key] = alert
    
    return warning



