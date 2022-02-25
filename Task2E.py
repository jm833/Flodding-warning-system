from floodsystem.plot import *
from floodsystem.flood import *
from floodsystem.stationdata import *

def task2E():
    stations = build_station_list()

    #produce the x and y variable: the 5 most risky rivers and their levels
    risky_stations = stations_highest_rel_level(stations,5)
    risky_station_objects = [i[0] for i in risky_stations]


    #plots the water levels over the past 10 days for the 5 stations at which the current relative water level is greatest.
    for station in risky_station_objects:
        dates, levels = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days=10))

        plot_water_levels(station,dates,levels)
        plt.show()

if __name__ == "__main__":
    task2E()
