"""
1D
Check for non repetition in list and dictionary
Check for sorting

1E
length of the result
more must be equal in count
each greater than the next
"""

from unittest import result
from floodsystem.geo import *
from floodsystem.stationdata import build_station_list

def test_rivers_with_station():

    # get the data for testing
    stations = build_station_list()
    r = rivers_with_station(stations)

    # check less or equal number of items is in r    
    assert len(r) <= len(stations)

    # check for no repetition and sorted in alphabetical order
    for i in range(len(r) - 1):
        assert r[i] < r[i + 1]




def test_stations_by_river():

    stations = build_station_list()
    d = stations_by_river(stations)

    # check the list of station is sorted in alphabetical order
    # check the list of stations has no repetitions
    keys = []

    for key, value in d.items():
        keys.append(key)
        for i in range(len(value)-1):
            assert value[i] < value[i + 1]

    # produce a list of (river, station) pair recorded
    pair  = []
    for item in stations:
        if item.river != None and item.name != None:
            pair.append((item.river, item.name))
 
    # remove recorded data from a list of all (river, station) pairs
    for k, v in d.items():
        for i in range(len(v)):
            if (k, v[i]) in pair:
                pair.remove((k,v[i]))

    # check whether all the data is recorded and sorted
    for item in pair:
        assert item[0] not in keys






def test_rivers_by_station_number():
    """Test 1E, rivers by station number"""
    
    N = 9
    stations = build_station_list()

    # get data for testing
    r = rivers_by_station_number(stations, N)
    x = len(r)

    # check enough items in the list is printed
    assert x >= N
    
    # if more is printed than required,
    # check the extra rivers have the same number of stations compared to the last required river
    if x >= N:
        for i in range(x - N):
            assert r[x - 1 - i][1] == r[N-1][1]

    # check the result is sorted by number of stations
    for i in range(x-1):
        assert r[i][1] >= r[i+1][1]


