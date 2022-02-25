import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import *
from floodsystem.stationdata import build_station_list
from floodsystem.analysis import *

def plot_water_levels(station, dates, levels):
    """displays a plot of the water level data against time for a station, including lines of the typical low and high levels"""

    # Plot
    plt.plot(dates, levels)
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title('Station{}'.format(station.name))

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """plots the water level data and the best-fit polynomial"""
    poly,time_shift = polyfit(dates, levels, p)
    plt.plot(dates, levels, 'real')
    plt.plot(dates, poly, 'best_fit')
    for d,l in zip(dates, levels):
        if l == station.typical_range[0]:
            plt.plot(d, l, marker='o', color='green')
        elif l == station.typical_range[1]:
            plt.plot(d, l, marker='*', color='red')
    plt.xlabel("Date")
    plt.ylabel("Water Level")
    plt.xticks(rotation = 45)
    plt.title("Station {}".format(station.name))
    plt.show()
    



    

