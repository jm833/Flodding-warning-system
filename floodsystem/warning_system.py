from datetime import timedelta
from scipy.misc import derivative
from floodsystem.analysis import *
from floodsystem.station import *
from floodsystem.stationdata import *
from floodsystem.flood import *
from floodsystem.datafetcher import *
from matplotlib import dates


def risk_assessment():

    #give a list of station objects with valid data
    stations = build_station_list()
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    valid_station = [i for i in stations if i.name != s for s in inconsistent_stations]
    
    #give a list of station objects with relative water levels greater than 0.8, which are worth analysed.
    analysed_stations = level_over_threshold(valid_station, 0.8)
    station_rwl = [analysed_stations, analysed_stations.relative_water_level()]

    #fetch dates-level data and create a list of dates in numbers.
    dates, levels = fetch_measure_levels((i.measure_id for i in analysed_stations), dt = timedelta(days = 5) )
    dates_num = matplotlib.dates.date2num(dates)

    #give the best fit curve function and the time shift
    poly, timeshift =  polyfit(dates, levels, 3)
    latest_time = dates_num[-1] - timeshift

    #give the 1st derivative and the 2nd derivative of the water_level function.
    #can give different weight to the derivative in the following analysis
    dp = derivative(poly,latest_time)
    d2p = derivative(dp, latest_time)









