from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

def run():
    """Test for Stations_level_over_threshold function"""

    # fetch data
    stations = build_station_list()

    # print required result
    result = stations_level_over_threshold(stations, 2)

    mr = []
    for item in result:
        mr.append ((item[0].name, item[1]))

    print(mr)



if __name__ == "__main__":
    run()


