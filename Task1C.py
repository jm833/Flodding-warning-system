from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    """Task 1C"""
    #Build a list for stations
    stations = build_station_list()

    #Specify the coordinates of the given centre and the radius we want
    centre = (52.2053, 0.1218)
    r = 10

    #The list of station names within the radius
    station_list = [station.name for station in stations_within_radius(stations, centre, r)]

    #Sort the station list in alphabetical order
    print('stations within 10 km from Cambridge city centre: ', sorted(station_list))

run()