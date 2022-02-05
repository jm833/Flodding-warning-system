# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from typing import Counter
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit
from floodsystem.utils import sorted_by_key


def rivers_with_station(stations):
    """find rivers monitored by given stations"""

    station_names = []
    for items in stations:
        station_names.append(items.name)

    rivers = set()

    # import the data of all the stations
    data = build_station_list()

    # check if a station is the stations given and add its river into the list
    for station in data:
        if station.name in station_names:
            rivers.add(station.river)

    all_rivers = list(rivers)
    all_rivers.sort()
    # return the rivers monitored by the given stations
    return all_rivers


def stations_by_river(stations):
    """find all the stations monitoring the given rivers"""

    river_names = []
    for items in stations:
        river_names.append(items.river)

    # import the data of all the stations
    data = build_station_list()

    river_stations = {}

    # pair a station to the corresponding river
    for station in data:
        if station.river in river_names:
            try:
                river_stations[station.river].append(str(station.name))
            except KeyError:
                river_stations[station.river] = [str(station.name)]

    # sort the value which is a list, did not work
    for key in river_stations:
        river_stations[key].sort()

    return river_stations


def rivers_by_station_number(stations, N):
    """sort all the rivers by the number of stations they have"""

    # import the data of all the stations
    data = build_station_list()

    # collect all the names of the rivers into a list
    river_names = []
    for item in stations:
        river_names.append(item.river)

    # count the number of stations monitoring a river
    counter = {}

    for station in data:
        if station.river in river_names:
            try:
                counter[station.river] += 1
            except KeyError:
                counter[station.river] = 1

    # turn the counting result into a list of tuples
    river_number = []
    for key, value in counter.items():
        river_number.append((key,value))

    # sort the rivers in a descending order of the number of stations monitoring it
    river_number.sort(key = lambda tup:tup[1], reverse=True)

    # pick out data we want
    f_result = []
    threshold = river_number[N][1]

    i = 0
    while river_number[i][1] >= threshold:
        f_result.append(river_number[i])
        i += 1

    return f_result


def stations_by_distance(stations, p):
    """Sort stations by distance"""

    #Create a list to hold the result
    station_distance = []
    
    #Append the list by MonitoringStation Objets and the distance between their coordinates and the given coordinate p
    for station in stations:
        distance = haversine(station.coord, p)
        station_distance.append((station, distance))
        
    return sorted_by_key(station_distance,1)

    

def stations_within_radius(stations, centre, r):
    """List all stations within a given radius r from a given centre"""

    result = [station for station in stations if haversine(station.coord, centre) <= r]
        
    return result
