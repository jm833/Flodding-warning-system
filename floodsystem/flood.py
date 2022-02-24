import imp
from floodsystem.stationdata import build_station_list
from . import datafetcher
from .station import MonitoringStation
from floodsystem.stationdata import update_water_levels

def stations_level_over_threshold(stations, tol):
    """find stations which has relative water level(rwl) higher than a threshold"""

    # fetch the latest data of each river
    update_water_levels(stations)
    river_over_tol = []

    #find rivers with rwl higher than a threshold 
    for station in stations:
        if station.relative_water_level() == None:
            continue
        elif station.relative_water_level() > tol:
            river_over_tol.append((station, station.relative_water_level()))

    #sort the result
    river_over_tol.sort(key = lambda tup:tup[1], reverse=True)
    
    return river_over_tol



def stations_highest_rel_level(stations, N):
    """find the rivers under the highest risk of flooding"""
    
    # fetch data
    update_water_levels(stations)
    data = []

    # pair rivers with their relative water levle
    for station in stations:
        if station.relative_water_level() != None:
            data.append((station, station.relative_water_level()))
    
    # sort the rivers by their water level
    data.sort(key = lambda tup:tup[1], reverse=True)

    # return required number of rivers
    result = data[:N]

    return result



