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

      
    
        


def calculate_kvalue(stations):
    update_water_levels(stations)

    valid_rivers = []
    green_alert = []
    yellow_alert = []
    red_alert = []

    for station in stations:
        if station.typical_range_consistent():
            valid_rivers.append(station)

    for v in valid_rivers:
        try:
            name = v.name
            a = v.relative_water_level()
            b = (polynomial_derivatives(v)[0])
            c = (polynomial_derivatives(v)[1])
            kvalue = 0.63 * a + 0.36 * b + 0.01 * c
            # print(kvalue)

            if kvalue >= 0.6:
                alert = name + "(green flooding alert)"
                green_alert.append(alert)
            elif kvalue >= 0.8:
                alert = name + "(yellow flooding alert)"
                yellow_alert.append(alert)
            elif kvalue >= 1:
                alert = name + "(red flooding alert)"
                red_alert.append(alert)
            else:
                continue

            
            

        except(TypeError,KeyError):
            pass


    print(green_alert)
    print(yellow_alert)
    print(red_alert)

