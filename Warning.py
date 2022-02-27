from floodsystem.warning_system import *
from floodsystem.stationdata import build_station_list

def run():
    data = build_station_list()

    for station in data:
        try:
            print(type(polynomial_derivatives(station)[0]))
            print(type(polynomial_derivatives(station)[1]))
        except TypeError:
            print(0,0)
            
        

    # print(issue_warning(data))


if __name__ == "__main__":
    run()

