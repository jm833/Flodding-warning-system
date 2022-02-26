from floodsystem.plot import *
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list

def task2F():
    """Task 2F"""
    dt = 2
    N = 5
    p = 4

    # Build list of stations
    stations = build_station_list()
    
    # Get the station objects out of the list of names
    risky_stations = stations_highest_rel_level(stations, N)
    risky_station_objects = [i[0] for i in risky_stations]

    for station in risky_station_objects:
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        if len(dates) == 0 or len(levels) == 0:
            continue  # Deal with empty lists appearing
        plot_water_level_with_fit(station, dates, levels, p)
        plt.show()
    

if __name__ == "__main__":

    # Run Task2F
    task2F()