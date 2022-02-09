from floodsystem.geo import *
from floodsystem.station import MonitoringStation

def test_stations_by_distance():
    station1 = MonitoringStation("s id", "m id","A station", (3.0,4.0),(0.0,1.0),"A river","A town")
    station2 = MonitoringStation("s id", "m id","B station", (6.0,8.0),(0.0,1.0),"B river","B town")

    stations = [station1,station2]
    sorted_station_by_distance = stations_by_distance(stations,(0.0,0.0))

    assert sorted_station_by_distance[0][0]== station1
   
    
test_stations_by_distance() 


def test_stations_within_radius():
    station1 = MonitoringStation("s id", "m id","A station", (0.0,0.1),(0.0,1.0),"A river","A town")
    station2 = MonitoringStation("s id", "m id","B station", (0.1,0.2),(0.0,1.0),"B river","B town")
    station3 = MonitoringStation("s id", "m id","C station", (9.0,9.0),(0.0,1.0),"C river","C town")
   
    stations_within_r = stations_within_radius([station1,station2,station3],(0.0,0.0),100)

    assert stations_within_r == [station1,station2] or [station2,station1]

test_stations_within_radius()
