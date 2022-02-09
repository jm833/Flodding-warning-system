# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import *


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    #Create 3 stations, with last two having inconsistent data
    station1 = MonitoringStation("s id", "m id","some station", (1.0,2.2),(-2.3,3.4),"river x","my town")
    station2 = MonitoringStation("s id", "m id","some station", (1.0,2.2),(0.0,0.0),"river x","my town")
    station3 = MonitoringStation("s id", "m id","some station", (1.0,2.2),(1.0,0.5),"river x","my town")

    assert(station1.typical_range_consistent() is True)
    assert(station2.typical_range_consistent() is False)
    assert(station3.typical_range_consistent() is False)


def test_inconsistent_typical_range_stations():
    #Create 3 stations, with last two having inconsistent data
    station1 = MonitoringStation("s id", "m id","some station", (1.0,2.2),(-2.3,3.4),"river x","my town")
    station2 = MonitoringStation("s id", "m id","some station", (1.0,2.2),(0.0,0.0),"river x","my town")
    station3 = MonitoringStation("s id", "m id","some station", (1.0,2.2),(1.0,0.5),"river x","my town")
    station_list = [station1,station2,station3]

    assert(inconsistent_typical_range_stations[station_list]==[station2.name,station3.name])



    