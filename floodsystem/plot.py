from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import *
from stationdata import build_station_list

def plot_water_levels(station, dates, levels):
    """displays a plot of the water level data against time for a station, including lines of the typical low and high levels"""

    # Plot
    plt.plot(dates, levels)
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title('Station:{}'.format(station.name))

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()