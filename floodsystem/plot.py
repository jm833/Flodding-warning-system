from turtle import color
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
    plt.axhline(station.typical_range[0],label = "typical low", color = "g")
    plt.axhline(station.typical_range[1],label = "typical high", color = "r")
    plt.title('Station:{}'.format(station.name))

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the historical water levels of station given by dates and levels.
    It then plots those levels along with a polynomial best fit of degree
    p which can then be used to estimate future water levels"""

    plt.plot(dates,levels,label = "real")

    best_fit, offset = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)
    y = best_fit(x - offset)
    plt.plot(dates, y, label="Best Fit")
    plt.axhline(station.typical_range[0],label = "typical low", color = "g")
    plt.axhline(station.typical_range[1],label = "typical high", color = "r")
    plt.title('Station:{}'.format(station.name))
    plt.legend()
    plt.show()
    



    

