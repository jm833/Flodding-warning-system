from floodsystem.plot import *
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list

stations = build_station_list()

#produce the x and y variable: the 5 most risky rivers and their levels
data= stations_highest_rel_level(stations,5)
station = []
station.append(data[i][0] for i in range(5))

#plots the water levels over the past 2 days for the 5 stations at which the current relative water level is greatest.
for i in stations:
    for s in station:
        if s == i.name:
            dates, levels = fetch_measure_levels(i.measure_id, dt = timedelta(2))

            plot_water_level_with_fit(station, dates, levels, p=4)