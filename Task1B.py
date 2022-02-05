from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list



def run():
    """Task 1B"""
    #Build a list of stations
    stations = build_station_list()

    #The coordinates of Cambridge city centre
    p = (52.2053, 0.1218)
    print(stations_by_distance)

    #Find the distance between all stations and Cambridge city centre
    station_distance = stations_by_distance(stations, p)
 
    #List only the name, town and distance of stations
    distance_list = [(stations.name, stations.town, distance)for (stations,distance) in station_distance]


    print("10 closest stations: ", distance_list[:10])
    print("10 farthest stations: ", distance_list[-10:])

run()