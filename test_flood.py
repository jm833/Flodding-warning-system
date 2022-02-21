from floodsystem.geo import *
from floodsystem.station import MonitoringStation
from floodsystem.flood import *



def test_relative_water_level():
    station1 = MonitoringStation("s id", "m id","A station", "coordinate", (0.5, 2.5),  "A river","A town")
    station2 = MonitoringStation("s id", "m id","B station", "coordinate", (0.03, 0.15), "B river","B town")
    station3 = MonitoringStation("s id", "m id","C station", "coordinate", (1.3, 1.8),  "C river","C town")
    station4 = MonitoringStation("s id", "m id","D station", "coordinate", (4, 1), "D river","D town")

    station1.latest_level = 2
    station2.latest_level = 0.1
    station3.latest_level = 2
    station4.latest_level = 2

    station1.relative_water_level == 0.75
    station3.relative_water_level == 1.4
    station4.relative_water_level == None

test_relative_water_level()




def test_stations_level_over_threshold():
    station1 = MonitoringStation("s id", "m id","A station", "coordinate", (0.5, 2.5),  "A river","A town")
    station2 = MonitoringStation("s id", "m id","B station", "coordinate", (0.03, 0.15), "B river","B town")
    station3 = MonitoringStation("s id", "m id","C station", "coordinate", (1.3, 1.8),  "C river","C town")
    station4 = MonitoringStation("s id", "m id","D station", "coordinate", (4, 1), "D river","D town")

    station1.latest_level = 2
    station2.latest_level = 0.1
    station3.latest_level = 2
    station4.latest_level = 2

    list = [station1, station2, station3, station4]

    assert len(stations_level_over_threshold(list, 1)) == 1
    assert stations_level_over_threshold(list, 1)[0][0].name == "C station"

test_stations_level_over_threshold()






def test_stations_highest_rel_level():
    station1 = MonitoringStation("s id", "m id","A station", "coordinate", (0.5, 2.5),  "A river","A town")
    station2 = MonitoringStation("s id", "m id","B station", "coordinate", (0.03, 0.15), "B river","B town")
    station3 = MonitoringStation("s id", "m id","C station", "coordinate", (1.3, 1.8),  "C river","C town")
    station4 = MonitoringStation("s id", "m id","D station", "coordinate", (4, 1), "D river","D town")

    station1.latest_level = 2
    station2.latest_level = 0.1
    station3.latest_level = 2
    station4.latest_level = 2

    list = [station1, station2, station3, station4]

    assert stations_highest_rel_level(list, 3)[0][0].name == "C station"
    assert stations_highest_rel_level(list, 3)[1][0].name == "A station"
    assert stations_highest_rel_level(list, 3)[2][0].name == "B station"
    assert len(stations_highest_rel_level(list, 3)) == 3


test_stations_highest_rel_level()
