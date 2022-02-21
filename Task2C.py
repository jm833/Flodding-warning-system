from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level

def run():
    """Test for stations_highest_rel_level function"""
    
    # fetch data
    stations = build_station_list()

    # print required result
    result = stations_highest_rel_level(stations, 10)

    mr = []
    for item in result:
        mr.append ((item[0].name, item[1]))

    print(mr)



if __name__ == "__main__":
    run()
